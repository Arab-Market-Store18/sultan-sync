import os
from huggingface_hub import HfApi

# 1. الإعدادات
token = os.getenv("HF_TOKEN")
repo_id = "shababdd11/sultan-models"
api = HfApi()

# رابط الملف المباشر (Raw)
file_url = "https://huggingface.co/public-data/replicate-models/resolve/main/GFPGANv1.4.pth"

print("--- محاولة الرفع المباشر لتجاوز مشكلة الـ 0 بايت ---")

try:
    # الرفع باستخدام upload_file ولكن مع تحديد run_as_future أو الرفع من URL مباشرة
    # هذه الدالة تجبر Hugging Face على سحب الملف بنفسه إلى مستودعك
    api.upload_file(
        path_or_fileobj=file_url, # نمرر الرابط مباشرة هنا
        path_in_repo="gfpgan/GFPGANv1.4.pth",
        repo_id=repo_id,
        token=token,
        repo_type="model"
    )
    print("✅ تم إرسال أمر السحب المباشر للموقع!")
    print("انتظر دقيقة ثم حدث الصفحة، سيتولى سيرفر Hugging Face المهمة.")

except Exception as e:
    print(f"❌ حدث خطأ: {e}")
