# value = 15
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# Using Walrus operator (:=)

value = 13 

if remainder:= value% 5:
    print(f"Not divisible, remainder is {remainder}")


available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size : ").lower()) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")


flavors = ["masala", "ginger", "mint", "lemon"]

print("Available flavors: ", flavors)

while (flavor := input("choose a flavor: ").lower()) not in flavors:
    print(f"{flavor} is not available")

print(f"Chose {flavor} chai")