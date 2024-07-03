import mypackage


class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"
        self._private_attribute = "I am private"

    def public_method(self):
        """
        公共方法，可以从类外部访问
        """
        print("This is a public method.")
        self._private_method()
        self.__super_private_method()

    def _private_method(self):
        """
        内部方法，不建议从类外部访问
        """
        print("This is a private method.")

    def __super_private_method(self):
        """
        双下划线，名称重整，内部方法，无法从类外部访问
        """
        print("This is a super private method.")


# 创建 MyClass 类的实例
obj = MyClass()

obj.public_method()
obj._private_method()

mypackage.function1()
mypackage.function2()
# 打印包级别的变量
print(mypackage.__version__)
