import os
import re

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 通过 os.environ 改变当前进程的环境变量
os.environ['LANGSMITH_TRACING'] = 'true'
os.environ['LANGSMITH_ENDPOINT'] = 'https://api.smith.langchain.com'
# 这里需要自己登录 LangChain Smith 创建自己的 API KEY
os.environ['LANGSMITH_API_KEY'] = ''
# 自己当前项目的名称
os.environ['LANGSMITH_PROJECT'] = 'python-demo-ai-langchain'

# ========================================== 本地调用 ==========================================
from langchain_ollama import OllamaLLM

# 指定模型
llm = OllamaLLM(base_url="http://127.0.0.1:11434", model='deepseek-r1:14b', temperature=0)

# 定义提示模板
prompt_template = ChatPromptTemplate.from_messages([
    ('system', '请将下面的内容翻译为{language}，并对句子进行详细的解析！(解析用中文)'),
    ('user', '{text}')
])

# 简便写法
parser = StrOutputParser()

chain = prompt_template | llm | parser

res = chain.invoke({'language': 'English', 'text': '我爱你，爱着你，就像老鼠爱大米！'})

print(f"简便写法的结果是：{res}")

# 使用正则表达式提取 </think> 后面的内容
match = re.search(r'</think>\s*(.*)', res, re.DOTALL)

if match:
    result = match.group(1).strip()  # 提取并去掉前后的空白字符
    print(f'提取的结果是: {result}')
else:
    print("没有找到有效的内容")
