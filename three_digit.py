#9.Program to check if a number is a 3-digit number or not?

n1 = input("Enter any digits: ")              # Intialization statement

if n1.isdigit() and 100 <= int(n1) <=999:     # conditional statement
    print("It is a three digit number")       # print statement

else:
    print("It is not a three digit number")

