s = eval(input("Enter a list: "))
ctr = 0
for char in s:
    if len(char) >= 2 and char[0] == char[-1]:
        ctr += 1

print("no. of strings: ",ctr)