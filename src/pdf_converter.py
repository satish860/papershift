import fitz  # pip install PyMuPDF
import os
import base64
import json
from typing import Union, Dict, List

def convert_pdf_to_images_with_target_height(
    pdf_path: str,
    out_dir: str = None,
    dpi: int = 300,
    target_height_px: int = 2048,
    aspect_threshold: float = 1.5,  # e.g. only bump if height/width > threshold
    return_base64: bool = False,
    store_output: bool = True
) -> Union[List[str], Dict[str, Union[List[str], List[Dict[str, str]]]]]:
    """
    Renders each page of pdf_path to a PNG, at `dpi` for crispness,
    then scales its height to at least `target_height_px` (if very tall),
    preserving aspect ratio.
    
    Args:
        pdf_path: Path to the PDF file
        out_dir: Directory to save the output images (required if store_output=True)
        dpi: DPI for image rendering
        target_height_px: Target height in pixels
        aspect_threshold: Aspect ratio threshold for height adjustment
        return_base64: If True, returns base64 encoded images in the result
        store_output: If True, saves images to disk at out_dir
        
    Returns:
        If return_base64=False and store_output=True: List of image file paths
        If return_base64=True: Dict with 'file_paths' (if store_output=True) and 'base64_images' keys
    """
    if store_output and not out_dir:
        raise ValueError("out_dir must be provided when store_output=True")
    
    if store_output:
        os.makedirs(out_dir, exist_ok=True)
        
    doc = fitz.open(pdf_path)
    image_paths = []
    base64_images = []
    
    for i, page in enumerate(doc, start=1):
        # page.rect is in points (1pt = 1/72")
        w_pt, h_pt = page.rect.width, page.rect.height
        ar = h_pt / w_pt

        # decide final pixel‐height
        h_px = (
            max(target_height_px, int(ar * target_height_px))
            if ar > aspect_threshold
            else target_height_px
        )
        # zoom = px / pt  →  px = pt * zoom
        zoom = h_px / h_pt

        # but also factor in desired DPI: zoom_dpi = dpi/72
        # you can multiply them together if you want both effects:
        zoom_total = zoom * (dpi / 72)

        mat = fitz.Matrix(zoom_total, zoom_total)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        if store_output:
            out_path = os.path.join(out_dir, f"page_{i:03}.png")
            pix.save(out_path)
            image_paths.append(out_path)
            
        if return_base64:
            # Convert pixmap to base64
            img_bytes = pix.tobytes()
            img_b64 = base64.b64encode(img_bytes).decode('utf-8')
            base64_images.append({
                "page": i,
                "width": pix.width,
                "height": pix.height,
                "data": img_b64,
                "format": "png"
            })

    doc.close()
    
    # Return results based on flags
    if return_base64:
        result = {"order": [img["page"] for img in base64_images], "base64_images": base64_images}
        if store_output:
            result["file_paths"] = image_paths
        return result
    else:
        return image_paths
