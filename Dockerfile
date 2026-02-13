# استخدم نسخة بايثون رسمية
FROM python:3.9

# حدد مكان الشغل جوه السيرفر
WORKDIR /code

# انسخ ملفات المكتبات أولاً
COPY ./requirements.txt /code/requirements.txt

# ثبت المكتبات
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# انسخ باقي كود المشروع (الـ HTML والبايثون)
COPY . .

# شغل السيرفر (FastAPI) على بورت 7860 (الخاص بـ Hugging Face)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
