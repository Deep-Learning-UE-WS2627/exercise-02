#exercise 2 step 3
print("Exercise 2 Step 3")
print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
print("Sum: " + str(num1+num2))
print("Product: " + str(num1*num2))
#exercise 2 step 4
print("Exercise 2 Step 4")
print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
print ("Enter Operator a = Addition or m = Multiplication")
Operation = str(input())
if Operation == "a":
    print("Sum: " + str(num1+num2))
elif Operation == "m":
    print("Product: " + str(num1*num2))
elif Operation != "a" and Operation != "m": 
    print("Invalid Operator")