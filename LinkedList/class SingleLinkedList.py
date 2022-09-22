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