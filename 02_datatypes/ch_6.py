essential_spices = {"cardamnom", "ginger", "cinnamon"}
optional_spice = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spice
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spice
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spice
print(f"Only in essential spices: {only_in_essential}")

print(f"Is cloves in essential spices? {"cloves" in optional_spice}")

# types of each data types
name = "Pooja"
print(type(name))

name1 = ("Pooja")
print(type(name1))

name2 = ("Pooja",)
print(type(name2))

name3 = {"Pooja"}
print(type(name3))

name4 = ["Pooja"]
print(type(name4))