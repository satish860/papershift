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
    verbose: bool = False,
    max_workers: int = 4,
    batch_size: int = 5,
    quality: int = 95,
    fast_mode: bool = False
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
        max_workers: Maximum number of worker processes for PDF conversion
        batch_size: Number of pages to process in a single batch
        quality: Image quality (1-100) for JPEG compression in fast mode
        fast_mode: If True, uses reduced resolution and JPEG format for faster processing
        
    Returns:
        If combined_output=True: A single string containing all markdown content
        If combined_output=False: A list of strings, each containing markdown for one page
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    print(f"Starting PDF to markdown conversion for: {pdf_path}")
    print(f"Using model: {model}")
    
    if verbose:
        print(f"PDF path: {pdf_path}")
        print(f"DPI: {dpi}")
        print(f"Target height: {target_height_px}px")
        print(f"Aspect threshold: {aspect_threshold}")
        print(f"Parallel processing: {max_workers} workers, batch size: {batch_size}")
        if fast_mode:
            print(f"Fast mode: Enabled (quality: {quality}%)")
    
    print(f"Step 1/3: Converting PDF to base64 images...")
    
    # Convert PDF to base64 images
    result = convert_pdf_to_images_with_target_height(
        pdf_path=pdf_path,
        out_dir=None,  # We don't need to save the images
        dpi=dpi,
        target_height_px=target_height_px,
        aspect_threshold=aspect_threshold,
        return_base64=True,
        store_output=False,
        max_workers=max_workers,
        batch_size=batch_size,
        quality=quality,
        fast_mode=fast_mode
    )
    
    base64_images = result["base64_images"]
    page_order = result["order"]
    
    print(f"Step 1/3 completed: Successfully converted PDF to {len(base64_images)} base64 images")
    print(f"Step 2/3: Processing {len(page_order)} pages to markdown...")
    
    # Process each page to markdown
    markdown_pages = []
    
    for i, page_num in enumerate(page_order):
        # Find the corresponding base64 image
        page_data = next((img for img in base64_images if img["page"] == page_num), None)
        
        if not page_data:
            print(f"Warning: Page {page_num} not found in base64 images")
            continue
        
        print(f"  Processing page {page_num}/{len(page_order)} ({i+1}/{len(page_order)})...")
        
        # Create output file path if output_dir is provided
        output_file = None
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f"page_{page_num:03d}.md")
        
        # Process the page
        print(f"  Sending page {page_num} to model for processing...")
        markdown_content = process_page(
            base64_image=page_data["data"],
            prompt=prompt,
            model=model,
            api_key=api_key,
            site_url=site_url,
            app_name=app_name,
            output_file=output_file
        )
        print(f"  Page {page_num} processing complete")
        
        # Add page number as a header if there are multiple pages
        if len(page_order) > 1:
            markdown_content = f"## Page {page_num}\n\n{markdown_content}"
        
        markdown_pages.append(markdown_content)
        
        if output_file:
            print(f"  Saved markdown for page {page_num} to {output_file}")
    
    print(f"Step 2/3 completed: All {len(page_order)} pages processed")
    print(f"Step 3/3: Finalizing output...")
    
    # Create combined output if requested
    if combined_output:
        print(f"  Combining {len(markdown_pages)} markdown pages...")
        combined_markdown = "\n\n---\n\n".join(markdown_pages)
        
        # Save combined output if output_dir is provided
        if output_dir:
            combined_file = os.path.join(output_dir, "combined.md")
            with open(combined_file, 'w', encoding='utf-8') as f:
                f.write(combined_markdown)
            
            print(f"  Saved combined markdown to {combined_file}")
        
        print(f"Step 3/3 completed: Markdown conversion finished successfully")
        return combined_markdown
    else:
        print(f"Step 3/3 completed: Generated {len(markdown_pages)} separate markdown files")
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
    parser.add_argument(
        "--max-workers", type=int, default=4,
        help="Maximum number of worker processes for PDF conversion (default: 4)"
    )
    parser.add_argument(
        "--batch-size", type=int, default=5,
        help="Number of pages to process in a single batch (default: 5)"
    )
    parser.add_argument(
        "--quality", type=int, default=95,
        help="Image quality (1-100) for JPEG compression in fast mode (default: 95)"
    )
    parser.add_argument(
        "--fast-mode", action="store_true",
        help="If True, uses reduced resolution and JPEG format for faster processing"
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
            verbose=args.verbose,
            max_workers=args.max_workers,
            batch_size=args.batch_size,
            quality=args.quality,
            fast_mode=args.fast_mode
        )
        
        print(f"Successfully converted PDF to markdown")
        print(f"Markdown files saved to: {os.path.abspath(args.output_dir)}")
        
        return 0
    except Exception as e:
        print(f"Error converting PDF to markdown: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
