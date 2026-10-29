while True:

    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter math operation: either 'add' or 'multi', either 'addition' or 'multiplication'")
    operator = input()

    if (operator == "add") or (operator == "addition"):
        print("Sum: " + str(num1+num2))
    elif (operator == "multi") or (operator == "multiplication"):
        print("Product: " + str(num1*num2))

    print("Continue (Y/N)? ")
    cont = input()
    if cont == "N" or cont == "n":
        break
        