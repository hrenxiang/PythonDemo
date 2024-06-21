d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')

s1 = {1, 2, 3}
s2 = set([1, 2, 3])

d5 = {1: 123, "a": 1.00, 2: "bbb"}

s3 = {1, "2", 3.00}


def func_verify_equals():
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d1 == d2 == d3 == d4)
    print("====================")
    print(s1)
    print(s2)
    print(s1 == s2)


def func_verify_mixture():
    print(d5[1])
    print(d5["a"])
    print(d5[2])
    print("==========")
    print(1 in s3)
    print("2" in s3)


def func_sort():
    d = {'b': 1, 'a': 2, 'c': 10}
    d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])  # 根据字典键的升序排序
    d_sorted_by_value = sorted(d.items(), key=lambda x: x[1], reverse=True)  # 根据字典值的降序排序
    print(d_sorted_by_key)
    print(d_sorted_by_value)

    s = {3, 4, 2, 1}
    s_sorted = sorted(s)
    print(s_sorted)


if __name__ == '__main__':
    func_sort()
