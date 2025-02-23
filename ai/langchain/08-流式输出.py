import importlib
import os

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_ollama import OllamaLLM
from langchain_community.chat_message_histories import ChatMessageHistory

# 通过 os.environ 改变当前进程的环境变量
importlib.import_module("ai.langchain.set_env")

# ========================================== 本地调用 ==========================================
# 指定模型
llm = OllamaLLM(base_url="http://127.0.0.1:11434", model='deepseek-r1:14b', temperature=0)

# 定义提示模板
prompt_template = ChatPromptTemplate.from_messages([
    ('system', '你是一个乐于助人的助手。用{language}尽你可能的回答所有问题。'),
    MessagesPlaceholder(variable_name='my_messages')  # 要跟后面 每次聊天时发送消息的键 msg的key 进行对应
])

# 获取链
chain = prompt_template | llm

# 保存历史聊天记录，所有用户的聊天记录都保存到 store。key：sessionId，value：历史聊天记录对象
store = {}


# 回调函数，此函数预期将接收一个 session_id 并返回一个消息历史记录对象
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# 携带历史消息进行聊天
do_message = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_session_history,
    input_messages_key='my_messages',  # 每次聊天时发送消息的键 msg的key
)

# 手动定义一个 session_id，实际根据情况进行获取
config = {'configurable': {'session_id': 'huangrx123'}}

# 第一轮，使用 stream 进行调用，最后流式输出
for resp in do_message.stream(
        input={'my_messages': [HumanMessage(content='给我讲一个好听的童话故事！')], 'language': 'zh-CN', },
        config=config):
    print(resp, end='')
    # 设定一个分隔符，可以看每次输出一个token，这样看流式比较清晰
    # print(resp, end='-')

# resp = do_message.invoke(
#     input={'my_messages': [HumanMessage(content='给我讲一个好听的童话故事！')], 'language': 'zh-CN', }, config=config)
#
# print(resp)
