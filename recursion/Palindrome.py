'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่
'''

def  isPalindrome(s):
   if len (s) <= 1:
      return True
      
   return  s[0] == s[len(s)-1] and isPalindrome(s[1:len(s)-1]) 

inp = input("Enter Input : ")

if   isPalindrome(inp):
      print (f"'{inp}' is palindrome")
else :
      print (f"'{inp}' is not palindrome")