enames=["Rahul","Sonai","Priyainka"]    #list 
eids=(101,102,103,104)      #tuple
uids={10,11,12,13,14}    #set
emp={
    'eid':101,
    'ename':'Rahul'
}
range_Value=range(100)
ename="Rahul Gandhi"

print('Rahul' in enames) #True

"""list=[10,20,30,250]  #immutable
b=bytes(list)
b[1]=44
print(40 in b)
print(40 not in b)"""

ba=bytearray([10,20,30,25,40,250]) #mutable
print(type(ba))
ba[3]=254
print(40 in ba)
print(70 not in ba)