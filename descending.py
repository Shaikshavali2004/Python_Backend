#15.Program to print given 3 numbers in descending order?

n1=int(input())
n2=int(input())
n3=int(input())
numbers=[n1,n2,n3]
numbers.sort(reverse=True)
print("The numbers in descending order",numbers)