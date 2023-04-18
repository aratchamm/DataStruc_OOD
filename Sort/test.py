def x_sort(in_list):
    lst = in_list.copy()
    for i in range(len(lst)):
        swapped = False
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
                swapped = True
                print(lst)
        if not swapped:
            break
    return lst


inp = input("Enter lst = ").split()
x_sort(inp)