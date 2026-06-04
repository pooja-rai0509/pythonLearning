# to import any  system packages
import sys
from fractions import Fraction
from decimal import Decimal as d  # typecast
# these can deal with huge numbers

# Data Types

# Number
# Integer

black_tea_grams = 14
ginger_grams = 3

#add
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

# subtract
remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")

# divide
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

# floor division
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot {bags_per_pot}")

# remaindeer
tota_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = tota_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods {leftover_pods}")

# poer/exponent
base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Scaled flavoe strength {powerful_flavor}")

# _ for readability
total_tea_leaves_harvested = 1_000_000_000
print(f"total leaves harvested {total_tea_leaves_harvested}")



# boolean 

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling  # upcasting
print(f"Total actions: {total_actions}")

milk_present = "0"
# any value present will be true
# 0 or none will be false
print(f"Is there milk? {bool(milk_present)}")

# logical operator (and, or, not)

water_hot = True
tea_added = False
can_serve = water_hot and tea_added
print(f"can server chai? {can_serve}")



# Real numbers - float

ideal_temp = 95.5
current_temp = 95.49999999999

print(f"Ideal temp {ideal_temp}")
print(f"Current temp {ideal_temp}")
print(f"Difference temp {ideal_temp - current_temp}")

print(sys.float_info)