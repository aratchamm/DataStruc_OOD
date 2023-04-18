def Bubble(arr):
    for i in  range(len(arr)):
        for k in range(len(arr)-1):
            if arr[k] > arr[k+1]:
                arr[k],arr[k+1] = arr[k+1],arr[k]
    return print(inp)

inp = [int(i) for i in input("Enter Input : ").split()]
Bubble(inp)