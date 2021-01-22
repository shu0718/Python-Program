arr1 = [2,4,6,8,10,12,14]
arr2 = [1,3,5,7,9,11,13,15]
i = 0
j = 0
m = len(arr1)-1
n = len(arr2)-1

while(i<m and j<n):
    if arr1[i] < arr2[j]:
        print(arr1[i])
        i+=1
    elif arr1[i] > arr2[j]:
        print(arr2[j])
        j+=1
    else:
        print(arr2[j])
        i+=1
        j+=1        

while i<=m:
    print(arr1[i])
    i+=1

while j<=n:
    print(arr2[j])
    j+=1
    


OUTPUT:-
1
2
3
4
5
6
7
8
9
10
11
12
14
13
15
