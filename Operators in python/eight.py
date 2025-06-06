ba=bytearray([10,20,30,25,40,250]) #mutable
print(type(ba))
ba[3]=254 # Item Assignment possible , Because Bytearray is Mutable object.
print(ba)
print(40 in ba)
print(70 not in ba)

for i in ba:
    print(i)
    
