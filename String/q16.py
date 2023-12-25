s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1_wordList = s1.split()
s2_wordList = s2.split()

for I in s1_wordList:
    for II in s2_wordList:
        if I.lower() == II.lower():
            print(I, "and", II, "are same.")

            