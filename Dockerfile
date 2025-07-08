# از ایمیج رسمی پایتون 3.10 استفاده می‌کنیم
FROM python:3.10-slim

# دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل‌های پروژه به داخل کانتینر
COPY . /app

# نصب pip جدید
RUN python -m pip install --upgrade pip

# نصب کتابخانه‌ها از requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# تنظیم متغیر محیطی پایتون برای خروجی فوری
ENV PYTHONUNBUFFERED=1

# اجرای فایل اصلی ربات
CMD ["python", "main.py"]
