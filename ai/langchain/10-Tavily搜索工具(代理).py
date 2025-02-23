import os

from langchain_community.tools import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_ollama.chat_models import ChatOllama
from langgraph.prebuilt import chat_agent_executor

from set_env import set_langsmith_variables

# 设置 langsmith 所需环境变量
set_langsmith_variables()

# 构建基础模型
llm = ChatOllama(base_url="http://127.0.0.1:11434", model='qwen2.5:14b', temperature=0)

# ==================================   没有任何代理下询问   ====================================
print(f'{llm.invoke("郑州今天天气怎么样！")}\n\n')

# ==========================================================================================

# ==================================   使用Tavily搜索引擎   ==================================
os.environ['TAVILY_API_KEY'] = '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'
search_engine = TavilySearchResults(
    max_results=1  # 搜索的结果最多两个
)

# print(search_engine.invoke("郑州今天天气怎么样！"))

# ==========================================================================================

# 使用模型绑定工具，有的模型提供 model.bind_tools([search_engine])，但是langchain-ollama中好像没有
tools = [search_engine]
llm_with_tools = llm.bind_tools(tools)

# resp = llm_with_tools.invoke([HumanMessage(content="中国的首都是哪个城市")])
# print(f'Model Content: {resp.content}\n')
# print(f'Tools Calls: {resp.tool_calls}\n\n')
#
# resp2 = llm_with_tools.invoke([HumanMessage(content="郑州今天天气怎么样")])
# print(f'Model Content: {resp2.content}\n')
# print(f'Tools Calls: {resp2.tool_calls}\n')

# =======================================   创建代理   =======================================
agent_executor = chat_agent_executor.create_tool_calling_executor(model=llm, tools=tools)

message1 = {
    'messages': [HumanMessage(content="中国的首都是哪个城市")]
}

message2 = {
    'messages': [HumanMessage(content="郑州今天天气怎么样")]
}

resp1 = agent_executor.invoke(input=message1)
resp2 = agent_executor.invoke(input=message2)

print(f'{resp1}\n\n')
# print(f'{resp2}\n\n')
print(f'{resp2["messages"][2]}')
# ==========================================================================================
