Bubble sort-
def __bubblesort__(arr):
    length = len(arr) 
    for i in range(length):
        for j in range(0, length-i-1):
            if arr [j] > arr [j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

arr = [4,2,60,13,15,1]

__bubblesort__(arr)
print(arr)

