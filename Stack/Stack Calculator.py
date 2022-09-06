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
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def push(self,i):
        return self.items.append(i)
    def pop(self):
        if self.isEmpty(): return None
        return self.items.pop()
    def peek(self):
        if self.isEmpty(): return None
        return self.items[-1]

s = Stack()
instructions = ['+','-','*','/','PSH','POP','DUP']

class StackCalc():

    def __init__(self):
        super().__init__()

    def plus(self):
        s.push(s.pop() + s.pop())
    def min(self):
        s.push(s.pop() - s.pop())
    def mul(self):
        s.push(s.pop() * s.pop())
    def div(self):
        s.push(int(s.pop() / s.pop()))
    def dulpicate(self):
        s.push(s.peek())

    def run(self,arg):
        for ele in arg.split():
            if ele.isnumeric():
                s.push(int(ele))
            else:
                if ele in instructions:
                    if not s.isEmpty() :
                        if ele == 'DUP':
                            self.dulpicate()
                        elif ele == 'POP':
                            s.pop()
                        elif ele == 'PSH':
                            s.push(ele)

                    if s.size() >=2:
                        if ele == '+':
                            self.plus()
                        elif ele == '-':
                            self.min()
                        elif ele == '*':
                            self.mul()
                        elif ele == '/':
                            self.div()
                else:
                    print(f"Invalid instruction: {ele}")
                    sys.exit()

    def getValue(self):
        if s.peek() != None: 
            valu = s.peek()
            return valu
        else: return 0



print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())