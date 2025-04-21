"""
Run a sample conversion of test images to markdown.

This script demonstrates the image_to_markdown functionality by converting
sample test images to markdown and saving the output to the test_output directory.
"""
import os
import sys
import argparse

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.image_to_markdown import convert_image_to_markdown, convert_images_to_markdown


def main():
    """Run the sample image to markdown conversion."""
    parser = argparse.ArgumentParser(description='Convert sample images to markdown')
    parser.add_argument('--api-key', help='OpenRouter API key')
    parser.add_argument('--single', action='store_true', help='Convert only a single image')
    parser.add_argument('--separate', action='store_true', help='Generate separate markdown files')
    parser.add_argument('--fast', action='store_true', help='Use fast mode with reduced quality')
    args = parser.parse_args()
    
    # Set up paths
    test_images_dir = os.path.join(os.path.dirname(__file__), 'data', 'images')
    simple_image = os.path.join(test_images_dir, 'simple.png')
    table_image = os.path.join(test_images_dir, 'table.png')
    chart_image = os.path.join(test_images_dir, 'chart.png')
    
    # Set up output directory
    output_dir = os.path.join(os.path.dirname(__file__), 'test_output', 'image_to_markdown')
    os.makedirs(output_dir, exist_ok=True)
    
    # Get API key from environment or command line
    api_key = args.api_key or os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print("ERROR: OpenRouter API key not provided.")
        print("Please provide an API key using the --api-key option or set the OPENROUTER_API_KEY environment variable.")
        return False
    
    # Run the conversion
    if args.single:
        print(f"Converting single image: {simple_image}")
        result = convert_image_to_markdown(
            image_path=simple_image,
            output_dir=output_dir,
            api_key=api_key,
            verbose=True,
            fast_mode=args.fast
        )
        print(f"Markdown saved to: {os.path.join(output_dir, 'simple.md')}")
    else:
        print(f"Converting multiple images: {simple_image}, {table_image}, {chart_image}")
        result = convert_images_to_markdown(
            image_paths=[simple_image, table_image, chart_image],
            output_dir=output_dir,
            api_key=api_key,
            combined_output=not args.separate,
            verbose=True,
            fast_mode=args.fast
        )
        
        if args.separate:
            print(f"Markdown files saved to:")
            print(f"  {os.path.join(output_dir, 'simple.md')}")
            print(f"  {os.path.join(output_dir, 'table.md')}")
            print(f"  {os.path.join(output_dir, 'chart.md')}")
        else:
            print(f"Combined markdown saved to: {os.path.join(output_dir, 'combined.md')}")
    
    print("Conversion completed successfully.")
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
