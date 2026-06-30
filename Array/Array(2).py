from array import *

val=array('i',[1,2,3,4,5,6])

copyarray=array(val.typecode,(x for x in val))

for i in range(0,len(copyarray)):
    print(copyarray[i],end=',')
print("\n")


#pop(delete the index element)
val.pop(4)#without index last elemt will be poped
for i in range(0,len(val)):
    print(val[i],end=',')

print("\n")

#remove(delete the index of the given element)
val.remove(2)
for i in range(0,len(val)):
    print(val[i],end=',')

print("\n")

#Slicing
a=val[1:4]
for i in range(0,len(a)):
    print(a[i],end=",")

print("\n")

#Slicing
a=val[::-1]
for i in range(0,len(a)):
    print(a[i],end=",")