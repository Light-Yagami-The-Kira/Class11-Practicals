s = eval(input("Enter a list: "))
N = int(input("Enter N to find Nth largest element"))
a = sorted(s)

maxx = a[-1]
maxx_occurence = a.count(maxx)

for i in range(N-1):
    maxx = a[-1-maxx_occurence]

    maxx_occurence += a.count(maxx)


print(N,"th Largest number is: ", maxx)