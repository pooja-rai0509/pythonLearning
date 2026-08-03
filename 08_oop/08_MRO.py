# Method Resolution Order

class A:
    label = "A : Base class"

class B(A):
    #label = "B : Masala Blend"
    pass

class C(A):
    #label = "C : Herbal Blend"
    pass

class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)
print(D.mro())