import math


def merge(list1, list2):
    index1 = 0
    index2 = 0
    merged_list = []

    while (index1 < len(list1)) and (index2 < len(list2)):
        if list1[index1] <= list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1

    while index1 < len(list1):
        merged_list.append(list1[index1])
        index1 += 1

    while index2 < len(list2):
        merged_list.append(list2[index2])
        index2 += 1

    return merged_list


def merge_sort(list):
    if len(list) <= 1:
        return list

    middleIndex = math.floor(len(list) / 2)
    left = merge_sort(list[:middleIndex])
    right = merge_sort(list[middleIndex:])
    return merge(left, right)


print(merge_sort([3, 5, 32, 6, 12, 4, 1, 78]))
