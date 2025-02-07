import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def generar_embeddings(csv_path, columna_texto='texto', tamaño_fragmento=500):
    # Leer el CSV
    df = pd.read_csv(csv_path)
    
    # Dividir el texto en fragmentos
    df['fragmentos'] = df[columna_texto].apply(lambda x: [x[i:i+tamaño_fragmento] for i in range(0, len(x), tamaño_fragmento)])
    
    # Convertir fragmentos en embeddings
    modelo = SentenceTransformer('all-MiniLM-L6-v2')
    df['embeddings'] = df['fragmentos'].apply(lambda x: modelo.encode(x))
    
    # Crear índice FAISS
    dimension = 384
    indice = faiss.IndexFlatL2(dimension)
    embeddings = np.vstack(df['embeddings'].explode().values)
    indice.add(embeddings)
    
    # Guardar el índice
    faiss.write_index(indice, 'output/embeddings_index.faiss')
    print("Embeddings generados y almacenados en 'output/embeddings_index.faiss'.")