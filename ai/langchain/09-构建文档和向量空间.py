import importlib
import os

from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_ollama import OllamaEmbeddings, OllamaLLM

from set_env import set_langsmith_variables

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
# ollama_embeddings = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
hugging_face_embeddings = HuggingFaceEmbeddings(model_name='iampanda/zpoint_large_embedding_zh',
                                                model_kwargs={'device': 'cpu'},
                                                encode_kwargs={'normalize_embeddings': True})
# 实例化向量数据库
# vector_store = Chroma.from_documents(documents=document_sample, embedding=ollama_embeddings)
vector_store = Chroma.from_documents(documents=document_sample, embedding=hugging_face_embeddings)

# 进行相似度查询，with_score 代表也返回相似度的分数，相似度越高距离越近分值越低，相似度越低距离越远分值越高
print(vector_store.similarity_search_with_score('咖啡猫'))  # 有多个结果值

# 组装为 Runnable 接口，方便后续调用
vector_store_retriever = RunnableLambda(vector_store.similarity_search_with_score).bind(k=1)
# print(vector_store_retriever.batch(['黑猫', '金鱼']))
# 用batch 传入 ['黑猫', '金鱼'] 每个有一个结果值，因为上面用bing(k=1)，获取了第一个

# 导入 langsmith 环境变量
set_langsmith_variables()

# 构建基础模型
llm = OllamaLLM(base_url="http://127.0.0.1:11434", model='deepseek-r1:14b', temperature=0)

# 定义提示模板
message = """
### 问题:
{question} 

### 上下文:
{context}

### 任务
请只用提供的上下文回答下面的question，并给出内容来源，上下文中的 source 字段

### 任务要求
1、回答内容不要丰富，就按上下文中的数据原封不动的输出，谢谢


"""
prompt_template = ChatPromptTemplate.from_messages(messages=[
    ('human', message),
])

# 获取链
chain = {'question': RunnablePassthrough(), 'context': vector_store_retriever} | prompt_template | llm

print(chain.invoke("请介绍一下蛇"))
