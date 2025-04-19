import os
import sys
import unittest
from pathlib import Path

# Add the parent directory to the path so we can import the src module
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.pdf_converter import convert_pdf_to_images_with_target_height


class TestPDFConverter(unittest.TestCase):
    def setUp(self):
        # Create test output directory
        self.test_output_dir = os.path.join(os.path.dirname(__file__), "test_output")
        os.makedirs(self.test_output_dir, exist_ok=True)
        
        # Path to a sample PDF for testing
        # Note: You'll need to add a sample PDF to the Test directory
        self.sample_pdf_path = os.path.join(os.path.dirname(__file__), "sample.pdf")
    
    def test_pdf_conversion(self):
        """Test that PDF conversion works if a sample PDF is available"""
        if not os.path.exists(self.sample_pdf_path):
            self.skipTest("Sample PDF not found. Add a PDF named 'sample.pdf' to the Test directory.")
        
        # Convert the PDF to images
        image_paths = convert_pdf_to_images_with_target_height(
            pdf_path=self.sample_pdf_path,
            out_dir=self.test_output_dir,
            dpi=150,  # Lower DPI for faster tests
            target_height_px=1024,  # Smaller height for faster tests
        )
        
        # Check that images were created
        self.assertTrue(len(image_paths) > 0, "No images were created")
        
        # Check that all image files exist
        for path in image_paths:
            self.assertTrue(os.path.exists(path), f"Image file {path} does not exist")
            self.assertTrue(path.endswith(".png"), f"Image file {path} is not a PNG")
    
    def test_invalid_pdf_path(self):
        """Test that an appropriate error is raised for invalid PDF paths"""
        with self.assertRaises(Exception):
            convert_pdf_to_images_with_target_height(
                pdf_path="nonexistent.pdf",
                out_dir=self.test_output_dir
            )
    
    def tearDown(self):
        # Clean up test output files if needed
        # Uncomment the following lines to clean up after tests
        # import shutil
        # if os.path.exists(self.test_output_dir):
        #     shutil.rmtree(self.test_output_dir)
        pass


if __name__ == "__main__":
    unittest.main()
