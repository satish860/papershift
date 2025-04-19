import argparse
import os
import sys
import json
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
    parser.add_argument(
        "--return-base64", action="store_true",
        help="Return base64 encoded images in JSON format"
    )
    parser.add_argument(
        "--no-store-output", action="store_true",
        help="Do not save images to disk (only applicable when --return-base64 is used)"
    )
    parser.add_argument(
        "--output-json", "-j", 
        help="Path to save the JSON output (only applicable when --return-base64 is used)"
    )
    
    args = parser.parse_args()
    
    # Validate PDF path
    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF file '{args.pdf_path}' not found", file=sys.stderr)
        return 1
    
    # Check if the user wants to disable storing output without returning base64
    if args.no_store_output and not args.return_base64:
        print("Error: --no-store-output can only be used with --return-base64", file=sys.stderr)
        return 1
    
    try:
        # Convert PDF to images
        result = convert_pdf_to_images_with_target_height(
            pdf_path=args.pdf_path,
            out_dir=args.output_dir if not args.no_store_output else None,
            dpi=args.dpi,
            target_height_px=args.target_height,
            aspect_threshold=args.aspect_threshold,
            return_base64=args.return_base64,
            store_output=not args.no_store_output
        )
        
        if args.return_base64:
            # Handle JSON output
            if args.output_json:
                with open(args.output_json, 'w') as f:
                    json.dump(result, f)
                print(f"JSON output saved to: {os.path.abspath(args.output_json)}")
            else:
                # Print JSON to stdout
                print(json.dumps(result))
            
            if not args.no_store_output:
                print(f"Successfully converted PDF to {len(result['file_paths'])} images")
                print(f"Images saved to: {os.path.abspath(args.output_dir)}")
        else:
            print(f"Successfully converted PDF to {len(result)} images")
            print(f"Images saved to: {os.path.abspath(args.output_dir)}")
        
        return 0
    except Exception as e:
        print(f"Error converting PDF: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
