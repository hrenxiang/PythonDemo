import re


def parse(text):
    # 使用正则表达式去除所有非字母数字和空格的字符，并将文本转换为小写
    text = re.sub(r'[^\w ]', ' ', text).lower()
    # 将文本按照空格分割成单词列表
    word_list = filter(None, text.split(' '))
    # 创建一个空字典，用于存储每个单词及其出现的频率
    word_cnt = {}
    # 遍历单词列表，统计每个单词的频率
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    # 将字典按词频从高到低排序，并返回排序后的列表
    return sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)


with open('./file/input.txt', 'r') as fin:
    content = fin.read()

word_and_freq = parse(content)

with open('./file/output.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))
