#12.Program to print the least/smallest number in given two numbers?
n1 = int(input("Enter n1 value: "))
n2 = int(input("Enter n2 value: "))

if n1 < n2:
    print(f"{n1} is the smallest number.")

elif n1 == n2:
    print(f"{n1} and {n2} are equal numbers.")

else:
    print(f"{n2} is the smallest number.")