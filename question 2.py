from numpy import *

arr=array([2000,3,500,6,13,900])
#calculate sum of array
sum=0
for i in range (0,len(arr)):
    sum+=arr[i]

print(sum)

print("\n")


#check if array is sorted
is_sorted=True
for i in range (0,len(arr)-1):
    if arr[i]>arr[i+1]:

        is_sorted=False
        break

print(is_sorted)
print("\n")

#code to find second largest number in the array

largest=arr[0]
second_largest=-float('inf')

for i in range(1,len(arr)):
    if arr[i]>largest:
        second_largest = largest
        largest=arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
     second_largest = arr[i]
        
print(largest)
print(second_largest)