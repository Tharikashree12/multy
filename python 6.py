a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number:"))
# First fist minimum between a and b 
min1 = a if a < b else b
# Then compare the result with c
minimum = min1 if min1 < c else c
# Display the minimum number
print("Minimum number is:", minimum)
