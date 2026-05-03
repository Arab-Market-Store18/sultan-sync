import os
from huggingface_hub import hf_hub_download, HfApi

token = os.getenv("HF_TOKEN")
repo_id = "shababdd11/sultan-models"
api = HfApi()

# سحب GFPGAN فقط
temp_file = hf_hub_download(repo_id="akhaliq/GFPGAN", filename="GFPGANv1.4.pth")
api.upload_file(path_or_fileobj=temp_file, path_in_repo="gfpgan/GFPGANv1.4.pth", repo_id=repo_id, token=token)
print("✅ Done: GFPGANv1.4.pth")
