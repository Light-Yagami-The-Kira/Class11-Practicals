s = input("Enter string: ")
v = 0
for c in s:
    if c in 'aeiouAEIOU':
        v += 1

print("No. of vowels: ", v)
    