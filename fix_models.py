import os
from huggingface_hub import hf_hub_download, HfApi

# إعدادات الدخول
token = os.getenv("HF_TOKEN")
repo_id = "shababdd11/sultan-models"
api = HfApi()

# العنوان الجديد والموثق للنموذج (بدلاً من العنوان القديم المعطوب)
SOURCE_REPO = "hfmaster/models-moved"
SOURCE_FILENAME = "face-restore/GFPGANv1.4.pth"

print(f"--- بدء سحب GFPGANv1.4.pth من العنوان الجديد ---")

try:
    # 1. تحميل الملف من المستودع البديل
    temp_file = hf_hub_download(repo_id=SOURCE_REPO, filename=SOURCE_FILENAME)
    
    # 2. رفعه إلى مستودعك في المجلد المخصص له حسب هيكل D:\
    api.upload_file(
        path_or_fileobj=temp_file, 
        path_in_repo="gfpgan/GFPGANv1.4.pth", 
        repo_id=repo_id, 
        token=token
    )
    print("✅ تم سحب وإصلاح ملف GFPGANv1.4.pth بنجاح!")

except Exception as e:
    print(f"❌ فشل السحب مجدداً. السبب: {e}")
