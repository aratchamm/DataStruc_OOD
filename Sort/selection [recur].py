def select(arr,index=0):
    if index == len(arr)-1:
        return
    index_min = FindMin(arr,index)
    arr[index],arr[index_min] = arr[index_min],arr[index]
    print(arr)
    select(arr,index+1)

def FindMin(arr,index):
    if index == len(arr)-1:
        return index
    temp_min = FindMin(arr,index+1)
    if arr[index] < arr[temp_min]:
        return index
    else:
        return temp_min

inp = [int(i) for i in input("Enter Input : ").split()]
select(inp)
print(inp)