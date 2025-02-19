import os
from langchain_ollama import OllamaLLM
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes

# 通过 os.environ 改变当前进程的环境变量
os.environ['LANGSMITH_TRACING'] = 'true'
os.environ['LANGSMITH_ENDPOINT'] = 'https://api.smith.langchain.com'
# 这里需要自己登录 LangChain Smith 创建自己的 API KEY
os.environ['LANGSMITH_API_KEY'] = ''
# 自己当前项目的名称
os.environ['LANGSMITH_PROJECT'] = 'python-demo-ai-langchain'

# ========================================== 本地调用 ==========================================
# 指定模型
llm = OllamaLLM(base_url="http://127.0.0.1:11434", model='deepseek-r1:14b', temperature=0)

# 定义提示模板
prompt_template = ChatPromptTemplate.from_messages([
    ('system', '请将下面的内容翻译为{language}！'),
    ('user', '{text}')
])

# 简便写法
parser = StrOutputParser()

chain = prompt_template | llm | parser

# 把我们的 LangChain 程序部署为服务

# 1、安装依赖 pip install "langserve[all]"，创建 FastApi 的应用
fast_api = FastAPI(title='第一个LangChain服务', version='1.0', description='使用LangChain翻译任何语句的服务')

# 2、添加路由
add_routes(app=fast_api, runnable=chain, path="/chainDemo")

# 3、启动服务
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(fast_api, host="0.0.0.0", port=8000)

