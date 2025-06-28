import argparse
import os
import json
from extractors.license_extractor import extract_license_info
from extractors.receipt_extractor import extract_receipt_info
from extractors.resume_extractor import extract_resume_info

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def run_for_type(doc_type: str, filename: str):
    name_only = os.path.splitext(filename)[0]

    if doc_type == "license":
        input_path = f"datasets/drivers_license/{filename}"
        output_path = f"outputs/license_output/{name_only}.json"
        prompt_path = "prompts/driving_license_prompt.txt"
        result = extract_license_info(input_path, prompt_path)

    elif doc_type == "receipt":
        input_path = f"datasets/shop_receipts/{filename}"
        output_path = f"outputs/receipt_output/{name_only}.json"
        prompt_path = "prompts/shop_receipt_prompt.txt"
        result = extract_receipt_info(input_path, prompt_path)

    elif doc_type == "resume":
        input_path = f"datasets/resume/{filename}"
        output_path = f"outputs/resume_output/{name_only}.json"
        prompt_path = "prompts/resume_prompt.txt"
        result = extract_resume_info(input_path, prompt_path)

    else:
        print(f"Unsupported document type: {doc_type}")
        return

    save_json(result, output_path)
    print(f"\n Output saved to {output_path}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a specific document with Gemini and OCR.")
    parser.add_argument("--type", required=True, help="Type of document: license, receipt, or resume")
    parser.add_argument("--file", required=True, help="File name (e.g., generated_license_0.png)")

    args = parser.parse_args()
    run_for_type(args.type, args.file)