# Text Generation App using Flask and Hugging Face
This project is a simple web application built using Flask that utilizes the Hugging Face API to generate text responses. Users can enter input text and get a response from the Mistral-7B-Instruct-v0.3 model.

# File Descriptions
app.py: This is the main Flask application file that handles the backend logic, including API calls to the Hugging Face model and rendering the frontend.

templates/index.html: This HTML file contains the structure of the web page, including the chat interface for user interaction with the chatbot.

static/style.css: This CSS file is used for styling the HTML page, making the chatbot interface more visually appealing.

.env: This optional file can store environment variables, such as your Hugging Face API key. It helps keep sensitive information secure and out of your main codebase.

README.md: This file serves as documentation for your project, explaining how to set it up, run it, and any other relevant information.

# Requirements
Python 3.x
Flask
langchain-huggingface
Optionally: python-dotenv (for environment variables)
# How It Works
Enter your query in the text area on the homepage.
Click the "Send" button.
The app sends the input to the Hugging Face API.
The response is displayed in the UI.
# API Used
Model: Mistral-7B-Instruct-v0.3
Endpoint: Hugging Face Inference API
# Troubleshooting
API Key Error:
If you encounter the error "API key not found", make sure the environment variable is correctly set.

# Dependency Issues:
Ensure you have installed all the required packages by running:

# License
This project is open-source and available under the MIT License.
