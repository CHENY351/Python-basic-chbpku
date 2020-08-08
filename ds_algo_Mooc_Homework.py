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
