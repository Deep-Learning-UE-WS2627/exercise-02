def calc ():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    choice = input("Choose add or mul\n")

    if choice in("sum", "add", "addition", "addieren", "+"):
        print("Sum: " + str(num1 + num2))

    if choice in ("product", "mul", "multi", "multiplication", "multiply", "multiplizieren", "*"):
        print("Product: " + str(num1 * num2))

        
    choice = input("Start over? y/n\n")

    if choice == "y":
        calc()
        
    if choice == "n":
        return
            
calc()

            