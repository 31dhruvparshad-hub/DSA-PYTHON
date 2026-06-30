from array import *
#taking input from user

arr=array('i',[])

n=int(input("Enter The Length of Array: "))

for i in range(0,n):
   arr.append(int(input(f"Enter {i} input: ")))

for x in arr:
   print(x,end=" ")

print("\n")

#Searching in an array

brr=array("i",[1,4,6,3,8,6,7])
i=brr.index(7)#it searches at what index is element 7 
print(i)