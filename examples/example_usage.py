"""
Example usage of the PDF to image converter.

This script demonstrates how to use the PDF converter with a sample PDF file.
"""
import os
import sys
import json
from pathlib import Path

# Add the parent directory to the path so we can import the src module
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.pdf_converter import convert_pdf_to_images_with_target_height


def main():
    # Path to your PDF file
    pdf_path = "path/to/your/document.pdf"  # Replace with your PDF path
    
    # Output directory for the images
    output_dir = "example_output"
    
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        print("Please update the 'pdf_path' variable with the path to your PDF file.")
        return 1
    
    print(f"Converting PDF: {pdf_path}")
    
    # Example 1: Standard conversion (save to disk only)
    print("\nExample 1: Standard conversion (save to disk only)")
    print(f"Output directory: {output_dir}")
    
    try:
        image_paths = convert_pdf_to_images_with_target_height(
            pdf_path=pdf_path,
            out_dir=output_dir,
            dpi=300,
            target_height_px=2048,
            aspect_threshold=1.5
        )
        
        print(f"Successfully converted PDF to {len(image_paths)} images:")
        for i, path in enumerate(image_paths, 1):
            print(f"  {i}. {path}")
        
        print(f"Images saved to: {os.path.abspath(output_dir)}")
        
        # Example 2: Get base64 encoded images and save to disk
        print("\nExample 2: Get base64 encoded images and save to disk")
        result = convert_pdf_to_images_with_target_height(
            pdf_path=pdf_path,
            out_dir=output_dir + "_base64",
            dpi=300,
            target_height_px=2048,
            aspect_threshold=1.5,
            return_base64=True,
            store_output=True
        )
        
        print(f"Successfully converted PDF to {len(result['file_paths'])} images")
        print(f"Images saved to: {os.path.abspath(output_dir + '_base64')}")
        print(f"Base64 data available for {len(result['base64_images'])} images")
        print(f"Page order: {result['order']}")
        
        # Save the JSON output to a file
        json_path = os.path.join(output_dir + "_base64", "output.json")
        with open(json_path, 'w') as f:
            json.dump(result, f)
        print(f"JSON output saved to: {os.path.abspath(json_path)}")
        
        # Example 3: Get base64 encoded images only (no disk storage)
        print("\nExample 3: Get base64 encoded images only (no disk storage)")
        result_base64_only = convert_pdf_to_images_with_target_height(
            pdf_path=pdf_path,
            dpi=150,  # Lower DPI for smaller base64 strings
            target_height_px=1024,  # Smaller height for smaller base64 strings
            aspect_threshold=1.5,
            return_base64=True,
            store_output=False
        )
        
        print(f"Successfully converted PDF to {len(result_base64_only['base64_images'])} base64 encoded images")
        print(f"Page order: {result_base64_only['order']}")
        print("No images were saved to disk")
        
        return 0
    
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
