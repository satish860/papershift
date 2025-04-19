"""
Run integration tests for multiple PDF files.

This script runs the integration test for multiple PDF files and stores the output.
"""
import os
import sys
import time
from pathlib import Path

# Add the parent directory to the path so we can import the src module
sys.path.insert(0, str(Path(__file__).parent.parent))
from Test.integration_test_pdf_to_markdown import run_integration_test

def main():
    # PDF files to test
    pdf_files = [
        "1-pages.pdf",
        "10-pages.pdf"
    ]
    
    # Base directory for test files
    test_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Results
    results = {}
    
    # Run tests for each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(test_dir, pdf_file)
        
        # Create output directory based on PDF filename
        output_dir = os.path.join(test_dir, "test_output", os.path.splitext(pdf_file)[0])
        
        print(f"\n{'=' * 50}")
        print(f"Testing: {pdf_file}")
        print(f"{'=' * 50}")
        
        # Record start time
        start_time = time.time()
        
        # Run the integration test
        success = run_integration_test(
            pdf_path=pdf_path,
            output_dir=output_dir,
            verbose=True
        )
        
        # Record end time
        end_time = time.time()
        duration = end_time - start_time
        
        # Store results
        results[pdf_file] = {
            "success": success,
            "duration": duration,
            "output_dir": output_dir
        }
    
    # Print summary
    print(f"\n{'=' * 50}")
    print("Test Summary")
    print(f"{'=' * 50}")
    
    for pdf_file, result in results.items():
        status = "PASSED" if result["success"] else "FAILED"
        print(f"{pdf_file}: {status} (Duration: {result['duration']:.2f} seconds)")
        print(f"  Output directory: {result['output_dir']}")
    
    # Check if all tests passed
    all_passed = all(result["success"] for result in results.values())
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
