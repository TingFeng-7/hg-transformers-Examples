# Load model directly
from transformers import AutoProcessor, AutoModelForCausalLM
from os.path import join as pathj
# from transformers import LLavaC

model_rootdir = "/Users/tingfengwu/code/models/"
epo_id = "liuhaotian/llava-v1.5-7b"
repo_id = "liuhaotian/llava-v1.5-13b"
local_id = pathj(model_rootdir, repo_id)
print(local_id)
# processor = AutoProcessor.from_pretrained(model_rootdir + "liuhaotian/llava-v1.5-13b")
model = AutoModelForCausalLM.from_pretrained(model_rootdir + "liuhaotian/llava-v1.5-13b")