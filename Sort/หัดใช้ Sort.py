def Sorted(temp):
    for j in range(len(temp) -1):
        for i in range(len(temp) -1 ):
            if temp[i] > temp[i+1]:
                temp[i],temp[i+1] = temp[i+1],temp[i]


inp = [int(i) for i in input("Enter Input : ").split()]
temp = []
for i in inp:
    temp.append(i)
Sorted(temp)

if temp == inp:
    print("Yes")
else:
    print("No")