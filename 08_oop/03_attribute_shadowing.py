class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.cup = "small"

cutting.temperature = "warm"
print("After changing, ",cutting.temperature)
print("Direct look in class, ",Chai.temperature)
print(cutting.cup)

del cutting.temperature
print(cutting.temperature)
