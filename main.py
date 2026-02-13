from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import pipeline
import shutil
import os

app = FastAPI()

# --- تحميل الموديلات الذكية ---
print("Loading AI Models... Please wait.")
# 1. موديل تحويل الصوت لنص (Speech to Text)
asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

# 2. موديل التلخيص (Summarization)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 3. موديل الترجمة (Translation)
translator = pipeline("translation_en_to_ar", model="Helsinki-NLP/opus-mt-en-ar")

# --- نموذج البيانات للترجمة ---
class TranslationRequest(BaseModel):
    text: str

# --- الصفحة الرئيسية ---
@app.get("/")
def read_index():
    return FileResponse("index.html")

# --- دالة مساعدة لتنسيق النقاط (Bullet Points) ---
def format_as_bullets(text):
    sentences = text.split('. ')
    bullet_points = ""
    for sentence in sentences:
        if sentence.strip():
            bullet_points += f"• {sentence.strip()}.\n"
    return bullet_points

# --- 1. زرار معالجة الصوت (تسجيل أو رفع ملف) ---
@app.post("/process-audio")
async def process_audio(file: UploadFile = File(...)):
    # حفظ الملف مؤقتاً
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # أ: تحويل الصوت لنص
        print("Transcribing audio...")
        transcription = asr_pipeline(temp_filename)["text"]

        # ب: تلخيص النص
        print("Summarizing text...")
        # (نلخص بحد أقصى 150 كلمة عشان السرعة)
        summary_result = summarizer(transcription, max_length=150, min_length=40, do_sample=False)
        raw_summary = summary_result[0]['summary_text']
        
        # ج: تحويل التلخيص لنقاط
        formatted_summary = format_as_bullets(raw_summary)

        # التخزين في Dictionary والرد
        return {"message": formatted_summary, "original_text": transcription}

    except Exception as e:
        return {"message": f"Error: {str(e)}"}
    
    finally:
        # تنظيف السيرفر
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

# --- 2. زرار الترجمة المنفصل ---
@app.post("/translate")
async def translate_text(request: TranslationRequest):
    try:
        # ترجمة النص اللي جاي من الفرونت إند
        translated = translator(request.text)
        return {"translated_message": translated[0]['translation_text']}
    except Exception as e:
        return {"translated_message": "فشل في الترجمة"}
