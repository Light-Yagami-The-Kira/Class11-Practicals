s = input("Enter a string: ")

c = 0

for a in s:
    if a.isnumeric():
        c += 1

print("No. of digits: ", c)