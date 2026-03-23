def naturalnum(n):
    print("Natural numbers series:")
    for i in range(1, n+1):
        print(i,end=" ")
    print()
def evennum(n):
    print ("Even numbers series:")
    for i in range(2,n+1,2):
        print(i,ends=" ")
    print()
def oddnum(n):
    print("Odd Numbers Series:")
    for i in range(1, n+1, 2):
        print(i, end=" ")
    print()
def fibonacci(n):
    print("Fibonacci number series:")
    a,b=0,1
    for i in range(n):
        print(a,ends=" ")
        a,b=b.a+b
    print()
print("1.Natural numbers")
print("2.Even numbers")
print("3.Odd numbers")
print("4.Fibonacci numbers")

choice = int (input("Enter your choice: "))
n = int(input("Enter the limit: "))
if choice == 1:
    Natural(n)
elif choice == 2:
    Even(n)
elif choice == 3:
    Odd(n)
elif choice == 4:
    fibonacci(n)
print ("Invalid choice")
