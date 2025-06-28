# FirstWork Assignment – Document Extraction Project

This is a Python project built for the FirstWork internship assignment. It extracts structured data from documents using **Google Gemini API** and **EasyOCR**.

It supports:
- Driving Licenses
- Shop Receipts
- Resumes (image format only)

---

## ✅ What This Project Does

- Takes input image files like `.jpg` or `.png`
- Uses OCR to read the text from the document
- Sends the extracted text to Gemini for processing
- Extracts required fields and returns them as JSON
- Saves the result in the outputs folder

---

## 🧱 Folder Structure

FirstWork/
├── main.py # Entry point for the project
├── extractors/ # Extraction logic for each doc type
├── prompts/ # Prompts for Gemini API
├── utils/ # OCR + Gemini helper code
├── datasets/ # Put your input files here
│ ├── drivers_license/
│ ├── shop_receipts/
│ └── resumes/
├── outputs/ # Output JSONs get saved here
├── .env.example # Template for Gemini API key
├── requirements.txt # Python dependencies
└── README.md # This file

---

## ⚙️ Setup Instructions (Mac and Windows)

### 1. Install Python and PyCharm

- Download Python: https://www.python.org/downloads/  
  ✅ Tick “Add Python to PATH” while installing (for Windows)
- Download PyCharm: https://www.jetbrains.com/pycharm/download/

---

### 2. Create Virtual Environment (optional)

```bash
python -m venv venv
Activate it:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3. Install Required Libraries
pip install -r requirements.txt
This will install:

easyocr

google-generativeai

python-dotenv

torch

scikit-image

imageio

4. Setup Gemini API Key
Go to: https://aistudio.google.com/app/apikey

Copy your API key

Create a file named .env in the project root with:

GEMINI_API_KEY=your-api-key-here
✅ Do not share your .env file publicly.

▶️ How to Run the Project
Use this command to process a file:

python main.py --type license --file your_image.jpg
python main.py --type receipt --file your_receipt.png
python main.py --type resume --file your_resume.jpg
Make sure your file is placed in the correct subfolder under datasets/.

📂 Output Location
The output will be saved as a JSON file inside:

outputs/license_output/

outputs/receipt_output/

outputs/resume_output/

File name will match the input image name.