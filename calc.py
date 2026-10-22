while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter Your operator of choice: '+' or '*', 'add' or 'multi', 'addition' or 'multiplication'")
    operator = input()

    if (operator == "+") or (operator == "add") or (operator == "addition"):
        print("Sum: " + str(num1 + num2))
    elif (operator == "*") or (operator == "multi") or (operator == "multiplication"):
        print("Product: " + str(num1 * num2))
    else:
        print("Only '+', '*', 'add', 'multi', 'addition' and 'multiplication' are valid inputs.")

    answer = input("Do you want to try again? (yes/no): ").strip().lower()
    if answer not in ("y", "yes", "j", "ja"):
        break