
# sum of factorial 给定n，计算1+2!+3!+...+n!的值
n = int(input())
sum = 0
for k in range(1, n+1):
    # factorial of k
    temp = 1
    for i in range(1, k+1):
        temp = i * temp
    sum += temp
print(sum)


# days per month 给定y和m，计算y年m月有几天?
year = int(input())
month = int(input())
list31 = [1, 3, 5, 7, 8, 10, 12]
list30 = [4, 6, 9, 11]
if month in list31:
    print("31")
elif month in list30:
    print("30")
elif month == 2 and year % 4 == 0 and year % 100 != 0:
    print('29')
else:
    print('28')


# shift str to right 给定字符串s和数字n，打印把字符串s向右 移动n位的新字符串
s = 'abcd'
n = 3
for i in range(n):
    s = s[-1] + s[:len(s)-1] # s = s[-1] + s[:-1]
print(s)

#给定一个英文数字字符串，打印相应阿拉伯 数字字符串
s = "one-two-three"
dict = {'one':1, 'two':2, 'three':3, 'four':4}
slist = s.split('-')
print(slist)
a = ''
for key in slist:
    a = a + str(dict[key])
print(a)
