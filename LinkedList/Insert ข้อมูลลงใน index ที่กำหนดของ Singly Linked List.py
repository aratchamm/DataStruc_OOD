# สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง 

# โดยคลาส LinkedList จะประกอบไปด้วย

# 1. def __init__(self): สำหรับสร้าง linked list

# 2. def __str__(self): return string แสดง ค่าใน linked list

# 3. def isEmpty(self): return list นั้นว่างหรือไม่

# 4. def append(self, data): เพิ่ม data ต่อท้าย linked list

# 5. def insert(self, index, data): insert data ใน index ที่กำหนด

# โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

# คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Header Node ดูนะครับ

# *******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********

# class Node:
#     def __init__(self, data):
#         self.data = data
     


# ข้อมูลอินพุท จะคั่นด้วยเครื่องหมาย คอมม่า

# ตัวแรก จะเป็น ลิสต์ตั้งต้น คั่นด้วยช่องว่าง (space)

# ตัวต่อไปจะอยู่ในรูปแบบ index:data

# Enter Input : 1 2 3 4, 0:7, 3:9
# ลิสต์ตั้งต้นคือ 1->2->3-> 4

# ข้อมูล 0:0 คือให้เพิ่ม node ลำดับ 0 โดยมีข้อมูลเป็น 7

# ข้อมูล 3:9 คือให้เพิ่ม node ลำดับ 3 โดยมีข้อมูลเป็น 9


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