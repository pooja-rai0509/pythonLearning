class TeaLeaf:
    def __init__(self, age):
        self._age = age

    # getter
    @property
    def age(self):
        return self._age + 2

    # setter
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self.age = age
        else:
            raise ValueError("Tea leag age must be between 1 & 5yrs")


leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 4
print(leaf.age)