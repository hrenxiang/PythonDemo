l1 = [1, 2, "hello", "world"]  # 列表中同时含有int和string类型

tup1 = ("json", 18)

l1.append("huang")
l2 = l1  # 列表追加

tup2 = tup1 + ("boy",)


def main():
    for i in l1:
        print(i)
    for e in tup1:
        print(e)


def print_append_demo():
    for i in l2:
        print(i)
    for e in tup2:
        print(e)


def acquire_element():
    print(l2[4])
    print(l2[-1])
    print(tup2[2])
    print(tup2[-1])


def slice_method():
    print(l2[0:5])  # 返回列表中索引从0到4的子列表
    print(l2[1:6])  # 返回列表中索引从1到5的子列表
    print(l2[-2:])  # 返回列表中索引从-2到列表末尾的子列表
    print(tup2[1:5])  # 返回列表中索引从1到4的子元组
    print(tup2[-2:])  # 返回列表中索引从-=2到元组末尾的子元组


def func_conversion():
    l3 = list(tup2)
    tup3 = tuple(l2)
    for i in l3:
        print(i)
    print("========")
    for e in tup3:
        print(e)


def func_sort():
    # l2.sort()
    l4 = [5, 3, 4, 1, 2]
    l4.sort()
    for i in l4:
        print(i)
    l5 = ["5", "3", "4", "1", "2"]
    l5 = sorted(l5)
    for i in l5:
        print(i)

    print("===========")

    tup4 = (5, 3, 4, 1, 2)
    tup4_sorted = sorted(tup4)  # 元组排序后会返回新元组
    for i in tup4_sorted:
        print(i)
    tup5 = ("5", "3", "4", "1", "2")
    tup5_sorted = sorted(tup5)
    for i in tup5_sorted:
        print(i)


def func_reversed():
    l2.reverse()
    for i in l2:
        print(i)
    print("=======")
    r = reversed(l2)
    for i in r:
        print(i)
    print("=======")
    tup2_reverse = reversed(list(tup2))
    for i in tup2_reverse:
        print(i)


# 输出内置属性
print(__name__)

if __name__ == '__main__':
    func_reversed()
