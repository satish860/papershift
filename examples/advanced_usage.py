"""
Advanced example demonstrating how to use the papershift library
with performance optimizations and custom settings.
"""
import os
import time
from dotenv import load_dotenv
from papershift import convert_pdf_to_markdown

# Load environment variables from .env file (for API keys)
load_dotenv()

# Get API key from environment or set it directly
api_key = os.environ.get("OPENROUTER_API_KEY")

def main():
    # Path to your PDF file
    pdf_path = "path/to/your/document.pdf"
    
    # Output directory for markdown files
    output_dir = "markdown_output"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Converting PDF to markdown with advanced settings: {pdf_path}")
    
    start_time = time.time()
    
    # Convert PDF to markdown with performance optimizations
    markdown_content = convert_pdf_to_markdown(
        pdf_path=pdf_path,
        output_dir=output_dir,
        api_key=api_key,
        # Performance optimizations
        max_workers=8,           # Increase parallel processing
        batch_size=5,            # Control memory usage
        fast_mode=True,          # Use lower resolution and JPEG compression
        quality=85,              # Reduce quality for faster processing
        # Image rendering settings
        dpi=200,                 # Lower DPI for faster processing
        target_height_px=1536,   # Smaller target height for faster processing
        # Model settings
        model="openrouter/google/gemini-2.0-flash-001",  # Fast model
        prompt="Convert this document to clean markdown with proper formatting",
        # Output settings
        verbose=True,            # Show detailed progress
        combined_output=True     # Combine all pages into one markdown file
    )
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Save the combined markdown to a file
    output_file = os.path.join(output_dir, "combined_output.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Conversion complete in {elapsed_time:.2f} seconds!")
    print(f"Markdown saved to: {output_file}")

if __name__ == "__main__":
    main()
