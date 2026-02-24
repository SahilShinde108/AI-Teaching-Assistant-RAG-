import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    
    embedding = r.json()["embeddings"]
    return embedding

df = joblib.load("embeddings.joblib")

incoming_query = input("Ask a question: ")
question_embedding = create_embeddings([incoming_query])[0]

# Find similarities of question_embedding with other embeddings
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
print(similarities)
top_results = 3
max_indx = similarities.argsort()[::-1][0:top_results]  # Indices of top 3 most similar chunks
print(max_indx)
new_df = df.loc[max_indx]
print(new_df[["title", "number", "text"]])