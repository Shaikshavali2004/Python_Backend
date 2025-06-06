eids = [101, 102, 103, 104]

print(101 in eids) # True
print(105 in eids) # False

enames = {'Casandra','Kajal','Vicky'}
print('Casandra' in enames) #True
ename='Jashnavi'
print('J' in ename) # True

range_value = range(5)
print(10 in range_value) #False

set={10,20,30,40}
print(10 in set)
print(50 in set)

list=[10,20,30,250]
b=bytes(list)
print(40 in b)
print(40 not in b)

emp={"eid":101, "ename":"Rahul"}
print("eid" in emp)