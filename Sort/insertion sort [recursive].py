def Sorted(l,ls=[],i=0):
    if len(ls) == 0:
        ls.append(l.pop(0))
    if len(ls) == i or l[0] <= ls[i]:
        ls.insert(i,l.pop(0))
        print(f"insert {ls[i]} at index {i} : {ls}",end=" ")
        if len(l) == 0:
            return ls
        print(l)
        return Sorted(l,ls)
    else:
        return Sorted(l,ls,i+1)

    

inp = [int(i) for i in input("Enter Input : ").split()]
s = Sorted(inp)
print("\nsorted")
print(s)