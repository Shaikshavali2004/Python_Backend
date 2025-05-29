# 11.Program to print the greatest number in given two numbers?

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    #print("The greatest number is ",num1)
    print(f"{num1} is the greatest number.")

elif num1 == num2:
    print("Both are equal numbers")

else:
    #print("The greatest number is ",num2)
    print(f"{num2} is the greatest number.")