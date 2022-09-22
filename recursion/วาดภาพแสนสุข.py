'''
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว
'''

def staircase(n,s):
    if n>0:
        s+=1
        print("_"*(n-1) + "#"*(s))
        staircase(n-1,s)

    elif n<0:
        print("_"*(s) + "#"*(abs(n)))
        staircase(n+1,s+1)

    elif n==0 and s==0:
        print("Not Draw!")

    return ""   

s=0
print(staircase(int(input("Enter Input : ")),s))