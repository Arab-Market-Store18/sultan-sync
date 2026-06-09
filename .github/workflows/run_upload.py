import os
from huggingface_hub import hf_hub_download, HfApi

api = HfApi(token=os.environ['HF_TOKEN'])
repo = 'shababdd11/sultan-comfy-env'

files = {
    'comfyanonymous/flux_dev_fp8_safetensors': 'flux1-dev-fp8.safetensors',
    'black-forest-labs/FLUX.1-schnell': 'ae.safetensors',
    'comfyanonymous/flux_text_encoders': 't5xxl_fp8_e4m3fn.safetensors'
}

for repo_id, filename in files.items():
    print(f'📥 جاري تحميل {filename}...')
    local_path = hf_hub_download(repo_id=repo_id, filename=filename, token=os.environ['HF_TOKEN'])
    print(f'📤 جاري رفع {filename}...')
    api.upload_file(path_or_fileobj=local_path, path_in_repo=filename, repo_id=repo)

