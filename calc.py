while True:
    print("Enter number 1: ")
    num1 = int(input())

    print("Enter number 2: ")
    num2 = int(input())

    print("Enter operation (add or multi): ")
    operation = input()

    if operation == "add" or operation == "addition":
        print("Sum: " + str(num1 + num2))

    elif operation == "multi" or operation == "multiplication":
        print("Product: " + str(num1 * num2))

    print("Do you want to continue? (yes/no)")
    answer = input()

    if answer != "yes":
        break