class Dog:
    def __init__(self, name, age):
        self.name = name  # 实例变量
        self.age = age  # 实例变量

    def bark(self):
        # return f"{self.name} is barking."
        return "{} is barking.".format(self.name)


# 创建一个对象
my_dog = Dog("Buddy", 3)

print(my_dog.name)  # 输出：Buddy
print(my_dog.bark())  # 输出：Buddy is barking.


class Cat:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def common_species(cls):
        return cls.species

    @staticmethod
    def is_domestic():
        return True


print(Cat.common_species())  # 输出：Canis lupus familiaris
print(Cat.is_domestic())  # 输出：True


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving."


class Pig(Animal):
    def bark(self):
        return f"{self.name} is oink."

    # 内置方法，魔术方法
    def __str__(self):
        return f"Dog(name={self.name})"


my_pigf = Pig("Buddy")
print(my_pigf.move())  # 输出：Buddy is moving.
print(my_pigf.bark())  # 输出：Buddy is barking.
print(my_pigf.__str__())  # 输出：Buddy is barking.


class Chicken:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


my_chicken = Chicken("Buddy", 3)
print(my_chicken.name)  # 输出：Buddy
my_chicken.age = 4
print(my_chicken.age)  # 输出：4

import sys

print("sys.prefix:", sys.prefix)
print("sys.base_prefix:", sys.base_prefix)
print("Using virtual environment:", sys.prefix != sys.base_prefix)
