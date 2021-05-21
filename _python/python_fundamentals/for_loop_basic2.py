# 1. Biggie Size
def biggie_size(list):
    for index in range(len(list)):
        if list[index] > 0:
            list[index] = "big"
    return list


# 2. Count Positives
def count_positives(list):
    pos_count = 0
    for index in range(len(list)):
        if list[index] > 0:
            pos_count += 1
    list[len(list) - 1] = pos_count
    return list


# 3. Sum Total
def sum_total(list):
    sum = 0
    for index in range(len(list)):
        sum += list[index]
    return sum


# 4. Average
def average(list):
    sum = 0
    for index in range(len(list)):
        sum += list[index]
    return sum / len(list)


# 5. Length
def length(list):
    return len(list)


# 6. Minimum
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for index in range(1, len(list)):
            if list[index] < min:
                min = list[index]
        return min


# 7. Maximum
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for index in range(1, len(list)):
            if list[index] > max:
                max = list[index]
        return max


# 8. Ultimate Analysis
def ultimate_analysis(list):
    if len(list) == 0:
        return False
    else:
        analysis = {}
        sum = list[0]
        min = list[0]
        max = list[0]

        for index in range(1, len(list)):
            sum += list[index]
            if list[index] < min:
                min = list[index]
            if list[index] > max:
                max = list[index]

        analysis["sumTotal"] = sum
        analysis["average"] = sum / len(list)
        analysis["minimum"] = min
        analysis["maximum"] = max
        analysis["length"] = len(list)

        return analysis


# 9. Reverse List
def reverse_list(list):
    for index in range(len(list) // 2):
        temp = list[index]
        list[index] = list[len(list) - index - 1]
        list[len(list) - index - 1] = temp
    return list


# print(biggie_size([-1, 3, 5, -5]))
# print(count_positives([-1, 1, 1, 1]))
# print(count_positives([1, 6, -4, -2, -7, -2]))
# print(sum_total([1, 2, 3, 4]))
# print(sum_total([6, 3, -2]))
# print(average([1, 2, 3, 4]))
# print(length([37, 2, 1, -9]))
# print(length([]))
# print(minimum([37, 2, 1, -9]))
# print(minimum([]))
# print(maximum([37, 2, 1, -9]))
# print(maximum([]))
# print(ultimate_analysis([37, 2, 1, -9]))
# print(reverse_list([37, 2, 1, -9]))
