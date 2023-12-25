s = eval(input("Enter a list: "))
positive = 0
zero = 0
negative = 0

for char in s:
    if char == 0:
        zero += 1
    elif char > 0:
        positive += 1
    else:
        negative += 1

print("No. of Positives: ", positive)
print("No. of Negatives: ", negative)
print("No. of Zeros: ", zero)