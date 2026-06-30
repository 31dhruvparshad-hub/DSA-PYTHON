from numpy import *

arr=array([2000,3,500,6,13,90])
#create a maximum function
maximum=arr[0]
for i in range(0,len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]

print(maximum)
print("\n")

#create a minimum function
min_arr=arr[0]
for i in range(0,len(arr)):
    if arr[i]<min_arr:
        min_arr=arr[i]

print(min_arr)

#code to count iterations of a number 
arr = [5, 2, 5, 7, 5, 1]
x=int(input("Enter the number whose iterations need to be Counted: "))
count=0
for i in range(0,len(arr)):
    if arr[i]==x:
        count+=1

print(count)