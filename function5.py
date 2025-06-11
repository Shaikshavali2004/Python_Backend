a=18
def add():
    print("Addition")

print(type(a))    #Output: <class 'int'>
print(id(add))
print(type(add))   #Output: <class 'function'>
print(type(add())) #Output: NoneType