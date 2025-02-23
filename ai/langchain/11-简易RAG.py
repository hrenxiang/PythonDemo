import os

import bs4
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.chat_message_histories import ChatMessageHistory

from set_env import set_langsmith_variables

# 设置 langsmith 所需环境变量
set_langsmith_variables()

# 设置 USER_AGENT 环境变量
os.environ['USER_AGENT'] = 'Apifox/1.0.0 (https://apifox.com)'

from langchain_community.document_loaders import \
    WebBaseLoader  # USER_AGENT environment variable not set, consider setting it to identify your requests. 在导入前设置环境变量

## 加载：首先，我们需要加载数据。这是通过DocumentLoaders完成的。
web_base_loader = WebBaseLoader(web_paths=["https://javabetter.cn/interview/mysql-60.html"],
                                bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=('vp-page'))))

docs = web_base_loader.load()

# print(f"found {len(docs)} documents \n\n {docs}")
# ======================================================================================================================

## 分割：Text splitters将大型文档分割成更小的块。这对于索引数据和将其传递给模型很有用，因为大块数据更难搜索，并且不适合模型的有限上下文窗口。
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
# 为了可以更好的观察，这里我们分割的是得到的文本，但是docs从加载哪里打印的可以看出，是一个Document对象列表
# for text_chunk in text_splitter.split_text(docs[0].page_content):
#     print(f"{text_chunk}----\n")
# 所以在真正使用的时候，请使用 split_documents
text_chunks = text_splitter.split_documents(docs)
# ======================================================================================================================

## 存储：我们需要一个地方来存储和索引我们的分割，以便以后可以搜索。这通常使用VectorStore和Embeddings模型完成。
huggingface_embeddings = HuggingFaceEmbeddings(model_name='iampanda/zpoint_large_embedding_zh',
                                               model_kwargs={'device': 'cpu'},
                                               encode_kwargs={'normalize_embeddings': True}, )

vector_store = Chroma.from_documents(documents=text_chunks, embedding=huggingface_embeddings)

retriever = vector_store.as_retriever()
# ======================================================================================================================

## 检索：给定用户输入，使用检索器从存储中检索相关分割。
system_prompt = """你是一个问答助手。 
请使用以下获取的上下文片段来回答问题。如果上下文中没有答案，请说你不知道。保持答案简洁。
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human", "{input}")
])

# 构建基础模型
model = ChatOllama(base_url="http://127.0.0.1:11434", model='deepseek-r1:14b', temperature=0)

# 创建一个链以将文档列表传递给模型
docs_chain = create_stuff_documents_chain(llm=model, prompt=prompt)

# 创建检索链，检索文档然后将其传递
# retrieval_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=docs_chain)
# ======================================================================================================================

## 生成：ChatModel / LLM使用包括问题和检索到的数据的提示生成答案。
# resp = retrieval_chain.invoke({"input": "关系型数据库的优点？"})
#
# print(f"{resp}\n\n")
# print(f"{resp['answer']}\n\n")

'''
注意：
一般情况下，我们构建的链（chain）直接使用输入问答记录来关联上下文，但是在此案例中，查询检索器也需要对话上下文才能被理解。

解决办法
添加一个子链，它采用最新用户问题和聊天历史，并在它引用历史信息中的任何信息时重新表述问题，这可以被简单的认为是构建这个子链的目的，让检索过程融入了对话的上下文。
'''

# 添加子链
contextualize_q_system_prompt = """给定聊天历史和最新的用户问题，
这些问题可能在聊天历史中引用了上下文，
形成一个独立的问题，可以在没有聊天历史的情况下理解。
不要回答问题，如果需要，只需要重新表述问题，否则直接返回原问题。"""

retriever_history_temp = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human", "{input}")
])

history_chain = create_history_aware_retriever(
    llm=model,
    retriever=retriever,
    prompt=retriever_history_temp
)

# 保存问答的历史记录
store = {}


# 回调函数，此函数预期将接收一个 session_id 并返回一个消息历史记录对象
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# 整合父链和子链
retrieval_chain = create_retrieval_chain(retriever=history_chain, combine_docs_chain=docs_chain)

# 手动定义一个 session_id，实际根据情况进行获取
config = {'configurable': {'session_id': 'huangrx123'}}

# 携带历史消息进行聊天
result_chain = RunnableWithMessageHistory(
    runnable=retrieval_chain,
    get_session_history=get_session_history,
    input_messages_key='input',
    history_messages_key='chat_history',
    output_messages_key='answer',
)

# 第一轮对话
resp = result_chain.invoke({'input': 'MySQL使用索引的根本原因？'}, config=config, )
# print(f"{resp}\n\n")
print(f"{resp['answer']}\n\n")

# 第二轮对话
resp1 = result_chain.invoke({'input': '他的扩展有内容哪些？'}, config=config, )
print(f"{resp1['answer']}\n\n")