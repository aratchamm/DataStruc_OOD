def Findmin(l):
    if (len(l) == 1):
        return l[0]
    else:
        return min(l[0], Findmin(l[1:]))

inp = [int(i) for i in input("Enter Input : ").split()]
print(f"Min : {Findmin(inp)}")