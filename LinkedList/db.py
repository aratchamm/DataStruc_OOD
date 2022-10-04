
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        a=Node(item)
        if self.isEmpty():
            self.head=a
            self.tail=a
        else:
            self.tail.next=a
            a.previous=self.tail
            a.next=None
            self.tail=a

    def addHead(self, item):
        a=Node(item)
        if self.head != None:
            a.next=self.head
            self.head.previous=a
            self.head=a
        else:
            self.head=a
            self.tail=a
        
    def insert(self, pos, item):
        a=Node(item)
        if self.isEmpty():
            self.head=a
            self.tail=a
        elif pos==0 or -1*pos>self.size():
        
            self.head.previous=a
            a.next=self.head
            self.head=a   
        elif pos>=self.size()-1:
            self.tail.next=a
            a.previous=self.tail
            self.tail=a
        elif pos>=1:
            p=self.head #ตัวชี้
            n=0
            while p!=None:
                n+=1
                if pos-1==n:
                    break
                p=p.next
            a.next=p.next 
            p.next.previous=a
            a.previous=p
            p.next=a
        else:
            p=self.tail
            n=1
            while n<-1*pos:
                n+=1
                p=p.previous
            a.previous=p.previous
            p.previous.next=a
            a.next=p
            p.previous=a
             

    def search(self, item):
        s=self.head
        while s!=None:
            if s.value==item:
                return 'Found'
            else:
                s=s.next
        return 'Not Found'        
    
    def index(self, item):
        s=self.head
        a=0
        while s!=None:
            if s.value==item:
                
                return a
            s=s.next
            a+=1
            
        return -1
    
    def size(self):
        h=self.head
        s=0
        while h is not None:
            s+=1
            h=h.next
        return s
        
        

    def pop(self, pos):
       if pos<0 or pos>=self.size():
            return "Out of Range"
       else:
            i=0
            cur=self.head
            while i<pos:
                cur=cur.next
                i+=1
            if self.size()==1:
                self.head=None
                self.previous=None
            elif i==0:
                self.head = cur.next
                self.head.previous = None
            elif i==self.size()-1:
                self.tail = cur.previous
                self.tail.next = None
            else:
                cur.next.previous = cur.previous
                cur.previous.next = cur.next
            return "Success"        
                

    

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())