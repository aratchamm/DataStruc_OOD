class Stack():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items) 
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        return self.items.pop()
    def push(self,i):
        return self.items.append(i)
    def peek(self):
        return self.items[-1]
    def bottom(self):
        return self.items[0]
    def __str__(self):
        s = ''
        for i in self.items:
            s = i + ''
        return s

s = Stack()

open=['(','{','[']
close=[')','}',']']
x = 0

inp = input("Enter expresion : ")
for char in inp:
    if char in open:
            s.push(char)

    if not s.isEmpty():
        if char in close:
            if char == ')' and s.peek() == '(' or \
            char == ']' and s.peek() == '[' or \
            char == '}' and s.peek() == '{' :
                s.pop()
            else:
                x= 'U'
    else:
        x = 'C'

if not s.isEmpty() and x != 'U':
    x='O'

if x == 0: print(f"{inp} MATCH")  
if x == 'U': print(f"{inp} Unmatch open-close")  
if x == 'C': print(f"{inp} close paren excess")  
if x == 'O': print(f"{inp} open paren excess   {s.size()} : {s}")  

    