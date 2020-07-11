# 1.Narcissistic_number
max = int(input())
for i in range(100, max+1):
    n = len(str(i))
    sum = 0
    for j in str(i):
        sum += int(j)**n
    if i == sum:
        print(i)
        
        
     
    
    
alist=list(map(int,input().split()))
list = []
for i in alist:
    if i % 2 == 0:
        i //= 2
    else:
        i = i ** 2
    list.append(i)
print(sorted(list))
