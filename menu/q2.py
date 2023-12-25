while True:
    print("---------List----Menu------")
    print("1.len() 2.append() 3.extend() 4.insert() 5.sum() 6.count() 7.index()")
    print("8.remove() 9.pop() 10.reverse() 11.sort() 12.sorted() 13.min() 14.max()")

    L = eval(input("Enter a list: "))

    U = input("Enter Menu Number: ")

    if U == '1':
        print(len(L))
    elif U == '2':
        e = eval(input("Enter element"))
        L.append(e)
        print(L)
    elif U == '3':
        e = eval(input("Enter list: "))
        L.extend(e)
        print(L)
    elif U == '4':
        e = eval(input("Enter element: "))
        i = int(input("Enter the index: "))
        L.insert(i,e)
        print(L)
    elif U == '5':
        print(sum(L))
    elif U == '6':
        e = eval(input("Enter element: "))
        print(L.count(e))
    elif U == '7':
        e = eval(input("Enter element: "))
        print(L.index(e))
    elif U == '8':
        e = eval(input("Enter element to be removed: "))
        L.remove(e)
        print(L)
    elif U == '9':
        i = int(input("Enter index to be popped: "))
        L.pop(i)
        print(L)
    elif U == '10':
        L.reverse()
        print(L)
    elif U == '11':
        L.sort()
        print(L)
    elif U == '12':
        print(sorted(L))
    elif U == '13':
        print(min(L))
    elif U == '14':
        print(max(L))
    else:
        print("Wrong Input....")