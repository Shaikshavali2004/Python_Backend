# 18.Print min numbers in given 3 numbers-using Ternary Operator?

a = int(input())
b = int(input())
c = int(input())

min_num = a if a < b and a < c else(b if b < c else c)

print("The Minimum number is:",min_num)