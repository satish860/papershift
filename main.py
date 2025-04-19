import argparse
import os
import sys
import json
import time
from dotenv import load_dotenv
from src.pdf_to_markdown import convert_pdf_to_markdown


def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get OpenRouter API key from environment
    openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")
    
    parser = argparse.ArgumentParser(description="Convert PDF to markdown")
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
        "--api-key", default=openrouter_api_key,
        help="OpenRouter API key (defaults to OPENROUTER_API_KEY from .env file or environment)"
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
        "--output-file", 
        help="Path to save the markdown output (if not specified, prints to stdout)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print progress information"
    )
    parser.add_argument(
        "--max-workers", type=int, default=4,
        help="Maximum number of worker processes for parallel processing (default: 4)"
    )
    parser.add_argument(
        "--batch-size", type=int, default=5,
        help="Number of pages to process in a single batch to limit memory usage (default: 5)"
    )
    parser.add_argument(
        "--quality", type=int, default=95,
        help="Image quality (1-100) for JPEG compression in fast mode (default: 95)"
    )
    parser.add_argument(
        "--fast", action="store_true",
        help="Enable fast mode with reduced resolution and JPEG compression for faster processing"
    )
    parser.add_argument(
        "--show-env", action="store_true",
        help="Show environment variables and exit"
    )
    parser.add_argument(
        "--env-file", default=".env",
        help="Path to .env file (default: .env in current directory)"
    )
    
    args = parser.parse_args()
    
    # Load from specific .env file if provided
    if args.env_file and args.env_file != ".env":
        if os.path.exists(args.env_file):
            load_dotenv(args.env_file)
            # Reload the API key in case it was updated
            openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")
            if not args.api_key:
                args.api_key = openrouter_api_key
            print(f"Loaded environment from: {args.env_file}")
        else:
            print(f"Warning: Environment file not found: {args.env_file}")
    
    # Display environment variables if requested
    if args.show_env:
        print("\n=== Environment Variables ===")
        env_file = args.env_file if os.path.exists(args.env_file) else ".env (default)"
        print(f"Environment file: {env_file}")
        
        if openrouter_api_key:
            masked_key = openrouter_api_key[:4] + "*" * (len(openrouter_api_key) - 8) + openrouter_api_key[-4:] if len(openrouter_api_key) > 8 else "****"
            print(f"OPENROUTER_API_KEY: {masked_key}")
        else:
            print("OPENROUTER_API_KEY: Not set")
        return 0
    
    print(f"\n=== PDF to Markdown Converter ===")
    print(f"Processing file: {args.pdf_path}")
    
    # Validate PDF path
    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF file '{args.pdf_path}' not found", file=sys.stderr)
        return 1
    
    print(f"Output directory: {os.path.abspath(args.output_dir)}")
    if args.output_file:
        print(f"Output file: {os.path.abspath(args.output_file)}")
    
    print(f"Parallel processing: {args.max_workers} workers, batch size: {args.batch_size}")
    if args.fast:
        print(f"Fast mode enabled: Using reduced resolution and JPEG compression (quality: {args.quality}%)")
    print(f"Using model: {args.model}")
    
    if args.api_key:
        print("OpenRouter API key: Provided ")
    else:
        print("OpenRouter API key: Not provided ")
        print("Warning: You need to set the OPENROUTER_API_KEY in your .env file or provide it with --api-key")
        return 1
    
    start_time = time.time()
    print(f"Starting conversion process at {time.strftime('%H:%M:%S')}")
    print(f"This may take several minutes depending on the PDF size and complexity...")
    
    try:
        # Convert PDF to markdown
        print(f"\nInitiating PDF to markdown conversion...")
        markdown_content = convert_pdf_to_markdown(
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
            combined_output=True,
            verbose=args.verbose,
            max_workers=args.max_workers,
            batch_size=args.batch_size,
            quality=args.quality,
            fast_mode=args.fast
        )
        
        # Handle output
        print(f"\nConversion completed successfully!")
        
        if args.output_file:
            print(f"Saving markdown to output file...")
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"Markdown output saved to: {os.path.abspath(args.output_file)}")
        else:
            print(f"\n--- Markdown Output ---\n")
            # Print markdown to stdout
            print(markdown_content)
            print(f"\n--- End of Markdown Output ---")
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        
        print(f"\nTotal conversion time: {int(minutes)} minutes and {int(seconds)} seconds")
        print(f"Markdown files saved to: {os.path.abspath(args.output_dir)}")
        print(f"=== Conversion Complete ===\n")
        
        return 0
    except KeyboardInterrupt:
        print(f"\nConversion process interrupted by user", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"\nError converting PDF: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
