class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:     
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size

    def __str__(self):
        s=''
        p = self.head
        while p != None :
            if p!=self.tail:
                s += str(p.data) + '->'
            else:
                s += str(p.data)
            p = p.next
        return s

    def str_reverse(self):
        s=''
        p=self.tail
        while p != None :
            if p!=self.head:
                s += str(p.data) + '->'
            else:
                s += str(p.data)
            p = p.prev
        return s

    def isEmpty(self):
        if self.size == 0 :
            return True
        else:
            return False

    def append(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next=temp
            temp.prev=self.tail
            self.tail=self.tail.next
        self.size+=1

    def insert(self, index, data):
        i=0
        temp = Node(data)
        p=self.head
        if index==0:
            if(self.isEmpty()):
                self.head=temp
                self.tail=temp
            else:
                self.head.prev=temp
                temp.next=self.head
                self.head=temp
                
        elif index==len(self):
            self.append(data)
        else:
            while i != index:
                if i==index-1:
                    temp.prev=p
                    temp.next=p.next
                    p.next.prev=temp
                    p.next=temp
                else:
                    p=p.next
                i+=1
        self.size+=1

    def remove(self,data):
        p=self.head
        i=0
        while p != None:
            if p.data == data:
                if p != self.head and p != self.tail:
                    p.prev.next=p.next
                    p.next.prev=p.prev
                    p.prev=None
                    p.next=None
                elif p==self.head and self.head != self.tail:
                    p.next.prev=None
                    self.head=p.next
                    p.next=None
                elif p==self.tail and self.head != self.tail:
                    p.prev.next=None
                    self.tail=p.prev
                    p.prev=None
                else :
                    self.head=None
                    self.tail=None
                self.size-=1
                return [p,i]
            p=p.next
            i+=1
        return [None]

inp = input('Enter Input : ')
inp=inp.replace(', ',',').split(',')
DL=DoublyLinkedList()

for i in inp:
    i = i.split()
    if i[0] == 'A':
        DL.append(i[1])
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")
    elif i[0] == 'Ab':
        DL.insert(0, i[1])
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")
    elif i[0] == 'I':
        ele = i[1].split(':')
        if int(ele[0])<0 or int(ele[0])>DL.size:
            print("Data cannot be added")
        else:
            DL.insert(int(ele[0]), ele[1])
            print(f"index = {ele[0]} and data = {ele[1]}")
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")   
    elif i[0] == 'R':
        # a คือ node ตัวที่เอาออกไป ข้างในมีตน+index 
        # a[0] = ตำแหน่งที่เก็บ + a[0].data = ตัวเลข , a[1] = index 

        # ไปหาเลขใน DL อีกทีนึง
        a = DL.remove(i[1])
        if a[0] == None:
             print("Not Found!")
        else:
            print(f"removed : {a[0].data} from index : {a[1]}")
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")  