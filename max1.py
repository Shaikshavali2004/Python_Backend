# 19.Print max numbers in given 3 numbers-using Ternary Operator?


a = int(input())
b = int(input())
c = int(input())

max_num = a if a > b and a > c else(b if b > c else c)
print("The Maximum number is:",max_num)