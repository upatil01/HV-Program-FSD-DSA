def __insertionSort__(arr):
    for i in range(1, len(arr)):
        
        j = i-1
        while(j >= 0 and arr[i] < arr[j]):
            arr[j+1] = arr[j]
            j -=1

        arr[j+1] = arr[i]

arr = [25,24,26,5,8]
print(arr)
__insertionSort__(arr)
print(arr)