
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


# 类的练习
class People:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        
    def __str__(self):
        s = '{} comes from {}'.format(self.name, self.city)
        return s
    
    def moveto(self, newcity):
        self.city = newcity
        
    def __lt__(self, other):
        return self.city < other.city
    
    
class Teacher(People):
    def __init__(self, name, city, school):
        self.name = name
        self.city = city
        self.school = school
        
    def moveto(self, newschool):
        self.school = newschool
        
    def __lt__(self, other):
        return self.school < other.school
        
        
# 类的调用
a = People('ying','China')
b = People('meng','dongbei')
print(a)
print(a < b)
a.moveto('Canada')
print(a)


# 创建一个mylist类，继承自内置数据 类型list(列表),增加一个方法“累乘”product def product(self): 返回所有数据项的乘积
class mylist(list):
    def product(self):
        m = 1
        for n in self:
            m = n * m
        return m
# 调用    
a = mylist([1,2,3])
a.product()



# 生成器 例外处理
while True:    
    a = input()
    b = input()
    try:
        print(int(a)/int(b))
    except (ValueError, TypeError):
        print('not int')
    except ZeroDivisionError:
        print('divisor cannot be 0')
        
        
# 生成器
[i*2 for i in range(10)]
[i for i in range(100) if not ((i%7==0) or ('7' in str(i)))]


# 生成器 100以内勾股数
a = [(i, j, k) for i in range (1, 100) for j in range(1, 100) for k in range(1, 100) if i**2 + j**2 == k**2]
print(a)
    
a = {tuple(sorted([i, j, k])) for i in range (1, 100) for j in range(1, 100) for k in range(1, 100) if i**2 + j**2 == k**2}
print(a)


# 生成器 fibonacci数列
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b
        
for fn in fib():
    print(fn)
    if fn > 1000:
        break

        
# 乌龟作图 求圆周率        
import turtle
import random

t = turtle.Turtle()
turtle.tracer(0)
turtle.setworldcoordinates(0, 0, 1, 1)

t.penup()
t.goto(0,0)
t.pendown()
t.goto(0,1)
t.goto(1,1)
t.goto(1,0)
t.goto(0,0)
t.penup()
t.goto(0,1)
t.pendown()
t.circle(-1,90,100)
i = 0
for n in range(1,10001):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    t.penup()
    t.goto(x, y)
    if (x*x+y*y)**0.5 <= 1:
        t.dot(5,'pink')
        i = i+1
    else:
        t.dot(5,'blue')
print('pi',i/10000*4)
    
turtle.update()
turtle.done()


# 输入整数n，打印n行等腰空心三角形
n = int(input())
for i in range(1, n+1):
    if i == 1:
        print((n-i) * ' ' + '+')
    elif i == n:
        print((n-i) * ' ' + (2*i-1) * '+')
    else:
        print((n-i) * ' ' + '+' + (2*i-3) * ' ' + '+')
        
# 输入奇数n，打印底边为n的等腰空心三角形
n = int(input()) 
m = (n+1)//2 # 以n个+为底，共(n+1)/2行
for i in range(1, m + 1):
    if i == 1:
        print((m-i) * ' ' + '+')
    elif i == m:
        print((m-i) * ' ' + n * '+')
    else:
        print((m-i) * ' ' + '+' + (2*(i-1) -1) * ' ' + '+')
        
