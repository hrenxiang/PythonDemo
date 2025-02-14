from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.llms import ChatMessage

llm = HuggingFaceLLM(model='/Users/hrenxiang/.ollama/models/manifests/registry.ollama.ai/library/deepseek-r1')

resp = llm.chat(messages=[ChatMessage(content='你好！')])

print(resp)
