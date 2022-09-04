class Stack():

    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def push(self,i):
        return self.items.append(i)
    def pop(self):
        if self.isEmpty(): return None
        return self.items.pop()
    def peek(self):
        return self.items[-1]
s=Stack()
inp = input("Enter Input : ").split(",")
for i in inp:
    i = i.split()
    if i[0] == 'A':
        s.push(i[1])
        print(f"Add = {i[1]} and Size = {s.size()}")
    elif i[0] == 'P':
        if not s.isEmpty(): 
            print(f"Pop = {s.pop()} and Index = {s.size()}")
        else:
            print("-1")
    
print("Value in Stack = ",end="")
if s.isEmpty():
    print("Empty")
else: 
    for i in s.items:
        print(i,end=" ")