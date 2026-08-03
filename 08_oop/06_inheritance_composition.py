class BaseChai:
    def __init__(self, type_):
        self.type_ = type_

    def prepare(self):
        print(f"Preparing {self.type_} chai...")

#Inherit class    
class Masalachai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

#composition class
class chaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type_} Chai in the shop")
        self.chai.prepare()

#inherit + composition    
class FancyChaiShop(chaiShop):
    chai_cls = Masalachai


shop = chaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()