from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os
import pandas as pd
from io import BytesIO
from src.embeddings import generate_embeddings  # Asegúrate de importar correctamente la función
from src.ocr import extract_text_tesseract, extract_text_easyocr

app = FastAPI()

# Pydantic model to hold the parameters for generating embeddings
class EmbeddingsParams(BaseModel):
    text_column: str = "text"
    chunk_size: int = 500
    storage: str = "faiss"

# Endpoint to generate embeddings from a CSV file
@app.post("/generate_embeddings/")
async def generate_embeddings_endpoint(
    file: UploadFile = File(...),  # File parameter to upload CSV
    params: EmbeddingsParams = EmbeddingsParams()  # Optional parameters for embeddings generation
):
    try:
        # Read the CSV file directly from memory
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))  # Convert the file content into a DataFrame

        # Call the generate_embeddings function with the DataFrame
        print(f"Generating embeddings from CSV file using {params.storage} storage...")
        generate_embeddings(
            df=df,  # Pass the DataFrame to the function
            text_column=params.text_column,
            chunk_size=params.chunk_size,
            storage=params.storage
        )

        return {"message": "Embeddings generated successfully."}
    except Exception as e:
        return {"error": f"Error generating embeddings: {str(e)}"}

# Endpoint to extract text from an image using Tesseract
@app.post("/extract_text_tesseract/")
async def extract_text_tesseract_endpoint(file: UploadFile = File(...)):
    try:
        # Save the uploaded image temporarily
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"Extracting text from {file.filename} using Tesseract...")

        # Extract text using Tesseract
        extract_text_tesseract(temp_path)

        # Remove the temporary file after processing
        os.remove(temp_path)

        return {"message": "Text extracted with Tesseract and saved in 'output/extracted_text.json'."}
    except Exception as e:
        return {"error": f"Error extracting text with Tesseract: {str(e)}"}

# Endpoint to extract text from an image using EasyOCR
@app.post("/extract_text_easyocr/")
async def extract_text_easyocr_endpoint(file: UploadFile = File(...)):
    try:
        # Save the uploaded image temporarily
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"Extracting text from {file.filename} using EasyOCR...")

        # Extract text using EasyOCR
        extract_text_easyocr(temp_path)

        # Remove the temporary file after processing
        os.remove(temp_path)

        return {"message": "Text extracted with EasyOCR and saved in 'output/extracted_text_easyocr.json'."}
    except Exception as e:
        return {"error": f"Error extracting text with EasyOCR: {str(e)}"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the OCR and Embedding API"}
