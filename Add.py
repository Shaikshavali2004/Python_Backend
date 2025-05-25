#Addition of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def add_numbers(num1, num2):
     return num1 + num2
print("The sum of the two numbers is: ", add_numbers(num1, num2))

#Another way to add two numbers
def add_numbers_alternative():
     num1 = int(input("Enter first number: "))
     num2 = int(input ("Enter second number: "))
     return num1 + num2
print("The sum of the two numbers is: ", add_numbers_alternative())

# Using a lamda function to add two numbers
add_numbers_lambda = lambda x, y: x + y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum of the two numbers is: ", add_numbers_lambda(num1, num2))

# Using a function to add two numbers with default values
def add_numbers_with_defaults(num1=10, num2=19):
      return num1 + num2
print("The sum of the two numbers is: ", add_numbers_with_defaults(num1, num2))

# simple program to add two numbers
a = 10
b =  20
c = a+b
print(c)

