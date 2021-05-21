def selection_sort(arr):
    for start in range(len(arr) - 1):
        minInd = start
        for index in range(start, len(arr)):
            if arr[index] < arr[minInd]:
                minInd = index
        arr[start], arr[minInd] = arr[minInd], arr[start]

# array = [4,6,1,7,2,8,4,3,1,6,2,7,3,4,7,8,2,5,8,9,1,1,2]
# selection_sort(array)
# print(array)