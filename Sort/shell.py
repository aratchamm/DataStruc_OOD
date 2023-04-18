count = 0
def shellSort(arr):
    n = len(arr)
    gap = 8 // 2
    global count
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            count += 1
            while j >= gap and arr[j - gap] > temp:
                count += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return count
print("  Shell sort ")
arr = [int(x) for x in input("Enter some numbers : ").split(" ")]
round = shellSort(arr)
print()
print(arr)
print("Data comparison =  {}".format(round))