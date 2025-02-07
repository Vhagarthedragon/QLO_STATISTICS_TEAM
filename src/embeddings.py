from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import chromadb
from pinecone import Pinecone

def generate_embeddings(df, text_column='text', chunk_size=500, storage='faiss'):
    """
    Generate vector embeddings from a CSV DataFrame and store them in a specified vector database.
    
    Parameters:
    - df (pandas.DataFrame): DataFrame containing the data.
    - text_column (str): Column name containing text data.
    - chunk_size (int): Size of text chunks.
    - storage (str): Storage method ('faiss', 'chromadb', or 'pinecone').
    """
    # Split text into chunks
    df['chunks'] = df[text_column].apply(lambda x: [x[i:i+chunk_size] for i in range(0, len(x), chunk_size)])
    
    # Convert chunks into embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    df['embeddings'] = df['chunks'].apply(lambda x: model.encode(x))
    embeddings = np.vstack(df['embeddings'].explode().values)
    
    if storage == 'faiss':
        """ Store embeddings in FAISS index """
        dimension = 384
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        faiss.write_index(index, 'output/embeddings_index.faiss')
        print("Embeddings stored in FAISS.")
    
    elif storage == 'chromadb':
        """ Store embeddings in ChromaDB """
        client = chromadb.PersistentClient(path="output/chroma_db")
        collection = client.get_or_create_collection(name="embeddings")
        for i, emb in enumerate(embeddings):
            collection.add(ids=[str(i)], embeddings=[emb.tolist()])
        print("Embeddings stored in ChromaDB.")
    
    elif storage == 'pinecone':
        """ Store embeddings in Pinecone """
        pc = Pinecone(api_key="YOUR_API_KEY")
        index = pc.Index("embedding-index")
        index.upsert([(str(i), emb.tolist()) for i, emb in enumerate(embeddings)])
        print("Embeddings stored in Pinecone.")
    
    else:
        print("Unrecognized storage method.")
