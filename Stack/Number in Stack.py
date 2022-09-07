from operator import index
from tkinter.messagebox import NO


class Stack():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        if self.isEmpty(): return None
        return self.items.pop()
    def push(self,i):
        return self.items.append(i)
    def peek(self):
        if self.isEmpty(): return None
        return self.items[-1]
    def __str__(self):
        s = ''
        for i in self.items:
            s += str(i) + ' '
        return s

s = Stack()
sD = Stack()

def ManageStack(ele) :
    if ele[0] == 'A':
        s.push(ele[1])
        print(f"Add = {ele[1]} ")
    elif ele[0] == 'P':
        print(f"Pop = {s.pop()}")
    elif ele[0] == 'D':
        if s.isEmpty():
            print(-1)
        while not s.isEmpty():
            x = s.pop()
            if x != ele[1]:
                sD.push(x)   
            else:
                print(f"Delete = {ele[1]}") 
        while not sD.isEmpty():
            s.push(str(sD.pop()))
        
        
    elif ele[0] == 'LD':
        while not s.isEmpty():
            x = int(s.pop())
            if int(ele[1]) <= x:
                sD.push(x)  
            else:
                print(f"Delete = {x} Because {x} is less than {ele[1]}")
        while not sD.isEmpty():
            s.push(str(sD.pop()))
    elif ele[0] == 'MD':
        while not s.isEmpty():
            x = int(s.pop())
            if int(ele[1]) >= x:
                sD.push(x)  
            else:
                print(f"Delete = {x} Because {x} is more than {ele[1]}")
        while not sD.isEmpty():
            s.push(str(sD.pop()))




inp = input("Enter Input : ").split(",")
for ele in inp:
    ele = ele.split()
    ManageStack(ele)
print(f"Value in Stack = {s.items}")