s = eval(input("Enter a list: "))
n = int(input("Enter the number to multiply: "))
for i in range(len(s)):
    s[i] *= n

print(s)