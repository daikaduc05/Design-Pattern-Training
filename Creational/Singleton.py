class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self,name):
        self.name = name   

s1 = Singleton("duc")
s2 = Singleton("hoang")
print(s2.name)  
print(s1 is s2)
