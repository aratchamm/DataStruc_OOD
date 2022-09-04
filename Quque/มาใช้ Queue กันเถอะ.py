# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

# D                 ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
#                     ปัจจุบันของ Queue

# ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
# ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty

class Queue():
    def __init__(self):
        self.stack = []
    def enQueue(self,i):
        self.stack.append(i)
    def deQueue(self):
        if q.isEmpty(): return None
        return self.stack.pop(0)
    def size(self): 
        return len(self.stack)
    def isEmpty(self): 
        return len(self.stack) == 0
    def peek(self):
        return self.stack[0]

q = Queue()
q2 = Queue()
inp = input("Enter Input : ").split(",")
for ele in inp:
    ele = ele.split()
    if ele[0] == 'E':
        if q.size() >= 1:
            for i in range(len(q.stack)):
                print(f"{q.stack[i]}, ", end="")
        print(ele[1])

        q.enQueue(ele[1])
        
    elif ele[0] == 'D':
        if not q.isEmpty():
            p = q.deQueue()
            q2.enQueue(p)
            print(f"{p} <- ",end='')
        if not q.isEmpty():
            for i in range(len(q.stack)):
                print(f"{q.stack[i]}", end="")
                if i!=len(q.stack)-1:
                    print(", ",end="")
            print()
        else:
            print("Empty")  
            break

if not q2.isEmpty():
    for i in range(len(q2.stack)):
        print(f"{q2.stack[i]}", end="")
        if i!=len(q2.stack)-1:
            print(", ",end="")
else:
    print("Empty",end='')

print(" : ",end="")

if not q.isEmpty():
    for i in range(len(q.stack)):
        print(f"{q.stack[i]}", end="")
        if i!=len(q.stack)-1:
            print(", ",end="")
else:
    print("Empty",end='')
