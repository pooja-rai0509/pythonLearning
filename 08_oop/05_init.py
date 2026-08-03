class chaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type}"


order = chaiOrder("Masala", 100)
print(order.summary())

order_two = chaiOrder("Ginger", 150)
print(order_two.summary())

class Emp:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello ",self.name)


emp = Emp("Pooja")
emp.greet()

emp2 = Emp("Ram")
Emp.greet(emp2)

emp3 = Emp("Sunny")
emp3.greet()