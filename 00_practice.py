#Instance Method
class Employee:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello", self.name)

emp = Employee("Pooja")
emp.greet()

#Static Method
class calc:
    @staticmethod
    def add(a, b):
        return a+b

# no obj
print(calc.add(10,20))
#or
# with obj
added = calc()
num = added.add(10,20)
print(num)

#Class Method
class Emp:
    def __init__(self, name):
        self.name = name

    company = "Google"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

emp1 = Emp("Pooja")
emp2 = Emp("Ram")
print(emp1.name)
print(emp1.company)
print(emp1.company)
print(Emp.company)
Emp.change_company("IBM")
print(emp1.company)
print(emp1.company)
print(Emp.company)

#factory method or alternative constructor
class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))

emps = Employees.from_string("Pooja-50000")
print(emps.name)
print(type(emps.name))
print(emps.salary)
print(type(emps.salary))

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance is ", self.__balance)

account = BankAccount(10000)
account.deposit(5000)
account.show_balance()
account.deposit(6500)
account.show_balance()
#print(account.__balance)   #can't access as its protected

#Inheritance
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def sound(self):
        print("Barking")

dog = Dog()
dog.eat()
dog.sound()

#Polymorphism
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = Dog()
animals.sound()
animals = Cat()
animals.sound()
#----OR-----
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()

#Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Dog")

dog = Dog()
dog.sound()
# dog = Animal()
# dog.sound()

# proprty decorator - getter & setter
class getSetEmployee:
    def __init__(self, name):
        self._name = name   # store real value in _name so that to escape from recursion

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != "":
            self._name = value
        else:
            print("Name cannot be blank")

    @name.deleter
    def name(self):
        print("Deleting name")
        del self._name
        print("Name deleted")

getseEmp = getSetEmployee("Pooja")
print(getseEmp.name)
getseEmp.name = "Ram"
print(getseEmp.name)
getseEmp.name = ""
print(getseEmp.name)
del getseEmp.name
# print(getseEmp.name)  not exist any name