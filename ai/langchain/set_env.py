import os

def set_langsmith_variables():
    os.environ['LANGSMITH_TRACING'] = 'true'
    os.environ['LANGSMITH_ENDPOINT'] = 'https://api.smith.langchain.com'
    # 这里需要自己登录 LangChain Smith 创建自己的 API KEY
    os.environ['LANGSMITH_API_KEY'] = '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'
    # 自己当前项目的名称
    os.environ['LANGSMITH_PROJECT'] = 'python-demo-ai-langchain'