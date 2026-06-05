# condition based task

# Creating a notification system for a smart kettlr
# It should remind the user only when the kettle has finished boiling.
# Task:
# A variable kettle_boiled = True
# If boiled, show "Kettle done! Time to make chai!"

kettle_boiled = False

if kettle_boiled:
    print(f"Kettle done! Time to make chai!")


# A local cafe wants a program thatb suggests a snack.
# If a customer asks for a cookie or samosa, it confirms the order.
# Otherwiuse, it says it's not available.
# Task:
# Take a snack input
# If its "cookies" or " samosa", confirm the order
# Else, show unavailabilty

snack = input("Enter your preferred snack: ").lower()
print(f"User said : {snack}")

availableSnack = ["cookie", "samosa"]

if snack == "cookie" or snack == "samosa":
    print("Order confirmed!")
else :
    print("Order is not available")

# or using membership test

if snack in availableSnack:
    print("Order confirmed!")
else :
    print("Order is not available")


# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.
# Task:
# Input: "small", "medium", "large"
# Small = rs 10, medium = rs 15, large = rs 20
# If invalid: show "Unknown cup size"

cup_size = input("Choose a cup size(small/medium/large) : ").lower()

if cup_size == "small":
    print("Price is 10 rs")
elif cup_size == "medium":
    print("Price is 15 rs")
elif cup_size == "large":
    print("Price is 20 rs")
else:
    print("Unknown cup size")
