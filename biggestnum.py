# 13.Program to print the greatest number in given three numbers?

n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))
n3 = int(input("Enter third value: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the greatest number")

elif n2 > n1 and n2 > n3:
    print(f"{n2} is the greatest number")

else:
    print(f"{n3} is the greatest number")