"""l1=[]
l2=list()
l3=[10,20.5,"Rahul",True,20.5,10]

print(l1)
print(l2)
print(l3)
print(l3[3])
print(l3[2])"""
#print(l3[8]) #IndexError

"""eids=[101,102,103,104,105]
for eid in eids:
    print(eid)"""

eids=[101,102,103,104,105]
i=0
while i<=len(eids)-1:
    print(eids[i])
    #i=i+1
    i+=1

print(type(eids))