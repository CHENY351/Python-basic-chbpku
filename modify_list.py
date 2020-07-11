alist=list(map(int,input().split()))
list = []
for i in alist:
    if i % 2 == 0:
        i //= 2
    else:
        i = i ** 2
    list.append(i)
print(sorted(list))
