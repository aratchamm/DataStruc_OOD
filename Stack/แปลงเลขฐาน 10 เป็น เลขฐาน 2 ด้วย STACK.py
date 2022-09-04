class Stack :

    def __init__(self):
        self.stack = []
    
    def push(self, item):
        return self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0

def dec2bin(token):
    s = Stack()
    out = ''

    while token!=0:
        mod = token%2
        token = token//2
        s.push(mod)

    while s.size() > 0:
        out = out + str(s.pop())
    return out

    ### Enter Your Code Here ###

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))