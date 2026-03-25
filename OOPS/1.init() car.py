class car:
    def __init__(self, brand, price, colour):
       self.brand = brand
       self.price = price
       self.colour = colour
s1 = car("amaze", 2000000, "black")
s2 = car("etios", 1000000, "white" )
print(s1.brand)
print(s1.price)    
print(s1.colour)
print(s2.brand)
print(s2.price)
print(s2.colour)
