def linear_search(list,n):
    for i in range(0,len(list)):
        if list[i] == n:
            return i+1
        

list = [1,2,3,45,64,73,455,677,777]
n = 73
print(linear_search(list,n))

