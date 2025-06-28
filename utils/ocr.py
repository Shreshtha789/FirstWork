import easyocr
from pdf2image import convert_from_path
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)

def ocr_from_file(file_path):
    if file_path.lower().endswith(".pdf"):
        images = convert_from_path(file_path)
        text = ""
        for img in images:
            result = reader.readtext(img, detail=0, paragraph=True)
            text += "\n".join(result)
        return text
    else:
        result = reader.readtext(file_path, detail=0, paragraph=True)
        return "\n".join(result)
