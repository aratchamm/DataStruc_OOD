# เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป

import sys

print('*** Fun with Drawing ***')
num = int(input("Enter input : "))

if(num<2):
  print('ERROR! you must to input more than 1')
  sys.exit()

for row in range((num*3)-2):  
    for col in range(num+1):  
        #if (row==0 and (col==(num-1))):  
        #    print("*",end="") 
        if ((col+row)==(num-1)):
            print("*",end="")

        else:  
            print(end="-")  
    print()