fav_chais = ["Masala chai", "Green tea", "Masala chai", "Lemon tea", "Green tea", "Elaichi chai"]

unique_chai = {chai for chai in fav_chais}

print(unique_chai)


reciepes = {
    "Masala chai" : ["ginger", "cardamom", "clove"],
    "Elaichi chai" : ["cardamom", "milk"],
    "Spicy chai" : ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingreients in reciepes.values() for spice in ingreients}

print(unique_spices)