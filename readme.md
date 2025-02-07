
# Proyecto QLO - Statistics Team

Este proyecto tiene como objetivo realizar dos tareas principales:

1. **Generación de embeddings** a partir de datos estructurados en un archivo CSV.
2. **Extracción de texto no estructurado** desde imágenes utilizando técnicas de OCR (Reconocimiento Óptico de Caracteres) a través de Tesseract y EasyOCR.

## Estructura del Proyecto

- **data/**: Contiene los archivos de entrada, como archivos CSV para la generación de embeddings e imágenes para la extracción de texto.
- **src/**: Código fuente para la generación de embeddings y la extracción de texto.
  - **embeddings.py**: Funciones para generar embeddings a partir de datos CSV.
  - **ocr.py**: Funciones para extraer texto de imágenes usando Tesseract y EasyOCR.
- **output/**: Contiene los resultados generados por las tareas, como los embeddings generados y los textos extraídos de las imágenes.

## Requisitos

Asegúrate de tener instaladas las dependencias necesarias. Puedes instalarlas fácilmente ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

**Requisitos adicionales**:
- **Tesseract** debe estar instalado y configurado en tu máquina. Si no lo tienes instalado, puedes seguir [esta guía](https://github.com/tesseract-ocr/tesseract/wiki) para instalarlo.
- **EasyOCR** funciona con modelos preentrenados, por lo que no es necesario configuraciones adicionales.

## Descripción de la API

El proyecto proporciona una API RESTful construida con FastAPI, que permite realizar las siguientes operaciones:

### 1. **Generación de Embeddings**
Genera embeddings a partir de un archivo CSV cargado por el usuario.

**Endpoint**: `POST /generate_embeddings/`

**Parámetros**:
- **file**: Archivo CSV que contiene los datos estructurados.
- **text_column** (opcional): El nombre de la columna que contiene el texto para generar los embeddings (por defecto es "text").
- **chunk_size** (opcional): Tamaño del fragmento de texto en el que se dividirá el texto (por defecto es 500).
- **storage** (opcional): El tipo de base de datos para almacenar los embeddings. Puede ser `faiss`, `chromadb` o `pinecone` (por defecto es "faiss").

**Respuesta exitosa**:
```json
{
    "message": "Embeddings generated successfully."
}
```

**Respuesta de error**:
```json
{
    "error": "Error generating embeddings: [mensaje de error]"
}
```

### 2. **Extracción de Texto con Tesseract**
Extrae texto de una imagen utilizando el motor de OCR Tesseract.

**Endpoint**: `POST /extract_text_tesseract/`

**Parámetros**:
- **file**: Imagen de la cual se extraerá el texto.

**Respuesta exitosa**:
```json
{
    "message": "Text extracted with Tesseract and saved in 'output/extracted_text.json'."
}
```

**Respuesta de error**:
```json
{
    "error": "Error extracting text with Tesseract: [mensaje de error]"
}
```

### 3. **Extracción de Texto con EasyOCR**
Extrae texto de una imagen utilizando el motor de OCR EasyOCR.

**Endpoint**: `POST /extract_text_easyocr/`

**Parámetros**:
- **file**: Imagen de la cual se extraerá el texto.

**Respuesta exitosa**:
```json
{
    "message": "Text extracted with EasyOCR and saved in 'output/extracted_text_easyocr.json'."
}
```

**Respuesta de error**:
```json
{
    "error": "Error extracting text with EasyOCR: [mensaje de error]"
}
```

## Ejecución de la API

Para ejecutar la API localmente, sigue estos pasos:

1. Asegúrate de tener las dependencias instaladas, tal como se explicó en la sección de Requisitos.
2. Ejecuta el siguiente comando para iniciar el servidor de FastAPI:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000/`. Puedes interactuar con ella utilizando herramientas como Postman o Insomnia.

## Ejemplo de Uso

### 1. **Generación de Embeddings**

**POST** `http://127.0.0.1:8000/generate_embeddings/`

**Body**:
```json
{
    "file": "<Archivo CSV de entrada>",
    "text_column": "column_name",
    "chunk_size": 500,
    "storage": "faiss"
}
```

### 2. **Extracción de Texto con Tesseract**

**POST** `http://127.0.0.1:8000/extract_text_tesseract/`

**Body**:
```json
{
    "file": "<Imagen para extraer texto>"
}
```

### 3. **Extracción de Texto con EasyOCR**

**POST** `http://127.0.0.1:8000/extract_text_easyocr/`

**Body**:
```json
{
    "file": "<Imagen para extraer texto>"
}
```

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Forkea este repositorio.
2. Crea una rama para tu nueva característica (`git checkout -b feature-nueva-caracteristica`).
3. Realiza los cambios y realiza un commit (`git commit -am 'Añadir nueva característica'`).
4. Sube los cambios (`git push origin feature-nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Obra de daniel diaz. es solo una prueba tecnica 
