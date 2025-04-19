"""
Example usage of the PDF to image converter.

This script demonstrates how to use the PDF converter with a sample PDF file.
"""
import os
import sys
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
    print(f"Output directory: {output_dir}")
    
    # Convert the PDF to images
    try:
        image_paths = convert_pdf_to_images_with_target_height(
            pdf_path=pdf_path,
            out_dir=output_dir,
            dpi=300,
            target_height_px=2048,
            aspect_threshold=1.5
        )
        
        print(f"\nSuccessfully converted PDF to {len(image_paths)} images:")
        for i, path in enumerate(image_paths, 1):
            print(f"  {i}. {path}")
        
        print(f"\nImages saved to: {os.path.abspath(output_dir)}")
        return 0
    
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
