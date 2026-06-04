chai_type = "Ginger chai"
customer_name = "Pooja"

print(f"Oredr for {customer_name} : {chai_type}")

chgai_description = "Aromatic and Bold"
print(f"First word: {chgai_description[0:8:1]}") 
print(f"First word: {chgai_description[0:8:2]}")
print(f"First word: {chgai_description[0:8:3]}")

# 1 means every character, 2 means every 2nd character...
# [index_no (from which index to start optional): upto no. of characters: no. of skips after char(optional)]

print(f"First word: {chgai_description[:8]}")
print(f"First word: {chgai_description[10:]}")
print(f"First word: {chgai_description[::-1]}")

label_chai = "Chai Spécial"
encoded_label = label_chai.encode("utf-8")
print(f"Non-Encoded label: {label_chai}")
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")

name = "pooja"
name = "R" + name[1:]
print(name)

data = name.encode("utf-8")
print(data)