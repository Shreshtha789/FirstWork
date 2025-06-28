import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def query_gemini_with_retry(prompt: str, retries: int = 2):
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            text = response.text.strip()

            # Remove markdown code block wrapper
            if text.startswith("```"):
                text = text.replace("```json", "").replace("```", "").strip()

            print(f"\n🔍 Cleaned Gemini Output (Attempt {attempt+1}):\n{text}\n")

            # Try parsing cleaned text
            json.loads(text)
            return text

        except Exception as e:
            print(f"[Retry {attempt + 1}] Gemini Error:", e)
            prompt = f"Your last output was invalid JSON. Please correct and return JSON only.\n\n{prompt}"

    return None
