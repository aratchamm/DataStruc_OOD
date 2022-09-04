class Stack:

    def __init__(self):
        self.items = []

    def push(self, i):
        return self.items.append(i)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


inp = input('Enter Input : ').split()
inp = inp[::-1]
x=0
S = Stack()

for ele in inp:
    if S.size() < 2:
        S.push(ele)
    else:
        if S.items[-2] == S.peek() and S.peek() == ele:
            S.pop()
            S.pop()
            x+=1
        else:  
            S.push(ele)

print(S.size())
for i in range(len(S.items)):
    print(S.items[i], end="")
    
if S.isEmpty():
    print("Empty")
else:
    print()
if(x>1):
    print(f"Combo : {x} ! ! !")