n = int(input())
m = int(input())
sum_even = 0
sum_odd = 0
for i in range(n,m+1):
    if i%2 == 0:
        sum_even += i
    else:
        sum_odd += i
        
print(sum_odd)
print(sum_even)
