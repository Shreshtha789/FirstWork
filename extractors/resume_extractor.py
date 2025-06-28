import json
import re
from utils.ocr import ocr_from_file
from utils.llm_interface import query_gemini_with_retry

def clean_text(text):
    return re.sub(r'[^\x00-\x7F]+', ' ', text).strip()

def extract_resume_info(file_path: str, prompt_template_path: str) -> dict:
    raw_text = ocr_from_file(file_path)
    text = clean_text(raw_text)

    with open(prompt_template_path) as f:
        prompt = f.read().replace("{text}", text)

    output = query_gemini_with_retry(prompt)

    print("\n📄 Gemini Raw Output (Resume):\n", output)

    try:
        return json.loads(output)
    except Exception as e:
        return {
            "error": "Failed to extract resume info",
            "gemini_response": output,
            "exception": str(e)
        }
