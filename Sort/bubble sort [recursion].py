def Bubble(arr,index = 0):
    if index == len(arr)-1:
        return
    if arr[index] > arr[index+1]:
        arr[index],arr[index+1] = arr[index+1],arr[index]
        Bubble(arr,0)
    else:
        Bubble(arr,index+1)
    

inp = [int(i) for i in input("Enter Input : ").split()]
Bubble(inp)
print(inp)