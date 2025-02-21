import importlib

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory, RunnableLambda, RunnablePassthrough
from langchain_ollama import OllamaLLM
from langchain_chroma import Chroma
from llama_index.legacy.embeddings import OllamaEmbedding

# 准备测试数据，假设数据如下
document_sample = [
    Document(
        page_content="猫是最受欢迎的宠物之一，它们因其优雅的姿态和独立的性格而深受喜爱。",
        metadata={"source": "哺乳动物宠物文档", "date": "2021-12-30"}
    ),
    Document(
        page_content="狗是伟大的伴侣，以忠诚和友好而闻名！",
        metadata={"source": "哺乳动物宠物文档"}
    ),
    Document(
        page_content="兔子是一种小型的哺乳动物，它们喜欢群体生活并有极高的繁殖能力。",
        metadata={"source": "哺乳动物宠物文档"}
    ),
    Document(
        page_content="金鱼是最常见的宠物之一，特别适合忙碌的人群。",
        metadata={"source": "水生生物文档"}
    ),
    Document(
        page_content="鹦鹉不仅外表鲜艳，且能学会说话，成为家中的娱乐明星。",
        metadata={"source": "鸟类宠物文档"}
    ),
    Document(
        page_content="蛇作为宠物逐渐获得了一些喜爱，但它们需要专业的照顾和环境。",
        metadata={"source": "爬行动物宠物文档"}
    )
]

# 定义嵌入模型
hugging_face_embeddings = HuggingFaceEmbeddings(model_name='iampanda/zpoint_large_embedding_zh',
                                                model_kwargs={'device': 'mps'},
                                                encode_kwargs={'normalize_embeddings': True})
page_contents = [doc.page_content for doc in document_sample]
# 实例化向量数据库
vector_store = Chroma.from_documents(documents=document_sample, embedding=hugging_face_embeddings)

# 进行相似度查询，with_score 代表也返回相似度的分数，相似度越高距离越近分值越低，相似度越低距离越远分值越高
# print(vector_store.similarity_search_with_score('咖啡猫')) # 有多个结果值

# 组装为 Runnable 接口，方便后续调用
vector_store_retriever = RunnableLambda(lambda query: [
    doc.page_content for doc, _ in vector_store.similarity_search_with_score(query, k=1)
])
# print(vector_store_retriever.invoke('黑猫'))
# vector_store_retriever = RunnableLambda(vector_store.similarity_search_with_score).bind(k=1)
# print(vector_store_retriever.batch(['黑猫', '金鱼']))
# 用batch 传入 ['黑猫', '金鱼'] 每个有一个结果值，因为上面用bing(k=1)，获取了第一个

# 导入 langsmith 环境变量
importlib.import_module('ai.langchain.set_env')

# 构建基础模型
llm = OllamaLLM(base_url="http://127.0.0.1:11434", model='deepseek-r1:7b', temperature=0)

# 定义提示模板
message = """
使用提供的上下文回答这个问题:
{question}

上下文:
{context}
"""
prompt_template = ChatPromptTemplate.from_messages(messages=[
    ('human', 'message'),
    MessagesPlaceholder(variable_name='my_messages')  # 要跟后面 每次聊天时发送消息的键 msg的key 进行对应
])

# 获取链
chain = {'question': RunnablePassthrough(), 'context': vector_store_retriever} | prompt_template | llm

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

# 调用时传入的 input 内容
input_content = {
    'my_messages': [HumanMessage(content='请介绍一下猫。')],  # 用户消息列表
    'language': 'zh-CN',  # 语言设置
}

# 调用 stream
for resp in do_message.stream(input=input_content, config=config):
    print(resp, end='')
