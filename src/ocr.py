from PIL import Image
import pytesseract
import json
import easyocr

def extraer_texto_tesseract(imagen_path):
    # Cargar la imagen
    imagen = Image.open(imagen_path)
    
    # Extraer texto con Tesseract
    texto = pytesseract.image_to_string(imagen)
    
    # Guardar en formato JSON
    salida = {"texto_extraido": texto}
    with open('output/texto_extraido.json', 'w', encoding='utf-8') as f:
        json.dump(salida, f, indent=4, ensure_ascii=False)
    
    print(f"Texto extraído con Tesseract y guardado en 'output/texto_extraido.json'.")

def extraer_texto_easyocr(imagen_path):
    # Inicializar EasyOCR
    lector = easyocr.Reader(['es'])
    
    # Extraer texto
    resultado = lector.readtext(imagen_path)
    texto = " ".join([res[1] for res in resultado])
    
    # Guardar en formato JSON
    salida = {"texto_extraido": texto}
    with open('output/texto_extraido_easyocr.json', 'w', encoding='utf-8') as f:
        json.dump(salida, f, indent=4, ensure_ascii=False)
    
    print(f"Texto extraído con EasyOCR y guardado en 'output/texto_extraido_easyocr.json'.")