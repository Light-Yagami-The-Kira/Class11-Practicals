s = eval(input("Enter a list: "))
elem = eval(input("Enter the element to be removed: "))
n = int(input("Enter the nth occurence to be removed: "))
ctr = 0
for i in range(len(s)):
    if elem == s[i]:
        ctr += 1
    if ctr == n:
        del s[i]
        break
print(s)

