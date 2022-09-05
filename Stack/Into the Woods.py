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
        return self.items.pop()
    def peek(self):
        if S.isEmpty(): return None
        return int(self.items[-1])

S = Stack()
inp = input("Enter Input : ").split(",")
for ele in inp:
    ele = ele.split()
    if ele[0] == 'A':
        ele[1] = int(ele[1])
        
        if S.isEmpty():
            S.push(ele[1])
        else:
            while not S.isEmpty() and S.peek() <= int(ele[1]):
                S.pop()
            S.push(ele[1])

    elif ele[0] == 'B':
        print(S.size())