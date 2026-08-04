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