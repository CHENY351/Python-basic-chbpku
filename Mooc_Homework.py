# 1. String shfit left
s = str(input())
n = int(input())
a = s[:n]
b = s[n:]
ss = b + a
print(ss)


# 2. Height of triangle
import math
a = int(input())
b = int(input())
c = math.sqrt(a ** 2 + b ** 2)
h = round(a * b / c, 2)
print(h)


# 3. Length of the last word in a string
s = str(input())
n = len(s.split(' ')[-1])
print(n)


# 4. Times of one character appear in a string
s = str(input())
n = str(input())
a = s.count(n)
print(a)

