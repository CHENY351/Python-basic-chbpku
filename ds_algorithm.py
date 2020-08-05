# 用栈判断括号是否合理
from pythonds.basic.stack import Stack

def parChecker(string):
    s = Stack()
    balance = True
    index = 0
    while balance and index < len(string):
        a = string[index]
        if a in '([{':
            s.push(a)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not match(top, a):
                    balance = False       
        index += 1
        
    if balance and s.isEmpty():
        return True
    else:
        return False
    
def match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)
    
print(parChecker('{[(])]()((()))}'))

# 用栈将十进制转化为二进制
from pythonds.basic.stack import Stack

def decTobinary(dec):
    s = Stack()
    
    while dec > 0:
        a = dec % 2
        s.push(a)
        dec = dec // 2
        
    binary = ''
    while not s.isEmpty():
        binary = binary + str(s.pop())
    
    return binary

print(decTobinary(233))


# 用栈将十进制转化为十六进制
from pythonds.basic.stack import Stack

def decToHex(dec):
    s = Stack()
    digits = '0123456789ABCDEF'
    
    while dec > 0:
        a = dec % 16
        s.push(a)
        dec = dec // 16
        
    binary = ''
    while not s.isEmpty():
        binary = binary + digits[s.pop()]
    
    return binary

print(decToHex(233))


# 后缀表达式求值
from pythonds.basic.stack import Stack

def postfixValue(postfixExpr):
    operandStack = Stack()
    #tokenList = postfixExpr.split()
    
    for token in postfixExpr:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = domath(token, operand2, operand1)
            operandStack.push(result)
    return operandStack.pop()

def domath(operator, operand2, operand1):
    if operator == '+':
        return operand2 + operand1
    elif operator == '-':
        return operand2 - operand1
    elif operator == '*':
        return operand2 * operand1
    else:
        return operand2 / operand1
    
print(postfixValue('45*62*+'))
