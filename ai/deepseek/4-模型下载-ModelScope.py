#模型下载
from modelscope import snapshot_download

model_dir = snapshot_download(model_id='deepseek-ai/DeepSeek-R1-Distill-Qwen-7B',
                              cache_dir='/Users/hrenxiang/Documents/company/ai/deepseek/models')