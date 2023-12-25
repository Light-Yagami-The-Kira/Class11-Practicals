n = int(input("Enter number of elements: "))
t = tuple()
for i in range(n):
    e = int(input("Enter a numeber: "))
    t = t + (e,)

print(t)