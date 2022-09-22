'''
สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง 

โดยคลาส LinkedList จะประกอบไปด้วย

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def isEmpty(self): return list นั้นว่างหรือไม่

4. def append(self, data): เพิ่ม data ต่อท้าย linked list

5. def insert(self, index, data): insert data ใน index ที่กำหนด

โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Header Node ดูนะครับ

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********

class Node:
    def __init__(self, data):
        self.data = data
     


ข้อมูลอินพุท จะคั่นด้วยเครื่องหมาย คอมม่า

ตัวแรก จะเป็น ลิสต์ตั้งต้น คั่นด้วยช่องว่าง (space)

ตัวต่อไปจะอยู่ในรูปแบบ index:data

Enter Input : 1 2 3 4, 0:7, 3:9
ลิสต์ตั้งต้นคือ 1->2->3-> 4

ข้อมูล 0:0 คือให้เพิ่ม node ลำดับ 0 โดยมีข้อมูลเป็น 7

ข้อมูล 3:9 คือให้เพิ่ม node ลำดับ 3 โดยมีข้อมูลเป็น 9
'''

class Node():
    def __init__(self,data):
      self.next = None
      self.data = data

class LinkedList():
     def __init__(self):
      self.head = None
      self.size = 0
    
     def __str__(self):
        s=''
        cur = self.head
        while cur != None:
            s += str(cur.data)
            if cur.next != None:
               s += '->'
            cur = cur.next   
        return s

     def isEmpty(self):
        return self.head == None

     def append(self, data):
        # สร้าง node ใหม่มา
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
               cur = cur.next
            cur.next = new_node
        self.size += 1

     def remove(self,data):
         cur_idx = 0
         cur = self.head
         while cur != None:
            if cur.data == data:
               if cur == self.head:
                  cur.next = None
                  self.head = cur
               elif cur == len(self)-1:
                  cur.next = None

               # กรณีอยู่ตรงกลาง
               else:
                  pass

                   

               
            self.size-= 1

            cur = cur.next
            cur_idx += 1


     def insert(self, index, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        elif index == 0:
            # สร้าง node ใหม่มา ยัดไปใส่หน้าเอา กำหนดให้ตัวที่อยู่ตอนแรกลิ้งไป
            new_node.next = self.head
            # ให้ตัวแรกเป็น head
            self.head = new_node
        else:
            cur = self.head
            cur_idx = 0
            while cur_idx < index-1:
               cur_idx += 1
               cur = cur.next
               
            new_node.next = cur.next
            cur.next = new_node
        self.size += 1 
      
      
         

l = LinkedList()    
inp = [i.strip() for i in input("Enter Input : ").split(",")]
fst = inp[0].split()

for i in fst:
   l.append(i)
if l.isEmpty():
   print("List is empty")
else:
   print(f"link list : {l}")

for i in inp[1:]:
   i = i.split(":")
   index = int(i[0])
   data = i[1]

   if index<0 or index>l.size:
      print("Data cannot be added")
      if l.isEmpty():
         print("List is empty")
      else:
         print(f"link list : {l}")
   else:
      l.insert(index, data)
      print(f"index = {index} and data = {data}")
      print(f"link list : {l}")