import os

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_ollama import OllamaLLM
from langchain_community.chat_message_histories import ChatMessageHistory

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

# 第一轮
resp = do_message.invoke(
    input={
        'my_messages': [
            HumanMessage(content='你好啊，我是大帅哥！')
        ],
        'language': 'zh-CN',
    },
    config=config,
)

print(f'==============================\n第一轮回答：\n{resp}\n==============================\n\n')

# 第二轮
resp2 = do_message.invoke(
    input={
        'my_messages': [
            HumanMessage(content='我前面那一句说的是什么')
        ],
        'language': 'zh-CN',
    },
    config=config,
)

print(f'==============================\n第二轮回答：\n{resp2}\n==============================\n\n')

# 第三轮，修改 session_id，代表的是开启一个新用户的对话，那就应该找不到之前的对话内容
config3 = {'configurable': {'session_id': 'zhangsan'}}
resp3 = do_message.invoke(
    input={
        'my_messages': [
            HumanMessage(content='我前面那一句说的是什么')
        ],
        'language': 'zh-CN',
    },
    config=config3,
)

print(f'==============================\n第三轮回答：\n{resp3}\n==============================\n\n')
