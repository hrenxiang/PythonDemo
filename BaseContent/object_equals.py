# 比较的是两个对象的值
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True

# ===================================================================================================

# 比较的是两个对象的身份标识（内存地址）是否相同
print(a is b)  # False\
c = a
print(c is a)  # True

# ===================================================================================================

# 对象的身份标识可以通过 id(object) 获取
print(id(a))  # 4307093632
print(id(b))  # 4307093312
print(id(c))  # 4307093632

# ===================================================================================================

z = 256
x = 256
print(z == x)  # True
print(z is x)  # False

p = -100000000000006
q = -100000000000006
print(p == q)  # True
print(p is q)  # False
print(id(p))
print(id(q))

# ===================================================================================================

# RecursionError: maximum recursion depth exceeded in comparison
# 递归错误：比较中超过的最大递归深度
# 由于列表 x 包含对自身的引用，直接进行深度拷贝和比较时会导致无限递归，进而引发 RecursionError。
# 这是因为 copy.deepcopy 和 == 比较都涉及到递归遍历结构
import copy

x = [1]
x.append(x)
y = copy.deepcopy(x)


# print(x == y)

# 自定义比较方法 RecursionError
def compare_lists(l1, l2, seen=None):
    if seen is None:
        seen = set()

    if id(l1) in seen or id(l2) in seen:
        return True

    seen.add(id(l1))
    seen.add(id(l2))

    if l1 is l2:
        return True

    if len(l1) != len(l2):
        return False

    for i in range(len(l1)):
        if isinstance(l1[i], list) and isinstance(l2[i], list):
            if not compare_lists(l1[i], l2[i], seen):
                return False
        elif l1[i] != l2[i]:
            return False

    return True


print(compare_lists(x, y))

# ===================================================================================================

aa = [1, 2, 3]
bb = copy.deepcopy(aa)

print(id(aa))
print(id(bb))

cc = 1
dd = 2
print(id(cc))
print(id(dd))

ee = '1'
ff = '2'
print(id(ee))
print(id(ff))
