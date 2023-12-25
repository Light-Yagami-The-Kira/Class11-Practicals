while True:
    print("-------String---Menu-------")
    print("1. len() 2.title() 3.lower() 4.upper() 5.Count() 6.find()")
    print("7.index() 8.endswith() 9.startswith() 10.isalnum() 11.islower() 12.isupper()")
    print("13.lstrip() 14.rstrip() 15.replace() 16.join() 17.partition() 18.split()")

    U = input("Enter Menu: ")
    s = input("Enter a string: ")
    if U == '1':
        print(len(s))
    elif U == '2':
        print(s.title())
    elif U == '3':
        print(s.lower())
    elif U == '4':
        print(s.upper())
    elif U == '5':
        e = input("Enter elem to count: ")
        print(s.count())
    elif U == '6':
        e = input("Enter elem to find: ")
        print(s.find(e))
    elif U == '7':
        e = input("Enter elem to find: ")
        print(s.index(e))
    elif U == '8':
        e = input("Enter the element to check: ")
        print(s.endswith(e))
    elif U == '9':
        e = input("Enter the element to check: ")
        print(s.startswith(e))
    elif U == '10':
        print(s.isalnum())
    elif U == '11':
        print(s.islower())
    elif U == '12':
        print(s.isupper())
    elif U == '13':
        print(s.lstrip())
    elif U == '14':
        print(s.rstrip())
    elif U == '15':
        oldstring = input("Enter oldstring: ")
        newstring = input("Enter newstring: ")
        print(s.replace(oldstring,newstring))
    elif U == '16':
        sepa = input("Enter a separator: ")
        print(sepa.join(s))
    elif U == '17':
        sepap = input("Enter Partition separator: ")
        print(s.partition(sepap))
    elif U == '18':
        sepas = input("Enter splitting separator: ")
        print(s.split(sepas))
    else:
        print("Wrong Input...")