from operator import itemgetter

from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama

from set_env import set_langsmith_variables

set_langsmith_variables()

from langchain_community.utilities import SQLDatabase

MYSQL_PATH = 'mysql+pymysql://root:123456@127.0.0.1:3306/huangrx-template-admin?charset=utf8mb4'

sql_database = SQLDatabase.from_uri(MYSQL_PATH)

# print(f'{sql_database.get_usable_table_names()}\n\n')

# print(sql_database.run('select * from t_sys_dept;'))

# 直接使用大模型与数据库整合
model = ChatOllama(base_url='http://127.0.0.1:11434', model='qwen2.5:14b', temperature=0)

chain = create_sql_query_chain(llm=model, db=sql_database)
# chain.get_prompts()[0].pretty_print()
# print(f'{chain.invoke(input={"question": "请问部门表中有哪些数据"})}\n\n\n\n')
# print(chain.invoke(input={"question": '请问部门表中有哪些数据，我只要文本格式的sql，其他任何字和格式都不要给我。'}))

answer_prompt = ChatPromptTemplate.from_template(
    """
    给定以下户问题，首先创建一个语法正确的查询以运行，然后查看查询结果并返回答案。

    Use the following format:

    Question: {question}
    SQLQuery: {query_sql}
    SQLResult: {result}
    Answer: Final answer here
    """
)

# 创建一个执行 SQL 语句的工具
execute_sql_tool = QuerySQLDatabaseTool(db=sql_database)

# 1、生成SQL语句 2、执行SQL 3、传入模板
result_chain = (RunnablePassthrough.assign(query_sql=chain)
                .assign(result=(itemgetter('query_sql') | execute_sql_tool))
                | answer_prompt
                | model
                | StrOutputParser()
                )

print(result_chain.invoke(input={"question": '请问部门表中有哪些数据，我只要文本格式的sql，其他任何字和格式都不要给我。', }))
