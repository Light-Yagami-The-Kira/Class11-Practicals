import copy
s = eval(input("Enter a list: "))
shallow_copy = s
deepcopy = copy.deepcopy(s)

## VERFICATION
s[0] = None
print(shallow_copy)  ## VALUE WILL ALSO CHANGE
print(deepcopy)      ## VALUE WONT CHANGE
