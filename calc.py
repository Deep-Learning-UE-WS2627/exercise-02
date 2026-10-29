
while True:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    operation = input("Enter operation (add/multi): ").lower().strip()

    if operation == "add" or operation == "addition":
        print("Sum:", num1 + num2)

    elif operation == "multi" or operation == "multiplication":
        print("Product:", num1 * num2)

    else:
        print("Invalid operation!")

    again = input("Do you want to continue? (yes/no): ").lower().strip()

    if again not in ["yes", "y", "ja", "j"]:
        print("Goodbye!")
        break
