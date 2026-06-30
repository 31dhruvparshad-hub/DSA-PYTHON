from numpy import *

arr=array([4, 7, 2, 9, 5])
target=int(input("Enter Number: "))
found=False
for i in range(0,len(arr)):
    if arr[i]==target:
        print(i)
        found = True
if not found:
    print(-1)    