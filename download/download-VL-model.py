# pip install huggingface_hub
from huggingface_hub import snapshot_download

repo_id = "liuhaotian/llava-v1.5-7b"
repo_id = "liuhaotian/llava-v1.5-13b"

repo_id = 'OpenGVLab/InternVL-Chat-Chinese-V1-1'

model_name = repo_id.split('/')[-1]
local_dir = './models/' + repo_id
cache_dir = local_dir + "/cache"
# 因为huggingface_hub默认在linux中下载到系统缓存管理中，
# 只需更改默认参数local_dir_use_symlinks=False，还可以通过local_dir设置存储路径。
is_download_model = True

allow = ["*.model", "*.json", "*.py", "*.md", "*.txt"]
ignore = [ "*.msgpack", "*.h5", "*.ot", ] #: 避免下载任何模型
model_suffix = [ "*.safetensors", "*.bin" ]

if is_download_model:
    allow += model_suffix
print(allow)
while True:
    try:
        snapshot_download(
            repo_id=repo_id,
            local_dir=local_dir,
            cache_dir=cache_dir,
            local_dir_use_symlinks=False,
            resume_download=True,
            allow_patterns=allow,
            ignore_patterns=ignore,
        )
        print("download success")
        break
    except Exception as e :
        print(e)
