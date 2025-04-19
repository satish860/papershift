# PDF Parser

A utility to convert PDF files to high-quality PNG images.

## Features

- Converts each page of a PDF to a PNG image
- Maintains high image quality with configurable DPI
- Intelligently scales tall pages to maintain readability
- Preserves aspect ratio
- Command-line interface for easy integration

## Installation

This project uses `uv` for dependency management. To install dependencies:

```bash
uv pip install -r requirements.txt
```

## Usage

```bash
python main.py path/to/your/file.pdf [options]
```

### Options

- `--output-dir`, `-o`: Directory to save output images (default: "output_images")
- `--dpi`: DPI for image rendering (default: 300)
- `--target-height`: Target height in pixels (default: 2048)
- `--aspect-threshold`: Aspect ratio threshold for height adjustment (default: 1.5)

### Example

```bash
python main.py document.pdf --output-dir my_images --dpi 400
```

## Project Structure

- `main.py`: Command-line interface
- `src/pdf_converter.py`: Core PDF to image conversion functionality
- `Test/`: Directory for test files and test scripts

## Dependencies

- PyMuPDF (fitz): PDF processing library