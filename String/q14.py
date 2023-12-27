s = input("Enter a string: ")
unique_char = ""
for i in s:
    if i not in unique_char:
        unique_char = unique_char + i
for c in unique_char:
    if c == " ":
        print("blank space","---->",ord(c))
    else:
        print(c,"--->",ord(c))

        