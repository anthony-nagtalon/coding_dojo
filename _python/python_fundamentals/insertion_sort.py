def insertion_sort(arr):
    for start in range(1, len(arr)):
        for ind in range(start, 0, -1):
            if arr[ind - 1] > arr[ind]:
                arr[ind - 1], arr[ind] = arr[ind], arr[ind - 1]
            else:
                break;

array = [4,6,1,7,2,8,4,3,1,6,2,7,3,4,7,8,2,5,8,9,1,1,2]
insertion_sort(array)
print(array)