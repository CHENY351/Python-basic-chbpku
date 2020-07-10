n = input()
l = len(n)
for i in range(l//2):   
    if n[i] != n[(l-1)-i]:
        print('no')
        break
else:
    print('y')
