"""
Example usage of the PDF to Markdown converter.

This script demonstrates how to use the PDF to Markdown converter with a sample PDF file.
"""
import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the src module
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.pdf_to_markdown import convert_pdf_to_markdown


def main():
    # Path to your PDF file
    pdf_path = "path/to/your/document.pdf"  # Replace with your PDF path
    
    # Output directory for the markdown files
    output_dir = "markdown_output"
    
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        print("Please update the 'pdf_path' variable with the path to your PDF file.")
        return 1
    
    print(f"Converting PDF to Markdown: {pdf_path}")
    
    try:
        # Example 1: Basic conversion with default settings
        print("\nExample 1: Basic conversion with default settings")
        markdown_content = convert_pdf_to_markdown(
            pdf_path=pdf_path,
            output_dir=output_dir,
            verbose=True
        )
        
        print(f"Markdown files saved to: {os.path.abspath(output_dir)}")
        print(f"Combined markdown length: {len(markdown_content)} characters")
        
        # Example 2: Custom settings
        print("\nExample 2: Custom settings")
        custom_output_dir = output_dir + "_custom"
        
        markdown_pages = convert_pdf_to_markdown(
            pdf_path=pdf_path,
            output_dir=custom_output_dir,
            dpi=150,  # Lower DPI for faster processing
            target_height_px=1024,  # Smaller height for faster processing
            prompt="Convert this document to markdown, preserving all tables and formatting",
            model="openrouter/google/gemini-2.0-flash-001",  # You can change the model
            combined_output=False,  # Get separate markdown for each page
            verbose=True
        )
        
        print(f"Markdown files saved to: {os.path.abspath(custom_output_dir)}")
        print(f"Number of pages processed: {len(markdown_pages)}")
        
        return 0
    
    except Exception as e:
        print(f"Error converting PDF to Markdown: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
