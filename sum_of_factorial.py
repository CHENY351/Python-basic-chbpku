
# sum of factorial
n = int(input())
sum = 0
for k in range(1, n+1):
    # factorial of k
    temp = 1
    for i in range(1, k+1):
        temp = i * temp
    sum += temp
print(sum)
