'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab  
'''

def FindPower(a,b):
    if a>=0 and b>=0:
        if b==1:
            return a
        elif b==0:
            return 1
        else:
            b -=1
            return a * FindPower(a,b)

inp = input("Enter Input a b : ").split()
a = int(inp[0])
b = int(inp[1])


print(FindPower(a,b))