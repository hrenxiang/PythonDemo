from langserve import RemoteRunnable

if __name__ == '__main__':
    client = RemoteRunnable(url='http://127.0.0.1:8000/chainDemo/')
    res = client.invoke({'language': 'English', 'text': 'hello'})
    print(res)