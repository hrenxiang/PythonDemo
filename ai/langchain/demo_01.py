import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

os.environ['LANGSMITH_TRACING'] = 'true'
os.environ['LANGSMITH_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGSMITH_API_KEY'] = ''
os.environ['LANGSMITH_PROJECT'] = 'python-demo-ai-langchain'
# os.environ[
#     'OPENAI_API_KEY'] = ''
#
# llm = ChatOpenAI(model='deepseek-chat',base_url='http://127.0.0.1:11434')
#
#
#
#
# # message = [
# #     SystemMessage(content='请将下面内容翻译为英语'),
# #     HumanMessage(content='你好！')
# # ]
#
# result = llm.invoke('你好！')
# print(f'结果是: {result}')


# import ollama
#
# llm = ollama.Client(host='http://127.0.0.1:11434')
#
# res = llm.chat(
#     model='deepseek-r1:14b',
#     messages=[{"role": "user", "content": "给我一周食谱"}],
#     options={"temperature": 0}
# )
#
# print(res)

from langchain_ollama import OllamaLLM

llm = OllamaLLM(base_url="http://127.0.0.1:11434", model='deepseek-r1:14b', temperature=0)

message = [
    SystemMessage(content='请将下面内容翻译为英语'),
    HumanMessage(content='这些是什么啊,有朋自远方来,不亦说乎！')
]

res = llm.invoke(message)

print(res)
