# Ch3-1. String shfit left
s = str(input())
n = int(input())
a = s[:n]
b = s[n:]
ss = b + a
print(ss)


# Ch3-2. Height of triangle
import math
a = int(input())
b = int(input())
c = math.sqrt(a ** 2 + b ** 2)
h = round(a * b / c, 2)
print(h)


# Ch3-3. Length of the last word in a string
s = str(input())
n = len(s.split(' ')[-1])
print(n)


# Ch3-4. Times of one character appear in a string
s = input()
a = s.split()
n = a[0].count(a[1])
print(n)


# Ch4-1. 合并两个列表并去重
alist=list(map(int, input().split()))
blist=list(map(int, input().split()))
new = (list(set(alist + blist)))
print(new)


# ch5-1.Narcissistic_number
max = int(input())
for i in range(100, max+1):
    n = len(str(i))
    sum = 0
    for j in str(i):
        sum += int(j)**n
    if i == sum:
        print(i)
 

# ch5-2.union of two str                    
a = input()
b = input()
set = set(a) | set(b) 
print(sorted(set))


# ch5-3.number about seven
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


# ch5-4.perfect number
n = int(input())
for i in range(6, n+1):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if i == sum:
        print(i)

        
# ch5-5.pyramid
n = int(input())
for i in range(1, n+1):
    print((n-i) * ' ' + (2*i-1) * '+')
    
    
# ch5-6.palindrome
n = input()
l = len(n)
for i in range(l//2):   
    if n[i] != n[(l-1)-i]:
        print('no')
        break
else:
    print('y')   

# ch5-7.modify a list
alist=list(map(int,input().split()))
list = []
for i in alist:
    if i % 2 == 0:
        i //= 2
    else:
        i = i ** 2
    list.append(i)
print(sorted(list))


# ch5-8。打印一定范围内的素数
n = int(input())
list = []
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list.append(i)
print(list)
