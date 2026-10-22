def main():
 print("Addition or Multiplication?")
 op = input()

 print("Enter number 1: ")
 num1 = int(input())
 print("Enter number 2: ")
 num2 = int(input())
 if op == "addition" or op == "add" or op == "Addition" or op == "Add":
  print("Sum: " + str(num1+num2))
 if op == "multiplication" or op == "mult" or op == "Multiplication" or op == "Mult":
  print("Product: " + str(num1*num2))
 else:
  print("Out of Range")
 print("Do you want to continue?y/n")
 yn = input()
 if yn == "y":
  main()

main()

