# 1. Countdown
def countdown(num):
    list = []
    for val in range(num, -1, -1):
        list.append(val)
    return list

#2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

#3. First Plus Length
def first_plus_length(list):
    return(list[0] + len(list))

#4. Values Greater Than Second
def values_greater_than_second(list):
    if(len(list) < 2):
        return False
    
    newList = []
    min = list[1]

    for index in range(len(list)):
        if(list[index] > min):
            newList.append(list[index])
    
    print("New List Size:", len(newList))
    return newList

#5. This Length, That Value
def length_and_value(size, value):
    list = []
    for index in range(size):
        list.append(value)
    return list