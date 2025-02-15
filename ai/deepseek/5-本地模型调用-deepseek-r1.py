from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.llms import ChatMessage

llm = HuggingFaceLLM(
    model_name='/Users/hrenxiang/Documents/company/ai/deepseek/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B',
    tokenizer='/Users/hrenxiang/Documents/company/ai/deepseek/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B',
    model_kwargs={'trust_remote_code': True},
    tokenizer_kwargs={')trust_remote_code': True},
)

resp = llm.chat(messages=[ChatMessage(content='你好！')])

print(resp)
