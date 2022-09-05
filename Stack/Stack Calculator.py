# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# *************************************************
# print("* Stack Calculator *")
# arg = input("Enter arguments : ")
# machine = StackCalc()
# machine.run(arg)
# print(machine.getValue())

import sys

class Stack():
    def __init__(self):
        self.items = []
    def pop(self):
        if self.isEmpty(): return None
        return self.items.pop()
    def push(self,i):
        return self.items.append(i)
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def peek(self):
        if s.isEmpty(): return None
        return self.items[-1]

instruction = ['+','-','*','/','DUP','POP','PSH']
s = Stack()

class StackCalc(Stack):
    def __init__(self):
        super().__init__()

    def plus(self):
        s.push(s.pop() + s.pop())
    def minus(self):
        s.push(s.pop() - s.pop())
    def divide(self):
        s.push(int(s.pop() / s.pop()))
    def mul(self):
        s.push(s.pop() * s.pop())
    def dup(self):
        s.push(s.peek())
    def pop(self):
        s.pop()
    def getValue(self):
        valu = s.peek()
        if valu == None: return 0
        return valu


    def run(self,arg):
        arg = arg.split()
        for i in arg:
            if i.isnumeric():
                s.push(int(i))
            elif i in instruction:
                if s.size()>1:
                    if i=='+':
                        self.plus()
                    elif i=='-':
                        self.minus()
                    elif i=='*':
                        self.mul()
                    elif i=='/':
                        self.divide()

                if s.size() > 0 :
                    if i=='DUP':
                        self.dup()
                    elif i=='POP':
                        self.pop()
                    elif i=='PSH':
                        self.Psh()
                    
            else:
                print(f"Invalid instruction: {i}")
                sys.exit()
            

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())