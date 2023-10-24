# pip install huggingface_hub
import sys
from huggingface_hub import snapshot_download
# repo_id = "ziqingyang/chinese-alpaca-lora-7b"
repo_id = sys.argv[1]
local_dir = f'./models/{repo_id}'
cache_dir = local_dir + "/cache"
# 因为huggingface_hub默认在linux中下载到系统缓存管理中，
# 只需更改默认参数local_dir_use_symlinks=False，
# 还可以通过local_dir设置存储路径。
while True:
    try:
        snapshot_download(
            repo_id=repo_id,
            local_dir=local_dir,
            cache_dir=cache_dir,
            local_dir_use_symlinks=False,
            resume_download=True,
            allow_patterns=["*.model", "*.json", "*.bin",
            "*.py", "*.md", "*.txt"],
            ignore_patterns=["*.safetensors", "*.msgpack",
            "*.h5", "*.ot", ],
        )
    except Exception as e :
        print(e)
