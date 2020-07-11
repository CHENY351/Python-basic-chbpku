# 1.Narcissistic_number
max = int(input())
for i in range(100, max+1):
    n = len(str(i))
    sum = 0
    for j in str(i):
        sum += int(j)**n
    if i == sum:
        print(i)
 

# 2.union of two str                    
a = input()
b = input()
set = set(a) | set(b) 
print(sorted(set))


# 3.number about seven
# solution 1
n = int(input())
sum = 0
for i in range(n+1):
    if i % 7 != 0 and str(i).find('7') == -1:
        sum += i ** 2
print(sum)

# solution 2
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 7 == 0 or '7' in str(i):
        continue
    else:
        sum += i ** 2
print(sum)


# 4.perfect number
n = int(input())
for i in range(6, n+1):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if i == sum:
        print(i)

        
# 5.pyramid
n = int(input())
for i in range(1, n+1):
    print((n-i) * ' ' + (2*i-1) * '+')
    
    
# 6.palindrome
n = input()
l = len(n)
for i in range(l//2):   
    if n[i] != n[(l-1)-i]:
        print('no')
        break
else:
    print('y')   

# 7.modify a list
alist=list(map(int,input().split()))
list = []
for i in alist:
    if i % 2 == 0:
        i //= 2
    else:
        i = i ** 2
    list.append(i)
print(sorted(list))
