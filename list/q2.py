s = eval(input("Enter a list: "))

s[0],s[-1] = s[-1],s[0]

print(s)