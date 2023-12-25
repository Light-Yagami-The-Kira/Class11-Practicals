s = input("Enter string: ")
S = ""

for char in s:
    if char.isupper():
        char = char.lower()
    elif char.islower():
        char = char.upper()
    else:
        pass
    S = S + char

print(S)