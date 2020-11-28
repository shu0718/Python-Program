'''taking input number'''
m = int(input())
'''taking the input of How many decimal digits are required from point.'''
n = int(input())
low = 0
high = m 
while(high>=low):
    mid = (high+low)//2
    if mid*mid==m:
        ans = mid
        break
    else:
        if mid*mid>m:
            high = mid-1
        else:
            low = mid+1
            ''' Simply take mid value in ans variable for helping in the square root
                root finding out.'''
            ans = mid
'''program to getting digits after points. '''           
increment = 0.1 
for i in range(0,n):
    while ans*ans<=m:
        ans = ans+increment
    ans = ans-increment
    increment = increment/10
    
print(round(ans,n))            
