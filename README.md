<a href="">
  <img alt="\Rain Sim" src="https://github.com/afarhadi99/ASCII-Art-Generator/blob/main/screenshot.jpg">
</a>

# Image to ASCII Art Converter

This project is a web application that converts images to ASCII art. Users can upload an image, customize ASCII characters, adjust the density of the output, and download the resulting ASCII art. The application is built using Python and Gradio, providing an intuitive interface for image-to-ASCII conversion.

## Requirements

To run this project locally, you'll need:

- Python 3.9 or higher
- gradio==3.50.2
- Pillow==10.0.0

## Running Locally

To run this script locally on a Windows machine, follow these steps:
1. Clone the repository or download the source code.
2. Open a command prompt and navigate to the project directory.
3. Create a virtual environment (optional but recommended):
    python -m venv venv venv\Scripts\activate
4. Install the required packages:
    pip install -r requirements.txt
5. Run the application:
    python app.py
6. Open a web browser and go to `http://localhost:7860` to access the application.

## Deploying to HuggingFace for free

To deploy this application to HuggingFace Spaces using Docker, follow these steps:

1. Create a new Space on HuggingFace:
   - Go to https://huggingface.co/spaces
   - Click on "Create new Space"
   - Choose a name for your Space
   - Select "Docker" as the SDK
   - Choose the "Gradio" Space SDK

2. Set up your repository:
   - Initialize a git repository in your project folder (if not already done)
   - Add your files, commit changes, and push to a GitHub repository

3. Connect your GitHub repository to the HuggingFace Space:
   - In your Space's settings, go to the "Repository" section
   - Link your GitHub repository to the Space

4. Update your Space's hardware:
   - In your Space's settings, go to the "Hardware" section
   - Select an appropriate GPU or CPU option based on your needs

5. The deployment process will start automatically once you've linked your repository. HuggingFace will use the Dockerfile in your repository to build and deploy your application.

6. Once the deployment is complete, you can access your application through the URL provided by HuggingFace Spaces.

Your Image to ASCII Art Converter should now be live and accessible through HuggingFace Spaces!

## How to Use

1. Upload an image using the "Upload Image" section.
2. Customize the ASCII characters in the "ASCII Characters" textbox if desired. Characters should be entered from darkest to lightest.
3. Adjust the "ASCII Art Density" slider to control the detail level of the output.
4. Click the "Convert to ASCII" button to generate the ASCII art.
5. View the result in the "ASCII Art Output" section.
6. Use the "Download ASCII Art" button to save the result as a text file.

## Project Structure

- `app.py`: The main Python script containing the Gradio interface and ASCII art conversion logic.
- `requirements.txt`: List of Python packages required for the project.
- `Dockerfile`: Instructions for building the Docker container for deployment.
- `README.md`: This file, containing project information and instructions.

