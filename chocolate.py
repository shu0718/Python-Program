n = int(input())
a = list(map(int,input().split()))
print(a)
s1s2 = input().split()
s1 = s1s2[0]
b = int(s1)
s2 = s1s2[1]
sum1 = 0
count1 = 0
c = []
for i in range(0,n-s2):
    for j in range(i,i+s2):
        sum1 += a[j]
    c.append(sum1)

for i in range(0,len(c)):
    if c[i] == s1:
        count1+=1
    

print(count1)        
    
