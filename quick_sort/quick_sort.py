
def get_pivot_index(num_list, start=0, end=None):
    def swap(num_list, idx1, idx2):
        temp = num_list[idx1]
        num_list[idx1] = num_list[idx2]
        num_list[idx2] = temp

    if end == None:
        end = len(num_list) - 1

    pivot = num_list[start]
    swapIndex = start

    for i in range(start, end + 1):
        print(num_list[i], i)
        if (pivot > num_list[i]):
            swapIndex += 1
            swap(num_list, i, swapIndex)

    swap(num_list, start, swapIndex)
    return swapIndex


def quick_sort(num_list, left=0, right=None):
    if right == None:
        right = len(num_list) - 1

    if left < right:
        pivot = get_pivot_index(num_list, left, right)
        quick_sort(num_list, left, pivot - 1)
        quick_sort(num_list, pivot + 1, right)

    return num_list


print(quick_sort([9, 4, 6, 12, 10, 1, 2, 5]))
