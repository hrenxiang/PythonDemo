import yaml


class Monster(yaml.YAMLObject):
    yaml_tag = u'!Monster'

    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.ac,
            self.attacks)


yaml_load = yaml.load("""
--- !Monster
name: Cave spider
hp: [2,6] # 2d6
ac: 16
attacks: [BITE, HURT]
""", Loader=yaml.FullLoader)
print(yaml_load)
print(id(yaml_load))
print(type(yaml_load))

monster = Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])
print(monster)
print(id(monster))
print(type(monster))

dump = yaml.dump(Monster(name='Cave lizard', hp=[3, 6], ac=16, attacks=['BITE', 'HURT']))
print(dump)


# !Monster
# ac: 16
# attacks:
# - BITE
# - HURT
# hp:
# - 3
# - 6
# name: Cave lizard


class MyClass:
    pass


instance = MyClass()
print(type(instance))  # <class '__main__.MyClass'>
print(type(MyClass))  # <class 'type'>

print('=======================================================')


class Field:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def validate(self, value):
        raise NotImplementedError


class StringField(Field):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.name} must be a string')


class IntegerField(Field):
    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be an integer')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for key, value in attrs.items():
            print(" attrs: {}".format(attrs.items()))
            if isinstance(value, Field):
                value.name = key
                fields[key] = value
        attrs['_fields'] = fields
        print(" _fields: {}".format(fields))
        return super().__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for name, field in self._fields.items():
            print(" model init: {} --- {}".format(name, field))
            setattr(self, name, kwargs.get(name))

    def validate(self):
        for name, field in self._fields.items():
            value = getattr(self, name)
            field.validate(value)


class User(Model):
    name = StringField()
    age = IntegerField()


# 使用示例
user = User(name="Alice", age=30)
user.validate()  # 成功
