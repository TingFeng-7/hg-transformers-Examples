# pip install huggingface_hub datasets
from huggingface_hub import snapshot_download
import datasets
# repo_id = "ziqingyang/chinese-alpaca-lora-7b"
repo_id = "haonan-li/cmmlu"

local_dir = './dataset/' + repo_id
cache_dir = local_dir + "/cache"

dataset = datasets.load_dataset(repo_id,'anatomy')
dataset.save_to_disk(local_dir)