import os
import re

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# 通过 os.environ 改变当前进程的环境变量
os.environ['LANGSMITH_TRACING'] = 'true'
os.environ['LANGSMITH_ENDPOINT'] = 'https://api.smith.langchain.com'
# 这里需要自己登录 LangChain Smith 创建自己的 API KEY
os.environ['LANGSMITH_API_KEY'] = ''
# 自己当前项目的名称
os.environ['LANGSMITH_PROJECT'] = 'python-demo-ai-langchain'

# ========================================== 调用Open Ai ==========================================
# os.environ['OPENAI_API_KEY'] = ''
#
# llm = ChatOpenAI(model='gpt-3.5-turbo',base_url='http://127.0.0.1:11434')
#
# message = [
#     SystemMessage(content='请将下面内容翻译为英语'),
#     HumanMessage(content='你好！')
# ]
# result = llm.invoke('你好！')

# print(f'结果是: {result}')
# 简单解析结果
# parser = StrOutputParser()
# parser_result = parser.parse(result)
# print(f'简单解析后的结果是: {parser_result}')


# ========================================== 本地调用 ==========================================
from langchain_ollama import OllamaLLM

llm = OllamaLLM(base_url="http://127.0.0.1:11434", model='deepseek-r1:14b', temperature=0)

message = [
    SystemMessage(content='请将下面内容翻译为英语'),
    HumanMessage(content='这些是什么啊,有朋自远方来,不亦说乎！')
]

res = llm.invoke(message)

print(f'结果是: {res}')

# 使用正则表达式提取 </think> 后面的内容
match = re.search(r'</think>\s*(.*)', res, re.DOTALL)

if match:
    result = match.group(1).strip()  # 提取并去掉前后的空白字符
    print(f'提取的结果是: {result}')
else:
    print("没有找到有效的内容")

# 简便写法
parser = StrOutputParser()
chain = llm | parser
print(f"简便写法的结果是：{chain.invoke(message)}")

# ========================================== 本地调用（不使用 LangChain 相关依赖） ==========================================
# 不使用 LangChain 相关依赖的话，在 Smith 控制台中看不到上面配置的项目，无法与之配合使用
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
