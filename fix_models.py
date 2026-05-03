import os
import subprocess

# 1. الإعدادات الأساسية
token = os.getenv("HF_TOKEN")
repo_id = "shababdd11/sultan-models"
file_url = "https://huggingface.co/public-data/replicate-models/resolve/main/GFPGANv1.4.pth"
local_file = "GFPGANv1.4.pth"

print(f"--- بدء المعالجة النهائية لملف {local_file} ---")

try:
    # 2. تحميل الملف إلى سيرفر GitHub أولاً (باستخدام wget لضمان القوة)
    print("جاري تحميل الملف من المصدر...")
    subprocess.run(["wget", "-O", local_file, file_url], check=True)
    
    # التأكد من حجم الملف المحمل
    size = os.path.getsize(local_file) / (1024 * 1024)
    print(f"✅ تم التحميل. الحجم الفعلي: {size:.2f} MB")

    # 3. الرفع القسري باستخدام أمر huggingface-cli
    # هذا الأمر هو الأضمن لتجاوز مشكلة الـ 0 بايت
    print("جاري الرفع القسري إلى Hugging Face...")
    upload_cmd = [
        "huggingface-cli", "upload",
        repo_id,
        local_file,
        f"gfpgan/{local_file}",
        "--token", token
    ]
    subprocess.run(upload_cmd, check=True)
    print("--- ✅ تمت العملية بنجاح! تحقق من المستودع الآن ---")

except Exception as e:
    print(f"❌ حدث خطأ تقني: {e}")
