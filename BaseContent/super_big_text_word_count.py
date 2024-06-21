import re
from collections import defaultdict


def parse_chunk(text, word_cnt, leftover):
    # 将上一个块的剩余部分与当前块结合
    text = leftover + text
    # 去除所有非字母数字字符并转换为小写
    text = re.sub(r'[^\w ]', ' ', text).lower()
    # 将文本拆分为单词
    words = text.split(' ')
    # 保存最后一个部分作为新的剩余部分
    leftover = words.pop() if text[-1].isalnum() else ''
    # 统计当前块中的单词
    for word in words:
        if word:
            word_cnt[word] += 1
    return leftover


def word_count(file_path, chunk_size=1024):
    # 创建一个默认值为0的字典，用于存储每个单词的计数
    word_cnt = defaultdict(int)

    # 变量用于存储上次读取后剩下的未处理的部分
    leftover = ''

    # 打开指定路径的文件进行读取操作
    with open(file_path, 'r') as f:
        while True:
            # 读取指定大小的块（chunk_size）的文本数据
            chunk = f.read(chunk_size)

            # 如果没有读取到数据，表示已经到达文件末尾，跳出循环
            if not chunk:
                break

            # 处理读取到的块，并更新单词计数字典和剩余部分
            leftover = parse_chunk(chunk, word_cnt, leftover)
        # 处理最后一个剩余部分
        if leftover:
            parse_chunk(leftover, word_cnt, '')

    # 按词频从高到低排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    # 将结果写入输出文件
    with open('./file/big_text_output.txt', 'w') as f:
        for word, freq in sorted_word_cnt:
            f.write(f'{word} {freq}\n')


# 调用函数处理文件
word_count('./file/big_text.txt')
