try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Choose operation: +, -, *, /")
    op=input("Enter operator: ")
    if op =="+":
        print("Result: ", num1 +num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input")
else:
    print("Calculation sucessful")
    
