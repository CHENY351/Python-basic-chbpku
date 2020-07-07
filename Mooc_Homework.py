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
