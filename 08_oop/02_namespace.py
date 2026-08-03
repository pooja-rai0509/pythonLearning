class chai:
    origin = "India"    #property

print(chai.origin)

chai.is_hot = True

print(chai.is_hot)

#creating objects from class chai

masala = chai()
print("Masala: ",masala.origin)
print(masala.is_hot)

masala.is_hot = False

print(chai.is_hot)
print(masala.is_hot)

masala.flavor = "Ginger"
print(masala.flavor)