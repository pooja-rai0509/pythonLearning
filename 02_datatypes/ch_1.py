#immutable example
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

print(f"Id of 2 : {id(2)}")
print(f"Id of 12: {id(12)}")

#mutable example
spice_mix = set()
print(f"Initial Spice mix id: {id(spice_mix)}")
print(f"Initil Spice mix: {spice_mix}")

spice_mix.add("ginger")
spice_mix.add("cardamom")
print(f"After Spice mix id: {id(spice_mix)}")
print(f"After Spice mix: {spice_mix}")