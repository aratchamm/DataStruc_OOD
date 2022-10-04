'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

ให้เขียน Recursive หาค่า Min ของ Input
'''

def Findmin(l):
    if (len(l) == 1):
        return l[0]
    else:
        return min(l[0], Findmin(l[1:]))

inp = [int(i) for i in input("Enter Input : ").split()]
print(f"Min : {Findmin(inp)}")