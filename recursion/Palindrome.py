'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่
'''

def palin(char):
    if len(char) != 0:
        if char[0] == char[len(char)-1]:
                return palin(char[1:len(char)-1])
        else:
            return "is not palindome"
    else:
        return "is palindome" 


inp=input("Enter Input : ")
char=[]
for i in inp:
    char.append(i)

print(f"'{inp}' {palin(char)}")