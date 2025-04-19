"""
PDF to Markdown Converter

This module provides functionality to convert a PDF file to markdown format.
It uses the pdf_converter to convert PDF pages to base64 images and then
uses the page_parser to convert each page to markdown.
"""
import os
import sys
import argparse
from typing import List, Dict, Optional, Union
import json

from .pdf_converter import convert_pdf_to_images_with_target_height
from .page_parser import process_page


def convert_pdf_to_markdown(
    pdf_path: str,
    output_dir: Optional[str] = None,
    dpi: int = 300,
    target_height_px: int = 2048,
    aspect_threshold: float = 1.5,
    prompt: str = "Convert this document to markdown",
    model: str = "openrouter/google/gemini-2.0-flash-001",
    api_key: Optional[str] = None,
    site_url: Optional[str] = None,
    app_name: Optional[str] = None,
    combined_output: bool = True,
    verbose: bool = False
) -> Union[str, List[str]]:
    """
    Convert a PDF file to markdown format.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the output markdown files (if None, no files are saved)
        dpi: DPI for image rendering
        target_height_px: Target height in pixels
        aspect_threshold: Aspect ratio threshold for height adjustment
        prompt: Text prompt to send with each page image
        model: The model to use for processing
        api_key: OpenRouter API key (defaults to environment variable)
        site_url: Optional site URL for OpenRouter
        app_name: Optional app name for OpenRouter
        combined_output: If True, returns a single string with all pages combined
        verbose: If True, prints progress information
        
    Returns:
        If combined_output=True: A single string containing all markdown content
        If combined_output=False: A list of strings, each containing markdown for one page
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    if verbose:
        print(f"Converting PDF to base64 images: {pdf_path}")
    
    # Convert PDF to base64 images
    result = convert_pdf_to_images_with_target_height(
        pdf_path=pdf_path,
        out_dir=None,  # We don't need to save the images
        dpi=dpi,
        target_height_px=target_height_px,
        aspect_threshold=aspect_threshold,
        return_base64=True,
        store_output=False
    )
    
    base64_images = result["base64_images"]
    page_order = result["order"]
    
    if verbose:
        print(f"Successfully converted PDF to {len(base64_images)} base64 images")
        print("Processing each page to markdown...")
    
    # Process each page to markdown
    markdown_pages = []
    
    for i, page_num in enumerate(page_order):
        # Find the corresponding base64 image
        page_data = next((img for img in base64_images if img["page"] == page_num), None)
        
        if not page_data:
            if verbose:
                print(f"Warning: Page {page_num} not found in base64 images")
            continue
        
        if verbose:
            print(f"Processing page {page_num}/{len(page_order)}...")
        
        # Create output file path if output_dir is provided
        output_file = None
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f"page_{page_num:03d}.md")
        
        # Process the page
        markdown_content = process_page(
            base64_image=page_data["data"],
            prompt=prompt,
            model=model,
            api_key=api_key,
            site_url=site_url,
            app_name=app_name,
            output_file=output_file
        )
        
        # Add page number as a header if there are multiple pages
        if len(page_order) > 1:
            markdown_content = f"## Page {page_num}\n\n{markdown_content}"
        
        markdown_pages.append(markdown_content)
        
        if verbose and output_file:
            print(f"Saved markdown for page {page_num} to {output_file}")
    
    # Create combined output if requested
    if combined_output:
        combined_markdown = "\n\n---\n\n".join(markdown_pages)
        
        # Save combined output if output_dir is provided
        if output_dir:
            combined_file = os.path.join(output_dir, "combined.md")
            with open(combined_file, 'w', encoding='utf-8') as f:
                f.write(combined_markdown)
            
            if verbose:
                print(f"Saved combined markdown to {combined_file}")
        
        return combined_markdown
    else:
        return markdown_pages


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument(
        "--output-dir", "-o", 
        default="output_markdown", 
        help="Directory to save the output markdown files (default: output_markdown)"
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
        "--prompt", default="Convert this document to markdown",
        help="Text prompt to send with each page image"
    )
    parser.add_argument(
        "--model", default="openrouter/google/gemini-2.0-flash-001",
        help="The model to use for processing"
    )
    parser.add_argument(
        "--api-key",
        help="OpenRouter API key (defaults to environment variable)"
    )
    parser.add_argument(
        "--site-url",
        help="Optional site URL for OpenRouter"
    )
    parser.add_argument(
        "--app-name",
        help="Optional app name for OpenRouter"
    )
    parser.add_argument(
        "--separate-files", action="store_true",
        help="Save each page as a separate markdown file (combined.md will still be created)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print progress information"
    )
    
    args = parser.parse_args()
    
    try:
        convert_pdf_to_markdown(
            pdf_path=args.pdf_path,
            output_dir=args.output_dir,
            dpi=args.dpi,
            target_height_px=args.target_height,
            aspect_threshold=args.aspect_threshold,
            prompt=args.prompt,
            model=args.model,
            api_key=args.api_key,
            site_url=args.site_url,
            app_name=args.app_name,
            combined_output=True,  # Always create combined output
            verbose=args.verbose
        )
        
        print(f"Successfully converted PDF to markdown")
        print(f"Markdown files saved to: {os.path.abspath(args.output_dir)}")
        
        return 0
    except Exception as e:
        print(f"Error converting PDF to markdown: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
