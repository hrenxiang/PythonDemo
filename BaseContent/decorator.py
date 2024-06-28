import functools


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        print('shelf func name: {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")


example()
example()


def my_decorator(func):
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)
    print(greet.__name__) # 输出wrapper 加上@functools.wraps(func)，输出greet


greet('hello world')
