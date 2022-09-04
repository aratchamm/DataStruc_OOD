# กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

# ***** อธิบาย Input 5 แบบ *****

# 1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

# 2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

# 4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร


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
    