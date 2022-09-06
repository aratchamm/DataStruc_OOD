class Stack():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        if self.isEmpty(): return -1
        return self.items.pop()
    def push(self,i):
        return self.items.append(i)
    def peek(self):
        if self.isEmpty(): return -1
        return self.items[-1]

s = Stack()

def ManageStack(ele) :
    if ele[0] == 'A':
        s.push(ele[1])
    elif ele[0] == 'P':
        s.pop()
    elif ele[0] == 'D':
        indexData = s.items.index(ele[1])
        print(indexData)


inp = input("Enter Input : ").split(",")
for ele in inp:
    ele = ele.split()
    ManageStack(ele)