"""
Run PDF to Markdown conversion tests and display results.

This script tests the PDF to Markdown converter with specified PDF files
and displays the results without relying on accessing the output files directly.
"""
import os
import sys
import time
from pathlib import Path

# Add the parent directory to the path so we can import the src module
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.pdf_to_markdown import convert_pdf_to_markdown


def test_pdf_file(pdf_path, output_dir=None, verbose=True):
    """
    Test PDF to Markdown conversion for a single file.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the output markdown files
        verbose: If True, prints progress information
        
    Returns:
        Tuple of (success, markdown_content, duration)
    """
    if verbose:
        print(f"Testing PDF: {pdf_path}")
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        return False, None, 0
    
    try:
        # Record start time
        start_time = time.time()
        
        # Convert PDF to markdown
        markdown_content = convert_pdf_to_markdown(
            pdf_path=pdf_path,
            output_dir=output_dir,
            verbose=verbose
        )
        
        # Record end time
        end_time = time.time()
        duration = end_time - start_time
        
        # Check if the conversion was successful
        success = bool(markdown_content)
        
        if verbose:
            if success:
                print(f"Conversion successful!")
                print(f"Markdown length: {len(markdown_content)} characters")
                print(f"Duration: {duration:.2f} seconds")
            else:
                print("Error: Conversion produced empty markdown content.")
        
        return success, markdown_content, duration
    
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False, None, 0


def main():
    # PDF files to test
    pdf_files = [
        "1-pages.pdf",
        "10-pages.pdf"
    ]
    
    # Base directory for test files
    test_dir = os.path.dirname(os.path.abspath(__file__))
    # Data directory for PDF files
    data_dir = os.path.join(test_dir, "data")
    
    # Results
    results = {}
    
    # Run tests for each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(data_dir, pdf_file)
        
        # Create output directory based on PDF filename
        output_dir = os.path.join(test_dir, "output", os.path.splitext(pdf_file)[0])
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\n{'=' * 50}")
        print(f"Testing: {pdf_file}")
        print(f"{'=' * 50}")
        
        # Test the PDF file
        success, content, duration = test_pdf_file(
            pdf_path=pdf_path,
            output_dir=output_dir,
            verbose=True
        )
        
        # Store results
        results[pdf_file] = {
            "success": success,
            "duration": duration,
            "output_dir": output_dir,
            "content_length": len(content) if content else 0
        }
        
        # Display a sample of the markdown content
        if content:
            print("\nSample of markdown content:")
            print("-" * 50)
            # Display first 500 characters
            print(content[:500] + "..." if len(content) > 500 else content)
            print("-" * 50)
    
    # Print summary
    print(f"\n{'=' * 50}")
    print("Test Summary")
    print(f"{'=' * 50}")
    
    for pdf_file, result in results.items():
        status = "PASSED" if result["success"] else "FAILED"
        print(f"{pdf_file}: {status} (Duration: {result['duration']:.2f} seconds)")
        print(f"  Output directory: {result['output_dir']}")
        print(f"  Content length: {result['content_length']} characters")
    
    # Check if all tests passed
    all_passed = all(result["success"] for result in results.values())
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
