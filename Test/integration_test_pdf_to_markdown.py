"""
Integration test for the PDF to Markdown converter.

This script demonstrates how to use the PDF to Markdown converter with a real PDF file.
It serves as both a test and an example of real-world usage.
"""
import os
import sys
import argparse
from pathlib import Path

# Add the parent directory to the path so we can import the src module
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.pdf_to_markdown import convert_pdf_to_markdown


def run_integration_test(pdf_path, output_dir="test_output", verbose=True):
    """
    Run an integration test with a real PDF file.
    
    Args:
        pdf_path: Path to a real PDF file
        output_dir: Directory to save the output markdown files
        verbose: If True, prints progress information
        
    Returns:
        True if the test passed, False otherwise
    """
    print(f"Running integration test with PDF: {pdf_path}")
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        return False
    
    try:
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Convert PDF to markdown
        markdown_content = convert_pdf_to_markdown(
            pdf_path=pdf_path,
            output_dir=output_dir,
            verbose=verbose
        )
        
        # Check if the conversion was successful
        if not markdown_content:
            print("Error: Conversion produced empty markdown content.")
            return False
        
        # Check if the combined file was created
        combined_file = os.path.join(output_dir, "combined.md")
        if not os.path.exists(combined_file):
            print(f"Error: Combined markdown file not created: {combined_file}")
            return False
        
        print(f"Integration test passed!")
        print(f"Markdown files saved to: {os.path.abspath(output_dir)}")
        print(f"Combined markdown length: {len(markdown_content)} characters")
        
        return True
    
    except Exception as e:
        print(f"Error during integration test: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Run integration test for PDF to Markdown converter")
    parser.add_argument("pdf_path", help="Path to a real PDF file for testing")
    parser.add_argument(
        "--output-dir", "-o", 
        default="test_output", 
        help="Directory to save the output markdown files (default: test_output)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print progress information"
    )
    parser.add_argument(
        "--data-dir", "-d",
        default="data",
        help="Directory containing PDF files (default: data, relative to Test directory)"
    )
    
    args = parser.parse_args()
    
    # If pdf_path is just a filename (not a full path), look for it in the data directory
    if not os.path.isabs(args.pdf_path) and not os.path.exists(args.pdf_path):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(test_dir, args.data_dir)
        potential_path = os.path.join(data_dir, args.pdf_path)
        if os.path.exists(potential_path):
            args.pdf_path = potential_path
    
    success = run_integration_test(
        pdf_path=args.pdf_path,
        output_dir=args.output_dir,
        verbose=args.verbose
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
