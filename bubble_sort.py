from array import *

arr = array('i',[])

n = int(input("Enter the length of arr :"))

for i in range(n):
    x = int(input())
    arr.append(x)


for i in range(0,n):
    for j in range(0,n-1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp


print(arr)            
