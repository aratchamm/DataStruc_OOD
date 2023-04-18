def x_serch(lst,key):
    lst.append(key)
    index = 0
    while key != lst[index]:
        index += 1
    lst.pop()
    if index >= len(lst):
        return -1
    if index > 0:
        lst[index-1], lst[index] = lst[index], lst[index-1]
    return index


inp = input("Enter Input : ").split("/")
ls = inp[0]
ke = inp[1]
lst = []
key=[]
for i in ls.split():
    lst.append(int(i))

for j in ke.split():
    key.append(int(j))

for x in range(len(key)):
    x_serch(lst,key[x])