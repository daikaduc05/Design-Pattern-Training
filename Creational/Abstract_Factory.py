from abc import ABC,abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_chair(self):
        pass
    @abstractmethod
    def create_product_sofa(self):
        pass
    @abstractmethod
    def create_product_table(self):
        pass

class Chair(ABC):
    @abstractmethod
    def __init__(self):
        pass

class Sofa(ABC):    
    @abstractmethod
    def __init__(self):
        pass

class Table(ABC):
    @abstractmethod
    def __init__(self):
        pass

class MordernChair(Chair):
    def __init__(self):
        print("Mordern Chair is created")

class MordernSofa(Sofa):
    def __init__(self):
        print("Mordern Sofa is created")        

class MordernTable(Table):
    def __init__(self):
        print("Mordern Table is created")
    
class WoodenChair(Chair):
    def __init__(self):
        print("Wooden Chair is created")

class WoodenSofa(Sofa):
    def __init__(self):
        print("Wooden Sofa is created")

class WoodenTable(Table):
    def __init__(self):
        print("Wooden Table is created")    

class MordernFurnitureFactory(AbstractFactory):
    def create_product_chair(self):
        return MordernChair()
    def create_product_sofa(self):
        return MordernSofa()
    def create_product_table(self):
        return MordernTable()
    
class WoodenFurnitureFactory(AbstractFactory):
    def create_product_chair(self):
        return WoodenChair() 
    def create_product_sofa(self):
        return WoodenSofa()
    def create_product_table(self):
        return WoodenTable()    


def factory(factor : AbstractFactory):
    factor.create_product_chair()
    factor.create_product_sofa()
    factor.create_product_table()

factory(WoodenFurnitureFactory())