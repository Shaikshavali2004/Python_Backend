# Write a program to find the biggest of given 3 numbers from the command prompt?

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the bigger number")

elif num2 > num1 and num2 > num3:
    print(f"{num2} is the bigger number")

else:
    print(f"{num3} is the bigger number")

