n = 5
for i in range(n):
    for j in range(1,n-i):
        print("*",end='')
    print()    


for i in range(n):
    for j in range(1,n-i):
        print('#',end='')
        for k in range(n-j+1):
            print("*",end='')
        print()        
    
