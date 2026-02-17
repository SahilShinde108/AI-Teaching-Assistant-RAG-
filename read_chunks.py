import requests

r = requests.post("http://localhost:11434/api/embeddings", json={
    "model": "bge-m3",
    "prompt": "Sahil is a good boy"
})

print(r.json())