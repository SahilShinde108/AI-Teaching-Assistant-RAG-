# 🎓 AI Teaching Assistant (RAG-Based)

An intelligent, Retrieval-Augmented Generation (RAG) powered teaching assistant that can answer questions based on your own video course content. It transcribes video lectures, indexes them into a vector database, and uses an LLM to provide context-aware answers with specific timestamps.

---

## 🚀 Features

- **Video Transcription**: Automatically converts video content to text using OpenAI's Whisper.
- **Context-Aware Q&A**: Employs RAG to provide accurate answers based *only* on the provided course material.
- **Timestamp References**: Points users to the exact video and time where a concept is taught.
- **Local LLM Integration**: Uses Ollama to run models like `llama3.2` or `deepseek-r1` locally for privacy and performance.
- **Efficient Retrieval**: Uses `bge-m3` embeddings for high-quality semantic search.

---

## 🛠️ Tech Stack

- **Large Language Models**: [Ollama](https://ollama.com/) (`llama3.2`, `bge-m3`)
- **Transcription**: [OpenAI Whisper](https://github.com/openai/whisper)
- **Vector Search**: [Scikit-learn](https://scikit-learn.org/) (Cosine Similarity)
- **Data Engineering**: `Pandas`, `Numpy`, `Joblib`
- **Media Processing**: `FFmpeg`
- **Language**: Python 3.x

---

## 📋 System Architecture

1.  **Ingestion**: Videos are converted to MP3.
2.  **Transcription**: Whisper converts MP3 to JSON with timestamps.
3.  **Indexing**: JSON chunks are embedded using `bge-m3` and stored in a `joblib` vector store.
4.  **Retrieval**: User queries are embedded and matched against the vector store.
5.  **Generation**: The LLM generates a human-like response using the retrieved context.

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- **Python 3.8+**
- **FFmpeg**: Installed and added to your system PATH.
- **Ollama**: Download and install from [ollama.com](https://ollama.com/).
- **Required Models**:
  ```bash
  ollama pull llama3.2
  ollama pull bge-m3
  ```

### 2. Install Dependencies
```bash
pip install whisper pandas numpy scikit-learn requests joblib
```

### 3. Project Structure
Create the following directories if they don't exist:
- `videos/`: Place your raw video files here.
- `audios/`: For extracted mp3 files.
- `jsons/`: For transcriptions.

---

## 📖 Usage Guide

Follow these steps in order to process your data:

### Step 1: Extract Audio
Run the script to convert your videos to mp3:
```bash
python video_to_mp3.py
```

### Step 2: Transcribe Content
Generate JSON transcripts with timestamps:
```bash
python mp3_to_json.py
```

### Step 3: Create Vector Index
Generate embeddings and save them to `embeddings.joblib`:
```bash
python preprocess_json.py
```

### Step 4: Ask Questions
Run the assistant to query your course content:
```bash
python process_incoming.py
```