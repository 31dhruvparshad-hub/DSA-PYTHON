from numpy import *
#no need to mention typecode and it also adjust itself with float and integer
val=array([1,2,3,4])#provides facility of heterogenous array

for x in val:
    print(x,end=",")
print("\n")


#linspace
ved=linspace(10,20,5)#divides number from 10 to 20 divided in to 5 parts
for x in ved:
    print(x,end=",")
print("\n")


#arange(here it creates a armthmatic progressio with common difference 5 )
v=arange(10,20,2)#remember here 20 is not included
for x in v :
    print(x,end=",")