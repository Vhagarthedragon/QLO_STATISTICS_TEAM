from PIL import Image
import pytesseract
import json
import easyocr
from io import BytesIO

def extract_text_tesseract(file):
    """
    Extract text from an image using Tesseract OCR and save it in a JSON file.
    
    Parameters:
    - file (BytesIO): The uploaded image as in-memory file.
    """
    try:
        # Usar directamente el objeto BytesIO con Image.open()
        image = Image.open(file)  # Abre la imagen desde el objeto BytesIO
        text = pytesseract.image_to_string(image)

        output = {"extracted_text": text}
        with open('output/extracted_text.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=4, ensure_ascii=False)

        print(f"Text extracted using Tesseract and saved in 'output/extracted_text.json'.")
    except Exception as e:
        print(f"Error extracting text with Tesseract: {e}")


def extract_text_easyocr(file):
    """
    Extract text from an image using EasyOCR and save it in a JSON file.
    
    Parameters:
    - file (BytesIO): The uploaded image as in-memory file.
    """
    try:
        reader = easyocr.Reader(['es'])
        image = Image.open(file)  # Usamos el objeto BytesIO directamente
        result = reader.readtext(image)
        text = " ".join([res[1] for res in result])

        output = {"extracted_text": text}
        with open('output/extracted_text_easyocr.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=4, ensure_ascii=False)

        print(f"Text extracted using EasyOCR and saved in 'output/extracted_text_easyocr.json'.")
    except Exception as e:
        print(f"Error extracting text with EasyOCR: {e}")
