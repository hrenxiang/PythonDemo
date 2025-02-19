import requests

response = requests.post(
    url='http://127.0.0.1:11434/api/generate',
    json={"model": "deepseek-r1:14b", "prompt": "你好啊，你是谁?，你有什么用", "stream": False}
)

print(response.status_code)
print(response.text)