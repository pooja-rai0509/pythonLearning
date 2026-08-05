def process_order(item, quantity):
    try:
        price = {"masala" : 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not in menu")
    except TypeError:
        print("Quantity must be in numbert")

process_order("ginger", 2)
process_order("masala", "two")