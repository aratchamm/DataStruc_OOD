# โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด
# ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ

import sys

print('*** Election ***')
i = int(input("Enter a number of voter(s) : "))
arr = [int(i) for i in input().split()]

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        if(i<=20):
            curr_frequency = List.count(i)
        
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i
        
        
    if (i<0 or i>20) :
       print('*** No Candidate Wins ***')
       sys.exit()
 
    return num  

print(most_frequent(arr))