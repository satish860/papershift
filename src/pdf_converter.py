import fitz  # pip install PyMuPDF
import os

def convert_pdf_to_images_with_target_height(
    pdf_path: str,
    out_dir: str,
    dpi: int = 300,
    target_height_px: int = 2048,
    aspect_threshold: float = 1.5,  # e.g. only bump if height/width > threshold
) -> list[str]:
    """
    Renders each page of pdf_path to a PNG, at `dpi` for crispness,
    then scales its height to at least `target_height_px` (if very tall),
    preserving aspect ratio.
    """
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    image_paths = []
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

        out_path = os.path.join(out_dir, f"page_{i:03}.png")
        pix.save(out_path)
        image_paths.append(out_path)

    doc.close()
    return image_paths
