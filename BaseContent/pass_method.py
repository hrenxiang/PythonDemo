# 不可变对象示例
def my_func1(b):
    b = 2
    # A ====== 1
    # B ====== 2
    print("A ====== {}".format(a))
    print("B ====== {}".format(b))


a = 1
my_func1(a)


# 可变对象示例
def my_func2(d):
    d.append(4)
    # C ====== [1, 2, 3, 4]
    # D ====== [1, 2, 3, 4]
    print("C ====== {}".format(c))
    print("D ====== {}".format(d))


c = [1, 2, 3]
my_func2(c)


# 改变可变对象的值（另一种方法）
def my_func4(f):
    f = f + [4]
    # E ====== [1, 2, 3]
    # F ====== [1, 2, 3, 4]
    # e 和 f一开始都指向 [1, 2, 3]，但是方法内部从新定义了f的指向
    print("E ====== {}".format(e))
    print("F ====== {}".format(f))


e = [1, 2, 3]
my_func4(e)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2
print("L1 ====== ID：{}，CONTENT：{}".format(id(l1), l1))
print("L2 ====== ID：{}，CONTENT：{}".format(id(l2), l2))
print("L3 ====== ID：{}，CONTENT：{}".format(id(l3), l3))
