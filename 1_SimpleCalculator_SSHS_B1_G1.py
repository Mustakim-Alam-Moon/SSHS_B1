run = 1

while (run == 1):
    print ("press - 1/2/3/4/5/6 for addition/subtraction/multiplication/division/modulus/exponent ")

    choice = input("enter 1,2,3,4,5,6: ")

    a = int(input(" Enter your first number: "))
    b = int(input(" Enter your second number: "))

    if choice  in ("1","2","3","4","5","6"):
        add = a + b
        sub = a - b
        mul = a * b
        div = a / b
        mod = a % b
        exp = a ** b

    if  choice == "1" : 
        print (" The addition is :", add)
    elif  choice == "2":
        print (" The subtraction is :", sub)
    elif choice == "3" :
        print (" The multiplication is :", mul)
    elif choice == "4" :
        print (" The divide is :", div)
    elif choice == "5" :
        print (" The modulus is :", mod)
    elif choice == "6" :
        print (" The exponent is :", exp)
    else :
        print("You've entered wrong number")

    run = int(input("Press 1 to continue: "))
    print()