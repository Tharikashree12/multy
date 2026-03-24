try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter second denominator: "))
    print("Result: " , a / b)
except ZeroDivisionError:
    print("Enter : Cannot divide by zero.")
    