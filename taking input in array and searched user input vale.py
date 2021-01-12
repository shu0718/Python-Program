from array import*

arr = array('i',[])

n = int(input("Enter the value of n"))

for i in range(n):
    x = int(input())
    arr.append(x)

for i in range(n):
    print(arr[i],end=' ')
print()    


arr.insert(2,3)
print(arr)
print(type(arr))

del arr[2]
print(arr)

y = int(input("Enter the searched values in given array:"))

for i in range(n):
    if y == arr[i]:
        print("searched is successfull")
        break
    else:
        if i == n-1:
            print("searched item is not in the list")
        else:
            i+=1
            
        

        
