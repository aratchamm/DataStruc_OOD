'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab  
'''

def FindPower(a,b):
    return a**b

inp = input("Enter Input a b : ").split()
a = int(inp[0])
b = int(inp[1])


print(FindPower(a,b))