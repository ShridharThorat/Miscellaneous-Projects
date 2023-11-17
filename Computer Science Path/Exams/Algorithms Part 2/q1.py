def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    # Complete the code below
    middle_index = len(unsorted) // 2
    l_unsorted = unsorted[:middle_index]
    l_sorted = merge_sort(l_unsorted)

    r_unsorted = unsorted[middle_index:]
    r_sorted = merge_sort(r_unsorted)

    return merge(l_sorted, r_sorted)


def merge(left, right):
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right
    return result


print(merge_sort([2, 4, 3, 5, 1]))
