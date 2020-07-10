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
        
