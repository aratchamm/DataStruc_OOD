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
        self.stack = []
    def push(self, item):
        return self.stack.append(item)
    def pop(self):
        if self.isEmpty(): return None
        return self.stack.pop()
    def peek(self):
        if self.isEmpty(): return None
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()
instructions = ['+','-','*','/','DUP','POP','PSH']

class StackCalc(Stack):
    def __init__(self):
        super().__init__()

    def plus(self):
        s.push(s.pop() + s.pop())
    def minus(self):
        s.push(s.pop() - s.pop())
    def divide(self):
        s.push(s.pop() / s.pop())
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
        for arg in arg.split():
            if arg.isnumeric():
                s.push(int(arg))
            elif arg in instructions :
                if s.size() > 1:
                    if arg == '+':
                        self.plus()
                    elif arg == '-':
                        self.minus()
                    elif arg == '*':
                        self.mul()
                    elif arg == '/':
                        self.divide()

                if s.size() > 0:
                    if arg == 'DUP':
                        self.dup()
                    elif arg == 'POP':
                        self.pop()
                    elif arg == 'PSH':
                        pass
            else:
                print(f"Invalid instruction: {arg}")
                sys.exit()
                
                

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
output = machine.run(arg)
print(machine.getValue())