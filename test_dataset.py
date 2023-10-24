import datasets
from datasets import load_dataset
repo_id = "haonan-li/cmmlu"
# @ dataset
anatomy_subset = load_dataset(repo_id,'anatomy')
test_data = anatomy_subset['test']
dev_data  = anatomy_subset['dev']

# @ preprocess https://huggingface.co/docs/datasets/nlp_process

# test_data = test_data.map(lambda examples: tokenizer(examples["text"]), batched=True)


from transformers import AutoModelForCausalLM, AutoTokenizer
# @tokenizer
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
inputs = tokenizer.encode("The weather is always wonderful", return_tensors="pt")
# inputs_id = inputs[0]
for inp_id in inputs[0]:
    encode_inps = tokenizer.decode(inp_id)
    print(encode_inps)
print("hello, world")