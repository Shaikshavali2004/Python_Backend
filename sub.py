#Subtraction of multiple numbers
a  = int(input())
b = int(input())
c = int(input())
sub = a-b+c
print("The result is: ",sub)

# Another way to subtract multiple numbers
n1  = int(input())
n2 = int(input())
n3 = int(input())
def subtract_numbers(n1, n2, n3):
    return n1 - n2 - n3
print("The value is: ",subtract_numbers(n1, n2, n3))
