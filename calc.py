while True: 
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter 'add' for Addition or 'multi' for Multiplikation")
    operation = str(input())

    if operation == 'add':
        print("Sum:", num1 + num2)
    elif operation == 'multi':
        print("Product:", num1 * num2)
    else:
        print("Invalid selection.")


    again = input("Do you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        break
