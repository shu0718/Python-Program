arr = [12,34,565,78,4,56]
'''
import math
def selection_sort(arr):
    for i in range(len(arr)):
        a = i
        for j in range(i+1,len(arr)):
            if arr[a]>arr[j]:
                a = j
        arr[i],arr[a] = arr[a],arr[i]

a = selection_sort(arr)
print(a)    
'''
for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]

print(arr)    
