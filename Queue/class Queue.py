class Queue():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def deQueue (self):
        return self.items.pop(0)
    def enQueue(self,i):
        return self.items.append(i)

    def front(self):
        return self.items[0]
    def peek(self):
        return self.items[0]

    def __str__(self):
        s = ''
        for i in self.items:
            s += i + ' '
        return s