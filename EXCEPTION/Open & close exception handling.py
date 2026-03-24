try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("Error. File not found")
finally:
    try:
        f.close()
        print("File closed sucessfully")
    except:
        print("File was not opened")
        