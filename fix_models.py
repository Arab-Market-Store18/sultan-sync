name: Sultan Verified GFPGAN
on:
  workflow_dispatch:

jobs:
  transfer:
    runs-on: ubuntu-latest
    steps:
      - name: Install Tools
        run: pip install -U huggingface_hub

      - name: Verified Download and Upload
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          # 1. تسجيل الدخول
          huggingface-cli login --token $HF_TOKEN
          
          # 2. تحميل ملف GFPGAN من المصدر الموثق (Raw URL)
          # سنستخدم wget هنا لأنها الأسرع للملفات المنفردة
          mkdir -p ./gfpgan
          wget -q https://huggingface.co/public-data/replicate-models/resolve/main/GFPGANv1.4.pth -O ./gfpgan/GFPGANv1.4.pth
          
          # 3. الرفع لمستودعك بنفس الطريقة التي نجحت في الاختبار
          huggingface-cli upload shababdd11/sultan-models ./gfpgan ./gfpgan --repo-type model
