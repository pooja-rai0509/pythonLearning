class chaiCup:
    size = 150
    
    def describe(self):
        return f"A {self.size} ml chai cup"


cup = chaiCup()
print(cup.describe())
print(chaiCup.describe(cup))

cup_two = chaiCup()
cup_two.size = 200
print(cup_two.describe())
print(chaiCup.describe(cup_two))
