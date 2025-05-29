#7. Write a program to find the biggest of given 2 numbers from the command prompt?
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 > num2:
    print("The first number is bigger")

elif num1 == num2:
    print("The both numbers are equal")

else:
    print("The second number is bigger")