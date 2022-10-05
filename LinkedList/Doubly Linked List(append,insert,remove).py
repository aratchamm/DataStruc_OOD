
from tkinter.messagebox import NO


class Node():
    def __init__(self,data):
        self.next = None
        self.data = data

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        s = ''
        cur = self.head
        while cur != None:
            if cur!= self.tail:
                s += str(self.data) + "->"
            else:
                s += str(self.data)
            cur = cur.next
        return s
    def str_reverse(self):
        s = ''
        cur = self.tail
        while cur != None:
            if cur != self.head:
                s += str(self.data) + "->"
            else:
                s += str(self.data)

            cur = cur.prev

        return s
    def isEmpthy(self):
        return self.size == 0
    def append(self,data):
        newNode = Node(data)
        if self.isEmpthy():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1
    def insert(self,pos,data):
        newNode = Node(data)
        if pos == 0:
            if self.isEmpthy():
                self.head = newNode
                self.tail = newNode
            else:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
        elif pos == self.size -1:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            cur_idx = 0
            cur = self.head
            while cur_idx < pos-1:
                cur_idx += 1
                cur = cur.next
            curNext = cur.next
            curNext.next.prev = cur 
            cur.next = curNext.next
            curNext.prev = None
            curNext.next = None
        self.size -= 1
    
    def remove(self,data):
        cur = self.head
        cur_idx = 0
        while cur != None:
                if cur.data == data:
                    if cur != self.head and cur != self.tail:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                        cur.next = None
                        cur.prev = None
                    elif cur == self.head and self.head != self.tail:
                        cur.next.prev = None
                        self.head = cur.next
                        cur.next = None
                    elif cur == self.tail and self.tail != self.head:
                        self.tail = cur.next
                        cur.prev.next = None
                        cur.prev = None
                    else:
                        self.head = None
                        self.tail = None
                    self.size -= 1
                    return [cur,cur_idx]

                cur = cur.next
                cur_idx += 1

        return [None]

