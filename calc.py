while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter math operation: either '+' or '*', either 'addition' or 'multiplication'")
    operator = input()

    if (operator == "+") or (operator == "addition"):
        print("Sum: " + str(num1 + num2))
    elif (operator == "*") or (operator == "multiplication"):
        print("Product: " + str(num1 * num2))
    else:
        print("Use only '+', '*', 'addition' and 'multiplication'.")

    answer = input("Do you want to continue? Enter 'y' to continue: ").strip().lower()
    if answer not in ("y", "Y", "yes"):
        break