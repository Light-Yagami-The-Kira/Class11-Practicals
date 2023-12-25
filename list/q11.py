s = eval(input("Enter a list: "))
a = sorted(s)
largest = a[-1]
largest_occurence = a.count(largest)

print("Second Largest Element: ", a[-largest_occurence-1])