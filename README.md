# 🎙️ AI Meeting Lead (Action-Items Extractor)

A sophisticated **Full-Stack AI Application** that transforms voice recordings and audio files into organized, actionable task lists. No more manual note-taking—let the AI handle your meeting minutes.

## 🚀 Live Demo
Experience the tool here: [Your-HuggingFace-Link-Here]

## ✨ Core Features
* **Live Voice Recording**: Record your meetings directly from the browser using the MediaRecorder API.
* **Audio File Processing**: Upload existing MP3/WAV files for instant analysis.
* **Speech-to-Text (ASR)**: Powered by OpenAI's `Whisper-Tiny` for high-accuracy transcription.
* **Action-Item Extraction**: Uses the `BART` model to distill long conversations into concise **Bullet Points**.
* **On-Demand Translation**: Integrated English-to-Arabic translation for the extracted tasks.

## 🛠️ Technical Architecture
The project follows a modern asynchronous flow:
1.  **Frontend**: JavaScript captures audio as a `Blob` and transmits it via `Multipart/form-data`.
2.  **API Layer**: FastAPI handles the file stream and manages temporary storage.
3.  **AI Engine**: 
    - `Whisper` converts audio waves to raw text.
    - `BART-Large-CNN` filters the text to extract specific tasks.
    - `Helsinki-NLP` provides the final translation layer.
4.  **Deployment**: Containerized using **Docker** with `ffmpeg` integration for audio decoding.

## 📦 Project Structure
* `main.py`: The FastAPI backend logic and AI pipelines.
* `index.html`: Modern violet-themed UI with recording capabilities.
* `Dockerfile`: Custom container configuration for Hugging Face Spaces.
* `packages.txt`: System-level dependencies (ffmpeg).
* `requirements.txt`: Python library dependencies.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install FFmpeg on your system.
3. Install dependencies: `pip install -r requirements.txt`.
4. Launch the app: `uvicorn main:app --reload`.

---
Built with 🧠 and 🎙️ by [PhilopateerDev](https://github.com/PhilopateerDev)
