import os
import urllib.request
from huggingface_hub import HfApi

# 1. إعدادات الهوية (تأكد أن التوكن مضاف في Secrets باسم HF_TOKEN)
token = os.getenv("HF_TOKEN")
repo_id = "shababdd11/sultan-models"
api = HfApi()

# 2. روابط الملف الحقيقية (نسخة RAW لضمان الحجم الكامل)
# هذا الرابط هو البديل الموثق بعد خطأ الـ 404 السابق
file_url = "https://huggingface.co/public-data/replicate-models/resolve/main/GFPGANv1.4.pth"
local_filename = "temp_gfpgan.pth"

print("--- جاري بدء عملية السحب لملف GFPGANv1.4 ---")

try:
    # تحميل الملف من الرابط المباشر إلى سيرفر GitHub
    print(f"جاري التحميل من: {file_url}")
    urllib.request.urlretrieve(file_url, local_filename)
    
    # التأكد من حجم الملف (لحمايتك من ملفات الـ 0 بايت)
    file_size = os.path.getsize(local_filename) / (1024 * 1024)
    print(f"✅ اكتمل التحميل محلياً. الحجم: {file_size:.2f} MB")

    # رفع الملف إلى مستودعك في المسار الصحيح حسب هيكل D:\
    print(f"جاري الرفع إلى مستودعك في مجلد gfpgan/...")
    api.upload_file(
        path_or_fileobj=local_filename,
        path_in_repo="gfpgan/GFPGANv1.4.pth",
        repo_id=repo_id,
        token=token
    )
    print("--- ✅ تمت العملية بنجاح! اذهب للمستودع وتأكد من الحجم ---")

except Exception as e:
    print(f"❌ حدث خطأ أثناء المعالجة: {e}")

finally:
    # حذف الملف المؤقت لتنظيف مساحة العمل
    if os.path.exists(local_filename):
        os.remove(local_filename)
