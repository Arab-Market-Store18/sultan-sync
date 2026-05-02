import os 
from huggingface_hub import hf_hub_download, HfApi

# إعدادات الهوية والمستودع
token = os.getenv("HF_TOKEN")
# استخدام معرفك التقني shababdd11 بناءً على سجلاتك
repo_id = "shababdd11/sultan-models" 
api = HfApi()

# قائمة المواقع الحقيقية للملفات الناقصة (نتائج بحث مايو 2026)
files_to_sync = [
    # إصلاح حزمة Buffalo_L (حل مشكلة الـ 0 Bytes)
    {"src_repo": "public-data/insightface", "filename": "models/buffalo_l/scrfd_10g_bnkps.onnx", "target": "insightface/models/buffalo_l/scrfd_10g_bnkps.onnx"},
    {"src_repo": "public-data/insightface", "filename": "models/buffalo_l/landmark_3d_68.onnx", "target": "insightface/models/buffalo_l/landmark_3d_68.onnx"},
    
    # نماذج التبديل والتحسين (إصلاح المعطوب)
    {"src_repo": "ezioruan/inswapper_128", "filename": "hyperswap_256_1c.onnx", "target": "swap/hyperswap_256_1c.onnx"},
    {"src_repo": "sczhou/CodeFormer", "filename": "CodeFormer.pth", "target": "codeformer/codeformer.pth"},
    {"src_repo": "akhaliq/GFPGAN", "filename": "GFPGANv1.4.pth", "target": "gfpgan/GFPGANv1.4.pth"},
    
    # نماذج الكشف
    {"src_repo": "isat-ai/yolov8-face", "filename": "yolov8n-face.pt", "target": "detection/yolov8n-face.pt"}
]

def run_repair():
    for item in files_to_sync:
        print(f"جاري سحب {item['filename']} من الموقع الحقيقي الموثق...")
        try:
            # تحميل الملف الأصلي بنجاح
            local_path = hf_hub_download(repo_id=item['src_repo'], filename=item['filename'])
            
            # رفعه لمستودعك في المسار التنظيمي الصحيح
            api.upload_file(
                path_or_fileobj=local_file,
                path_in_repo=item['target'],
                repo_id=repo_id,
                token=token
            )
            print(f"✅ تم إصلاح ورفع: {item['target']}")
        except Exception as e:
            print(f"❌ خطأ تقني في {item['filename']}: {e}")

if __name__ == "__main__":
    run_repair()
