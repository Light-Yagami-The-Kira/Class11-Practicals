s = input("Enter a string: ")
words = s.split()
smallest_words = [words[0]]

for w in words[1::]:
    if len(w) == len(smallest_words[0]):
        smallest_words.append(w)
        
    if len(w) < len(smallest_words[0]):
        smallest_words = [w]

print("Smallest Words are: ", ",".join(smallest_words))