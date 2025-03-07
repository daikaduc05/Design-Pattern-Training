from abc import ABC, abstractmethod
class LapTop(ABC):
    @abstractmethod
    def __init__(self):
        pass

class MacBook(LapTop):
    def __init__(self):
        print("MacBook is created")

class Dell(LapTop):
    def __init__(self):
        print("Dell is created")

class LaptopFactory():
    register = {}
    def register_laptop(self, name, laptop):
        self.register[name] = laptop
    def create_laptop(self, name):
        return self.register[name]()


laptop_factory = LaptopFactory()
laptop_factory.register_laptop("MacBook", MacBook)
laptop_factory.register_laptop("Dell", Dell)
laptop_factory.create_laptop("MacBook")
laptop_factory.create_laptop("Dell")