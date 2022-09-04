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