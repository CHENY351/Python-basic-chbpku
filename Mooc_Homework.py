# string shfit left
s = str(input())
n = int(input())
a = s[:n]
b = s[n:]
ss = b + a
print(ss)


# height of triangle
import math
a = int(input())
b = int(input())
c = math.sqrt(a ** 2 + b ** 2)
h = round(a * b / c, 2)
print(h)


