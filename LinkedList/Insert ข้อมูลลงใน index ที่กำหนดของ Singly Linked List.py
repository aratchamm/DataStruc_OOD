from dataclasses import replace


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:
                s+="->"
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next = p
        self.size+=1
    
    def insert(self, index, data):
        p=Node(data)
        if self.isEmpty():
            self.head = p
        elif index==0:
            p.next = self.head
            self.head = p
        else:
            t=self.head
            i = 0
            while i<index-1:
                i+=1
                t=t.next
            p.next = t.next
            t.next = p
        self.size +=1

l = LinkedList()        
inp = input("Enter Input : ")
inp=inp.replace(', ',',').split(',')

h = inp[0].split()
for i in h:
    l.append(i)
if not l.isEmpty(): 
    print(f"link list : {l}")
else: 
    print("List is empty")
for i in inp[1:]:
        i = i.split(":")
        index = int(i[0])
        data = i[1]
        if index < 0 or index>l.size:
            print("Data cannot be added")
        else:
            print(f"index = {index} and data = {data}")
            l.insert(index,data)
        if not l.isEmpty(): 
            print(f"link list : {l}")
        else: 
            print("List is empty")