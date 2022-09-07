class  Queue():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def enQueue(self,i):
        return self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def bottom(self):
        return self.items[-1]
    def front(self):
        return self.items[0]
    def __str__(self):
        s = ''
        for i in self.items:
            s = i + ''
        return s

q = Queue()
qEN = Queue()

inp = [*input("Enter Input : ")]
print(inp)