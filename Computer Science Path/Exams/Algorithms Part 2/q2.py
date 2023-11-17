from random import randrange


def quicksort(list, start, end):
    if start >= end:
        return

    pivot_ptr = randrange(start, end + 1)
    pivot_element = list[pivot_ptr]

    list[end], list[pivot_ptr] = list[pivot_ptr], list[end]
    less_than_ptr = start

    for i in range(start, end):
        if list[i] < pivot_element:
            list[i], list[less_than_ptr] = list[less_than_ptr], list[i]
            less_than_ptr += 1

    list[end], list[less_than_ptr] = list[less_than_ptr], list[end]

    # Add code below
    l_sort = quicksort(list,start,less_than_ptr-1)
    r_sort = quicksort(list,less_than_ptr+1,end)


l = [4, 8, 2, 5, 1, 9, 0, 7, 3, 6]
quicksort(l, 0, 9)
print(l)
