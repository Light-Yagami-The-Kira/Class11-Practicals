unique_words = ""
s = input("Enter a string: ")
words = s.split()
for i in words:
    if i not in unique_words:
        unique_words = unique_words + i + ","
print("Unique words are: ", unique_words[:-1])

