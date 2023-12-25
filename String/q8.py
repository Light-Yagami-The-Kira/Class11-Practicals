s = input("Enter a string: ")

words = s.split()

for w in words:
    if w[0][0] in 'aA':
        print(w)