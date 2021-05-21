def bubble_sort(arr):
    for end in range(len(arr)-1, -1, -1):
        for index in range(end):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    
# array = [4,6,1,7,2,8,4,3,1,6,2,7,3,4,7,8]
# bubble_sort(array)
# print(array)

