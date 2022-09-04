# หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!" กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

#     โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย



# class Stack:

#     def __init__(self):

#     def push(self, value):

#     def pop(self):

#     def size(self):

#     def isEmpty(self):



# inp = input('Enter Input : ').split()

# S = Stack()

# ### Enter Your Code Here ###

# print(S.size())

# ### Enter Your Code Here ###




class Stack:

    def __init__(self):
        self.items = []

    def push(self, i):
        return self.items.append(i)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


inp = input('Enter Input : ').split()
inp = inp[::-1]
x=0
S = Stack()

for ele in inp:
    if S.size() < 2:
        S.push(ele)
    else:
        if S.items[-2] == S.peek() and S.peek() == ele:
            S.pop()
            S.pop()
            x+=1
        else:  
            S.push(ele)

print(S.size())
for i in range(len(S.items)):
    print(S.items[i], end="")
    
if S.isEmpty():
    print("Empty")
else:
    print()
if(x>1):
    print(f"Combo : {x} ! ! !")