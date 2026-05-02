import os
from huggingface_hub import hf_hub_download, HfApi

# 1. جلب التوكن الذي قمت بإعداده مسبقاً
token = os.getenv("HF_TOKEN")
repo_id = "shababdd11/sultan-models" # معرف مستودعك التقني
api = HfApi()

# 2. قائمة الملفات الناقصة مع روابطها الحقيقية لعام 2026
# تم تحديد هذه المصادر لإصلاح ملفات الـ 0 Bytes
files_to_sync = [
    {"src": "public-data/insightface", "file": "models/buffalo_l/scrfd_10g_bnkps.onnx", "target": "insightface/models/buffalo_l/scrfd_10g_bnkps.onnx"},
    {"src": "public-data/insightface", "file": "models/buffalo_l/landmark_3d_68.onnx", "target": "insightface/models/buffalo_l/landmark_3d_68.onnx"},
    {"src": "ezioruan/inswapper_128", "file": "inswapper_128.onnx", "target": "swap/inswapper_128.onnx"},
    {"src": "sczhou/CodeFormer", "file": "CodeFormer.pth", "target": "codeformer/codeformer.pth"},
    {"src": "akhaliq/GFPGAN", "file": "GFPGANv1.4.pth", "target": "gfpgan/GFPGANv1.4.pth"}
]

print("--- بدء عملية السحب والإصلاح البرمجي ---")

for item in files_to_sync:
    try:
        print(f"جاري سحب {item['file']} من المصدر الرسمي...")
        # تحميل الملف الأصلي (بدلاً من الـ 0 Bytes المعطوب)
        local_path = hf_hub_download(repo_id=item['src'], filename=item['file'])
        
        # رفعه لمستودعك باستخدام التوكن الموجود مسبقاً
        api.upload_file(
            path_or_fileobj=local_path,
            path_in_repo=item['target'],
            repo_id=repo_id,
            token=token
        )
        print(f"✅ تم الرفع بنجاح إلى: {item['target']}")
    except Exception as e:
        print(f"❌ خطأ في معالجة {item['file']}: {e}")

print("--- انتهت العملية بنجاح ---")
