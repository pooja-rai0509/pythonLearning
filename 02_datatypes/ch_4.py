# Tuples

masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1

print(f"Ratio of ginger: {ginger_ratio} and Cardamom: {cardamom_ratio}")

# swap

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"Ratio of ginger: {ginger_ratio} and Cardamom: {cardamom_ratio}")


# membership

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")

# value is case sensetive
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")


##########################
employee = ("Pooja", 25, "Developer")

print(employee)