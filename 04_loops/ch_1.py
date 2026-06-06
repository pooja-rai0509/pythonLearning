# loops

# A tea stall owner has a diugital token display
# for every customer in line, a token number is printed and chai is served.
# Task:
# Use a for loop to generate token nos from 1 to 10 using range()
# Print : "Serving chai to token #[number]"

for token in range(1,11):
    print(f"Serving chai to token #{token}")


# A chai shop makes tea in batches in 15 min
# You want to simalate 4 batches
# Task:
# Use range() to simulate batch numbers
# Print: "Preparing chai for batch #[number]"

for batch in range(1,5):
    print(f"Preparing chai for batch #{batch}")


# You recieve a list of names for chai orders 
# The goal is to print out the ordser queue
# Task:
# Use a list of names
# Print: "Order ready for [name]"

names = ["Pooja", "Aman", "Becky", "Carlos"]

for name in names:
    print(f"Order ready for {name}")


# You're creating a tea menu board
# Each  must be numbered
# Task:
# Use enumerate() to print menu items with numbers

menu = ["Green", "Leoon", "Spiced", "Mint"]

for idx,m in enumerate(menu, start=1):
    print(f"Menu item is {idx,m}")


# You're preparing an order summary with customer names and their total bills
# Task:
# Use two lists : one for names & one for bills
# Print: "[Name] paid [amount]"

names = ["Pooja", "Meera", "Sam"]
bills = [50, 70, 150]

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rs")


# You want to simalate tea heating 
# It starts at 40 c and boils at 100 c
# Task:
# Use a while loop
# Increase temperature by 15 until it reaches or exeeds 100
# Print each temperature step

temp = 40

while temp < 100:
    print(f"Temperature now : {temp}")
    temp+=15

print(f"Tea is ready to boil")


# Some chai flavors are out of stock
# You want to skip those & stop entirely is someone requests a restricted flavor
# Task: 
# Skip if flavor is "Out of stock"
# Break if flavor is "Discontinued"

flavors = ["ginger", "out of stock", "lemon", "discontinued", "Tulsi"]

for flavor in flavors:
    if flavor == "out of stock":
        print(f"Flavor out of stock {flavor}")
        continue
    if flavor == "discontinued":
        print(f"Flavor discontinued {flavor}")
        break
    print(f"Flavor available {flavor}")

print("Outside of loop")


# for_else - else runs when condition not meets otherwise not runs

staff = [("Amit", 20), ("Zara", 17), ("Raj",15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
    
else:
    print("No one is eligible to manage the staff")


