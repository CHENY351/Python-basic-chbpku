# 一维开心消消乐：输入一串字符，逐个消去相邻的相同字符对,如果字符全部被消完，则输出不带引号的“None”
#solution 1
from pythonds.basic.stack import Stack

def xiaoxiaole(string):    
    s = Stack()
    for index in range(len(string)):
        a = string[index]
        if s.isEmpty() or index == 0:
            s.push(a)
        else:
            if  a != s.peek():
                s.push(a)
            else:
                s.pop()
            
    if s.isEmpty():
        return None
    else:
        output = ''
        while not s.isEmpty():
            output = output + str(s.pop())
            o = output[::-1]
        return o

print(xiaoxiaole('bbeeasd'))

# solution2
from pythonds.basic.stack import Stack

def xiaoxiaole(s):
    st = Stack()
    for a in s:
        if not st.isEmpty() and a == st.peek():
            st.pop()
        else:
            st.push(a)
    if st.isEmpty():
        return None
    else:
        output = ''
        while not st.isEmpty():
            output = output + str(st.pop())
        o = output[::-1]
        return o
    
s = input()
res = xiaoxiaole(s)
print(res)

# 洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
# 小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。
# 老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。
# 输入格式:长度为10的字符串，其中只包含0～9的数字，且不重复，代表顾客依次取到的盘子编号
# 输出格式：字符串：Yes或者No，表示遵照次序洗盘子，或者没有遵照次序洗盘子

from pythonds.basic.stack import Stack

def bossPan(s):
    st = Stack()
    n = 0  # 正在洗的盘子的编号
    i = 0  # 取盘子的次数，s[i]是取得盘子的编号
    while i < 10 and n < 10:
        # 洗盘子
        q = int(s[i])
        if n <= q:
            for m in range(n,q+1):
                st.push(m)
                print('push',m)
            n = q+1 # 正在洗下一个盘子
        
        # 取盘子
        while not st.isEmpty() and st.peek() == int(s[i]):
            m = st.pop()
            print('pop',m)
        i += 1
            
    if st.isEmpty():
        return 'Yes'
    else:
        return 'NO'
      
        
s = input()
res = bossPan(s)
print(res)
