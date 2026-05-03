import os
import requests
from huggingface_hub import HfApi

token = os.getenv("HF_TOKEN")
repo_id = "shababdd11/sultan-models"
api = HfApi()

# الرابط المباشر للملف (نسخة RAW لضمان الحجم الكامل)
file_url = "https://huggingface.co/public-data/replicate-models/resolve/main/GFPGANv1.4.pth"

print("--- بدء السحب المباشر لملف GFPGAN ---")

try:
    # 1. تحميل الملف إلى الذاكرة المؤقتة للـ Runner
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open("temp_gfpgan.pth", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # 2. الرفع المباشر إلى مستودعك
        api.upload_file(
            path_or_fileobj="temp_gfpgan.pth",
            path_in_repo="gfpgan/GFPGANv1.4.pth",
            repo_id=repo_id,
            token=token
        )
        print("✅ تم الرفع بنجاح! تحقق من الحجم الآن.")
    else:
        print(f"❌ خطأ في الرابط: {response.status_code}")

except Exception as e:
    print(f"❌ خطأ تقني: {e}")
