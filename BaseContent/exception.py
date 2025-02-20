# var1 = 10 / 0
# Traceback (most recent call last):
#   File "/Users/hrenxiang/Documents/development/python-workspace/PythonDemo/BaseContent/./exception.py", line 1, in <module>
#     var1 = 10 / 0
# ZeroDivisionError: division by zero

# try:
#     var1 = 10 / 0
# except ZeroDivisionError as e:
#     print(str(e))


# class MyInputError(Exception):
#     """自定义异常类型"""
#
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return "{} is invalid input".format(repr(self.value))
# try:
#     raise MyInputError(1)
# except MyInputError as err:
#     print('error: {}'.format(err))


# def wz():
#     try:
#         1 / 0
#     except Exception as e:
#         print("wz函数的异常处理：", e)
#     print("出错不影响外面的输出")
# def run():
#     try:
#         wz()
#         print("无影响")
#     except Exception as e:
#         print("run函数的异常处理：", e)
# run()
# 输出 wz函数的异常处理： division by zero
#      出错不影响外面的输出
#      无影响


# def wz2():
#     1 / 0
#     print("出错不影响外面的输出")
#
#
# def run2():
#     try:
#         wz2()
#         print("无影响")
#     except Exception as e:
#         print("run函数的异常处理：", e)
#
#
# run2()
# # 输出run函数的异常处理： division by zero
