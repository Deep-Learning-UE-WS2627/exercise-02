
while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    print("Do you want to add (a) or multiply (m)?")
    a_or_m = input()
    if a_or_m in ['a', 'add', 'addition']:
        print("Sum: " + str(num1+num2))
    elif a_or_m in ['m', 'multiply', 'multiplication']:
        print("Product: " + str(num1*num2))

    main = input("Do you want to do another Operation?")

    if main in ['Y','y','Yes','yes']:
        continue
    elif main in ['N','n','No','no']:
        print("Alrighty. Have a good day!")
        break