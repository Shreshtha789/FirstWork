import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load your API key from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if key is loaded
if not api_key:
    print("ERROR: Gemini API key not found in .env file!")
    exit()

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Send a test prompt
response = model.generate_content("Hello Gemini! Are you working?")
print("Gemini Response:")
print(response.text)