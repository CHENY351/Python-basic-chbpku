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