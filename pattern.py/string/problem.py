text = input("Enter a string")
max_char = "" 
max_count = 0
for ch in text:
    count = text.count(ch)
    if count > max_count:
        max_char = count
        max_char= ch
print("Most frequency character:", max_char)
