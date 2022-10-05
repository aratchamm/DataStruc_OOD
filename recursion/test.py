'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
หาลำดับ Fibonacci ของ input ที่รับเข้ามาโดยใช้ Recursive

F1 = 1, F2 = 1, เมื่อ n ≥ 3 Fn = Fn−1 + Fn− 2 
'''

def Fibo(num):
    if num == 1 or num == 2:
        return 1
    elif num >= 3:
        return Fibo(num-1) + Fibo(num-2)

inp = int(input("Enter Input : "))
print(f"fibo({inp}) = {Fibo(inp)}")