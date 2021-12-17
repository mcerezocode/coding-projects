# Title: Calculator
# Author details: Author: Max Cerezo, Contact details: maxcerezo.code@gmail.com
# Script and data info: This script requests two numbers and asks the user what to do with them.  

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
oper = str(input("Please choose 'add, subtract, multiply, divide: "))

if oper == "add":
    sum = (num1 + num2)
    print(sum)
elif oper == "subtract":
    sum = (num1 - num2)
    print(sum)
elif oper == "multiply":
    sum = (num1 * num2)
    print(sum)
elif oper == "divide":
    sum = (num1 / num2)
    print(sum)
else:
    print("Please choose from the following options.  Try again.  Thank you.")
