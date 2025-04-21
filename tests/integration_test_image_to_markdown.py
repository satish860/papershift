"""
Integration tests for the image_to_markdown module.

These tests verify that the image_to_markdown module works correctly
with actual images and the AI model.

Note: These tests require an OpenRouter API key to be set in the environment.
"""
import os
import sys
import unittest
import tempfile
import shutil
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.image_to_markdown import convert_image_to_markdown, convert_images_to_markdown


class TestImageToMarkdownIntegration(unittest.TestCase):
    """Integration tests for the image_to_markdown module."""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that are used for all tests."""
        # Check if OpenRouter API key is set
        cls.api_key = os.environ.get('OPENROUTER_API_KEY')
        if not cls.api_key:
            print("WARNING: OPENROUTER_API_KEY environment variable not set. Tests will be skipped.")
        
        # Set up paths to test images
        cls.test_images_dir = os.path.join(os.path.dirname(__file__), 'data', 'images')
        cls.simple_image = os.path.join(cls.test_images_dir, 'simple.png')
        cls.table_image = os.path.join(cls.test_images_dir, 'table.png')
        cls.chart_image = os.path.join(cls.test_images_dir, 'chart.png')
        
        # Create a test output directory
        cls.test_output_dir = os.path.join(os.path.dirname(__file__), 'test_output', 'image_to_markdown')
        os.makedirs(cls.test_output_dir, exist_ok=True)

    def setUp(self):
        """Set up test fixtures for each test."""
        # Create a temporary directory for each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = self.temp_dir.name

    def tearDown(self):
        """Tear down test fixtures for each test."""
        self.temp_dir.cleanup()

    def test_convert_single_image(self):
        """Test converting a single image to markdown."""
        # Skip if no API key
        if not self.api_key:
            self.skipTest("OPENROUTER_API_KEY not set")
        
        # Convert the image to markdown
        result = convert_image_to_markdown(
            image_path=self.simple_image,
            output_dir=self.output_dir,
            api_key=self.api_key,
            verbose=True
        )
        
        # Check the result
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        
        # Check that the output file was created
        output_file = os.path.join(self.output_dir, 'simple.md')
        self.assertTrue(os.path.exists(output_file))
        
        # Check the content of the output file
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertEqual(content, result)
        
        # Save a copy to the test_output directory for manual inspection
        shutil.copy(output_file, os.path.join(self.test_output_dir, 'simple.md'))

    def test_convert_multiple_images_combined(self):
        """Test converting multiple images to a combined markdown file."""
        # Skip if no API key
        if not self.api_key:
            self.skipTest("OPENROUTER_API_KEY not set")
        
        # Convert the images to markdown
        result = convert_images_to_markdown(
            image_paths=[self.simple_image, self.table_image, self.chart_image],
            output_dir=self.output_dir,
            api_key=self.api_key,
            combined_output=True,
            verbose=True
        )
        
        # Check the result
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        
        # Check that the combined output file was created
        combined_file = os.path.join(self.output_dir, 'combined.md')
        self.assertTrue(os.path.exists(combined_file))
        
        # Check the content of the output file
        with open(combined_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertEqual(content, result)
        
        # Save a copy to the test_output directory for manual inspection
        shutil.copy(combined_file, os.path.join(self.test_output_dir, 'combined.md'))

    def test_convert_multiple_images_separate(self):
        """Test converting multiple images to separate markdown files."""
        # Skip if no API key
        if not self.api_key:
            self.skipTest("OPENROUTER_API_KEY not set")
        
        # Convert the images to markdown
        result = convert_images_to_markdown(
            image_paths=[self.simple_image, self.table_image],
            output_dir=self.output_dir,
            api_key=self.api_key,
            combined_output=False,
            verbose=True
        )
        
        # Check the result
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        
        # Check that the separate output files were created
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'simple.md')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'table.md')))
        
        # Save copies to the test_output directory for manual inspection
        for filename in ['simple.md', 'table.md']:
            shutil.copy(
                os.path.join(self.output_dir, filename),
                os.path.join(self.test_output_dir, filename)
            )

    def test_fast_mode(self):
        """Test converting an image with fast mode enabled."""
        # Skip if no API key
        if not self.api_key:
            self.skipTest("OPENROUTER_API_KEY not set")
        
        # Convert the image to markdown with fast mode
        result = convert_image_to_markdown(
            image_path=self.simple_image,
            output_dir=self.output_dir,
            api_key=self.api_key,
            fast_mode=True,
            quality=80,
            verbose=True
        )
        
        # Check the result
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        
        # Save a copy to the test_output directory for manual inspection
        output_file = os.path.join(self.output_dir, 'simple.md')
        shutil.copy(output_file, os.path.join(self.test_output_dir, 'simple_fast_mode.md'))


if __name__ == '__main__':
    unittest.main()
