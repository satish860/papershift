"""
Generate test images for image_to_markdown tests
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image(output_path, text="Test Image", size=(800, 600), color="white", text_color="black"):
    """Create a test image with text"""
    # Create a new image with the given size and color
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, or fall back to default
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (200, 36)
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    # Draw the text
    draw.text(position, text, fill=text_color, font=font)
    
    # Save the image
    img.save(output_path)
    print(f"Created test image: {output_path}")
    return output_path

if __name__ == "__main__":
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    
    # Create a simple test image
    create_test_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "simple.png"))
    
    # Create a test image with a table
    table_text = "Test Image with Table"
    create_test_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "table.png"), 
                     text=table_text, size=(1000, 800))
    
    # Create a test image with a chart
    chart_text = "Test Image with Chart"
    create_test_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chart.png"), 
                     text=chart_text, size=(1000, 800), color="lightblue")
