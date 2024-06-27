import time

# 定义与表示
str1 = 'hello world'
str2 = '''hello world'''
str3 = "hello world"
str4 = """hello world"""

# 结果 True
print(str1 == str2 == str3 == str4)

s = 'a\nb\tc'
print(s)

name = 'jason'
print(name[0])  # 输出：'j'
print(name[1:3])  # 输出：'as'

for char in name:
    print(char)
    # 输出：
    # j
    # a
    # s
    # o
    # n

path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0]  # 输出：'ads'
print(namespace)
table = path.split('//')[1].split('/')[1]  # 输出：'training_table'
print(table)

id = '123'
name = 'jason'
print('no data available for person with id: {}, name: {}'.format(id, name))

# 方法一：直接字符串拼接
start_time = time.time()
s = ''
for n in range(0, 100000):
    s += str(n)
end_time = time.time()
print("直接字符串拼接时间：", end_time - start_time)

# 方法二：列表拼接后使用 join
start_time = time.time()
l = []
for n in range(0, 100000):
    l.append(str(n))
s = ' '.join(l)
end_time = time.time()
print("列表拼接后使用 join 时间：", end_time - start_time)


def func_test():
    """
    print(123)
    print(456)
    """
    print(789)


if __name__ == '__main__':
    func_test()
