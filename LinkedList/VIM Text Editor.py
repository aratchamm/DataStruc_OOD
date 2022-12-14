'''
เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่ ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  

***** รูปแบบ input *****

แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40

1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน

2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย

***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****

***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return self.data

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
                s += str(p.data) + ' '
            else:
                s += str(p.data)
            p = p.next
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
            self.size-=1
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

    def isin(self,data):
        i=0
        p=self.head
        if self.head != self.tail:
            while p!=None:
                if(p.data == data):
                    return i
                else:
                    p=p.next
                    i+=1
        elif self.head == self.tail:
            return 0
        return -1

    def deleteAt(self,index):
        i=0
        p=self.head
        
        while i!=index:
            i+=1
            if p.next != None:
                p=p.next
            else:
                return None
        if(p!=self.head and p!=self.tail ):
            p.prev.next=p.next
            p.next.prev=p.prev
        elif p==self.head :
            p.next.prev=None
            self.head=p.next
            p.next=None
        elif p==self.tail :
            p.prev.next=None
            self.tail=p.prev
            p.prev=None
        self.size-=1
        return p

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

DL = DoublyLinkedList()
inp = input("Enter Input : ").split(",")
DL.append('|')


for i in inp:
    i = i.split()
    if i[0] == 'I':
        DL.insert(i[1])
    