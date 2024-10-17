import os
from flask import Flask, render_template, request, jsonify
from langchain_huggingface import HuggingFaceEndpoint

app = Flask(__name__)

# Set Hugging Face API key directly in code
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "..."
huggingface_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')

if not huggingface_api_key:
    raise EnvironmentError("Hugging Face API key not found. Please set 'HUGGINGFACEHUB_API_TOKEN' in your environment.")

# Configure the Hugging Face model
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7,  # Adjust temperature for more creativity
    do_sample=True,  # Allow sampling for varied responses
)

def query_model(input_text):
    """Invoke the Hugging Face model with user input."""
    response = llm.invoke(input_text)
    return response.strip() if response else "I'm sorry, I couldn't generate a response."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('input')
    output = query_model(user_input)
    # Format the output to be more conversational
    formatted_output = f"Chatbot: {output}"
    return jsonify({'reply': formatted_output})

if __name__ == "__main__":
    app.run(debug=True)
