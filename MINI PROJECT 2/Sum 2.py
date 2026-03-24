try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        print("Login sucessful")
    elif username == "" or password == "":
        raise ValueError("Empty input not allowed")
    else:
        print("Invalid credentials")
except ValueError as e:
    print("Error:", e)
finally:
    print("Login process completed")
        
