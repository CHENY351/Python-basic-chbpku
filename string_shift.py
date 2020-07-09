# shift str to right
s = 'abcd'
n = 3
for i in range(n):
    s = s[-1] + s[:len(s)-1] # s = s[-1] + s[:-1]
print(s)
