schleife = True
while schleife:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter operator - either '+' or '*' (*G Jones starts to play in the background*)")
    inp = input()
    if (inp=="+") or (inp == "add") or (inp == "addition"):
        print("Sum: " + str(num1+num2))
    elif (inp=="*") or (inp=="multi") or (inp=="multiplication"):
        print("Product: " + str(num1*num2))
    else:
        print("please enter a valid operator next time")

    print("Do you want to do another calculation?")
    if (input()==""):
        schleife = False