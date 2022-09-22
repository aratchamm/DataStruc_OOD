'''
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า

4. def isEmpty(self): return list นั้นว่างหรือไม่

5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

6. def insert(self, index, data): insert data ใน index ที่กำหนด

7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append       ->  A
2. add_before -> Ab
3. insert          ->   I
4. remove       ->  R

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
'''

class DummyNode():
    def __init__(self,data):
        self.next = None
        self.data = data
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail=None
        self.size = 0

    def __str__(self):
        s=''
        h = self.head
        while h != None:
            if h != self.tail:
                s += str(h.data) + '->'
            else:
                s += str(h.data)
            h = h.next
        return s

    def str_reverse(self):
        s=''
        t = self.tail
        while t != None:
            if t!= self.head:
                s += str(t.data) + '->'
            else:
                s += str(t.data)
            t = t.prev
        return s

    def isEmpty(self):
        if self.size == 0: return True
        else: return False

    def append(self, data):
        newNode = DummyNode(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev=self.tail
            self.tail=self.tail.next
        self.size+=1

    def insert(self, index, data):
        newNode = DummyNode(data)
        cur_index = 0
        cur = self.head
        if index == 0:
            if(self.isEmpty()):
                self.head = newNode
                self.tail = newNode
            else:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode

        elif index==len(self):
            self.append(data)
        else:
            while i != index:
                if i==index-1:
                    cur.prev=p
                    cur.next=p.next
                    p.next.prev=cur
                    p.next=cur
                else:
                    p=p.next
                i+=1
        self.size+=1

    def remove(self, data):
        cur = self.head
        cur_index = 0
        while cur != None:
            # กรณีข้างหน้า
            if cur == self.head and cur != self.tail:
                self.head = cur.next
                cur.next = None
                cur.next.prev = None

            # กรณีข้างหลัง
            if cur == self.tail and cur != self.head:
                self.tail = cur.prev
                cur.prev = None
                cur.prev.next = None

            # กรณีตรงกลาง
            if cur != self.head and cur != self.tail:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.next = None
                cur.prev = None



            
l = DoublyLinkedList()
inp = [i.strip() for i in input("Enter Input : ").split(",")]
for i in inp:
    if i[0] == 'A'and i[1] != 'b':
            l.append(i[2:])
            print(f"linked list : {l}")
            print(f"reverse : {l.str_reverse()}")
    elif i[0] == 'A' and i[1] == 'b':
            l.insert(0,i[2:])
            print(f"linked list : {l}")
            print(f"reverse : {l.str_reverse()}")
    elif i[0] == 'I': 
            a = i[2:].split(':')
            index = int(a[0])
            data = a[1]
            if index<0 or index>l.size: 
                print("Data cannot be added")
            else: 
                l.insert(index,data)
                print(f"index = {index} and data = {data}")
                
            print(f"linked list : {l}")
            print(f"reverse : {l.str_reverse()}")
            
    elif i[0]   == 'R': 
        if i[2] not in l: print("Not Found!")
        else: 
            print(f"removed : {i[2]} from index : 0")
            l.remove(i[2])