s = "one-two-three"
dict = {'one':1, 'two':2, 'three':3, 'four':4}
slist = s.split('-')
print(slist)
a = ''
for key in slist:
    a = a + str(dict[key])
print(a)
