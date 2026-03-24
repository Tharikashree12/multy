try:
    f= open("sample.text." "w")
    f.write("Hello PYTHON")
except Exception:
    print("Error while writing file")
finally:
    f.closed()
    print("File closed sucessfully")
    