"""
Simple example demonstrating how to use the papershift library.
"""
import os
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
    
    print(f"Converting PDF to markdown: {pdf_path}")
    
    # Convert PDF to markdown
    markdown_content = convert_pdf_to_markdown(
        pdf_path=pdf_path,
        output_dir=output_dir,
        api_key=api_key,
        verbose=True,
        # Optional parameters for customization
        # dpi=300,
        # target_height_px=2048,
        # model="openrouter/google/gemini-2.0-flash-001",
        # max_workers=4,
        # batch_size=5,
        # fast_mode=True
    )
    
    # Save the combined markdown to a file
    output_file = "output.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Conversion complete! Markdown saved to: {output_file}")

if __name__ == "__main__":
    main()
