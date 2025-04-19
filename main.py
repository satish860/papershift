import argparse
import os
import sys
from src.pdf_converter import convert_pdf_to_images_with_target_height


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to images")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument(
        "--output-dir", "-o", 
        default="output_images", 
        help="Directory to save the output images (default: output_images)"
    )
    parser.add_argument(
        "--dpi", type=int, default=300, 
        help="DPI for image rendering (default: 300)"
    )
    parser.add_argument(
        "--target-height", type=int, default=2048, 
        help="Target height in pixels (default: 2048)"
    )
    parser.add_argument(
        "--aspect-threshold", type=float, default=1.5, 
        help="Aspect ratio threshold for height adjustment (default: 1.5)"
    )
    
    args = parser.parse_args()
    
    # Validate PDF path
    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF file '{args.pdf_path}' not found", file=sys.stderr)
        return 1
    
    try:
        # Convert PDF to images
        image_paths = convert_pdf_to_images_with_target_height(
            pdf_path=args.pdf_path,
            out_dir=args.output_dir,
            dpi=args.dpi,
            target_height_px=args.target_height,
            aspect_threshold=args.aspect_threshold
        )
        
        print(f"Successfully converted PDF to {len(image_paths)} images")
        print(f"Images saved to: {os.path.abspath(args.output_dir)}")
        
        return 0
    except Exception as e:
        print(f"Error converting PDF: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
