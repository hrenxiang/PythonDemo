def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of


square = nth_power(2)
cube = nth_power(3)

print(square(2))
# 输出: 4

print(cube(2))


# 输出L: 8


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@decorator
def say_hello(name):
    print("Hello, {}".format(name))


say_hello('Alice')

add = lambda x, y: x + y
print(add(3, 5))
# 输出: 8

# 使用在内置函数中
nums = [1, 2, 3, 4, 5]
m = map(lambda x: x ** 2, nums)
print(m)
squared = list(m)
print(squared)


# 输出: [1, 4, 9, 16, 25]

def add(a: int, b: int) -> int:
    return a + b


print(add(3, 5))

d = {'mike': 10, 'lucy': 2, 'ben': 30}


def sort_dict(d: dict):
    return sorted(d.items(), key=lambda x: x[1])


def sort_dict2(d: dict):
    return sorted(value for key, value in d.items())


print(sort_dict(d))
print(sort_dict2(d))

for item in d.items():
    print(item)
    print(item[0])

items_ = {key: value for key, value in d.items()}

from functools import reduce

l = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, l)
print(product)  # 输出: 120
