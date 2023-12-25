s = input("Enter a string: ")

largest_word = ""

words_list = s.split()

for word in words_list:
    if len(word) > len(largest_word.split(',')[0]):
        largest_word = word

        continue


    if len(word) == len(largest_word.split(',')[0]):
        largest_word = largest_word + "," + word

        continue


print("\nLargest Words are:", largest_word)