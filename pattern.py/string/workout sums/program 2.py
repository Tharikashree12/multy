s = input("Enter a string: ")
result = ""
for i in range(len(s)):
    if i % 2 == 1:
        result += "*"
    else:
        result += s[i]
print("Modified string:", result) 
