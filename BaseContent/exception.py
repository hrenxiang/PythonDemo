# var1 = 10 / 0
# Traceback (most recent call last):
#   File "/Users/hrenxiang/Documents/development/python-workspace/PythonDemo/BaseContent/./exception.py", line 1, in <module>
#     var1 = 10 / 0
# ZeroDivisionError: division by zero

# try:
#     var1 = 10 / 0
# except ZeroDivisionError as e:
#     print(str(e))


class MyInputError(Exception):
    """自定义异常类型"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{} is invalid input".format(repr(self.value))


try:
    raise MyInputError(1)
except MyInputError as err:
    print('error: {}'.format(err))
