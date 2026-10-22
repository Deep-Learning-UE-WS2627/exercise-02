while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter operation (+ or *): ")
    operation = input()
    if operation in ["+", "add", "addition"]:
        print("Result: " + str(num1 + num2))
    elif operation in ["*", "multiply", "multiplication"]:
         print("Result: " + str(num1 * num2))

    print("Do you want to continue? (y/n): ")
    continue_calc = input()
    if continue_calc.lower() not in ["y", "yes"]:
     break
