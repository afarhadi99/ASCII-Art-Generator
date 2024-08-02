import gradio as gr
from PIL import Image
import tempfile
import os

DEFAULT_ASCII_CHARS = '@#S%?*+;:,. '

def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def to_grayscale(image):
    return image.convert('L')

def pixel_to_ascii(image, ascii_chars):
    pixels = list(image.getdata())
    return ''.join([ascii_chars[pixel * len(ascii_chars) // 256] for pixel in pixels])

def image_to_ascii(image, ascii_chars, new_width):
    image = resize_image(image, new_width)
    image = to_grayscale(image)
    ascii_str = pixel_to_ascii(image, ascii_chars)
    img_width = image.width
    return '\n'.join([ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width)])

def generate_ascii_art(input_image, ascii_chars, density):
    if input_image is None:
        return "Please upload an image.", None
    
    # Ensure the ASCII characters are in descending order of darkness
    ascii_chars = ''.join(sorted(set(ascii_chars), key=lambda c: -ord(c)))
    
    # Calculate new width based on density
    new_width = int(density)
    
    ascii_art = image_to_ascii(input_image, ascii_chars, new_width)
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_file.write(ascii_art)
    
    return ascii_art, temp_file.name

def process_and_download(input_image, ascii_chars, density):
    ascii_art, temp_file_path = generate_ascii_art(input_image, ascii_chars, density)
    return ascii_art, temp_file_path

custom_css = """
#ascii-output {
    font-family: monospace;
    white-space: pre;
    overflow-x: auto;
    font-size: 5px;
    line-height: 1;
}
"""

with gr.Blocks(css=custom_css) as iface:
    gr.Markdown("# Image to ASCII Art Converter")
    gr.Markdown("Upload an image, choose ASCII characters, set density, convert to ASCII art, and download the result!")
    
    with gr.Row():
        input_image = gr.Image(type="pil", label="Upload Image")
    
    with gr.Row():
        ascii_chars_input = gr.Textbox(
            label="ASCII Characters", 
            value=DEFAULT_ASCII_CHARS,
            info="Enter characters from darkest to lightest. The script will remove duplicates and sort them."
        )
    
    with gr.Row():
        density_slider = gr.Slider(
            minimum=50,
            maximum=600,
            value=200,
            step=10,
            label="ASCII Art Density",
            info="Higher values create denser, more detailed ASCII art."
        )
    
    with gr.Row():
        convert_button = gr.Button("Convert to ASCII")
    
    with gr.Row():
        ascii_output = gr.Textbox(label="ASCII Art Output", elem_id="ascii-output", lines=50)
    
    with gr.Row():
        download_button = gr.File(label="Download ASCII Art")
    
    convert_button.click(
        process_and_download,
        inputs=[input_image, ascii_chars_input, density_slider],
        outputs=[ascii_output, download_button]
    )

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)