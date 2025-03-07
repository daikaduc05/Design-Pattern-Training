class FlyWeightMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = (cls, args, frozenset(kwargs.items()))
        if key not in cls._instances:
            cls._instances[key] = super().__call__(*args, **kwargs)
        return cls._instances[key]

class Student(metaclass=FlyWeightMetaClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} {self.age}'

s1 = Student('duc', 20)
s2 = Student('hoang', 20)
print(s1 is s2)