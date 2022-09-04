# จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

# โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

# 1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

# 2. วงเล็บปิดเกิน

# 3. วงเล็บเปิดเกิน

# แล้วให้แสดงผลตามตัวอย่าง

class Stack():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, i):
        return self.items.append(i)
    def pop(self):
        self.items.pop()
    def peek(self):
        if self.isEmpty(): return None
        return self.items[-1]

s = Stack()

open = ['(','{','[']
close = [')',']','}']
p=0

x = input("Enter expresion : ")
for char in x:
    if char in open:
        s.push(char)
        p=0
    else:
        if not s.isEmpty():
            if s.peek() == '{' and char == '}':
                s.pop()
            elif s.peek() == '[' and char == ']':
                s.pop()
            elif s.peek() == '(' and char == ')':
                s.pop()
            elif char in close and char != s.peek():
                p='U'
        else:
            p='C'
        

if not s.isEmpty() and p==0:
    p='O'

if p=='U':
    print(f"{x} Unmatch open-close")
elif p=='C':
    print(f"{x} close paren excess")
elif p=='O':
    print(f"{x} open paren excess {s.size()} : ",end='')
    for i in range(len(s.items)):
        print(s.items[i], end="")
elif p==0:
    print(f"{x} MATCH")
