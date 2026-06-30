from array import *

val=array('i',[1,2,3,4,5,6,7,8])
print(val)

#using for loop
for i in range(0,6):
    print(val[i],end=" ")
print('\n')
#using advanced for loop(better as in upper there is range hence if size of array increases it will not print all element)
for x in val:
    print(x,end=",")


#we can also do this by the normal for loop by calculating length of the array
print('\n')
y=len(val)
for i in range(0,y):
    print(val[i],end=",")

print('\n')
#For inserting float number in array(if we entere float in upper array it will give error as it's type code is )
ved=array('d',[2,3,4,5,7.5,8.5,4.4])

z=len(ved)
for i in range(0,z):
    print(ved[i],end=",")


print("\n")
#REVERSING THE ARRAY
val.reverse()
for i in range(0,y):
 print(val[i],end=",")
print("\n")
#Inserting in an array
ved.insert(1,50)
for i in range(0,len(ved)):
   print(ved[i],end=",")

#for appending use
print("\n")
ved.append(100)
for i in range(0,len(ved)):
   print(ved[i],end=",")

print("\n")
#for overiding the value of a particular index
ved[4]=50
print(ved[4])

