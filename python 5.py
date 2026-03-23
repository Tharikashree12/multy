a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
# First fist miximum between a and b 
max1 = a if a > b else b
# Then compare the result with c
maximum = max1 if max1 >c else c
# Display the maximum number
print("Maximum number is:", maximum)
