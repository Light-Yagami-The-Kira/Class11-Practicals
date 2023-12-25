s = eval(input("Enter a list: "))
temp = []
for elem in s:
    if elem not in temp:
        print(elem, "--->", s.count(elem))
        temp.append(elem)