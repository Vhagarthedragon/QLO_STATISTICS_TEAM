from src.embeddings import generar_embeddings
from src.ocr import extraer_texto_tesseract, extraer_texto_easyocr

if __name__ == "__main__":
    # Paso 1: Generar embeddings
    print("Generando embeddings...")
    generar_embeddings('data/datos.csv')
    
    # Paso 2: Extraer texto con Tesseract
    print("\nExtrayendo texto con Tesseract...")
    extraer_texto_tesseract('data/documento.png')
    
    # Paso 3: Extraer texto con EasyOCR
    print("\nExtrayendo texto con EasyOCR...")
    extraer_texto_easyocr('data/documento.png')
    
    print("\nProceso completado. Revisa la carpeta 'output' para ver los resultados.")