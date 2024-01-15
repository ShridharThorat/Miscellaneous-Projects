import random


# comparison_function lets us pass a custom function
# for ordering 2 books
def bubble_sort(arr, comparison_function):
    swaps = 0
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(arr) - 1):
            # if arr[idx] > arr[idx + 1]:
            if comparison_function(arr[idx], arr[idx + 1]):
                sorted = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print("Bubble sort: There were {0} swaps".format(swaps))
    return arr

def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
    sum_author_book_a = len(book_a['author_lower']) + len(book_a['title_lower'])
    sum_author_book_b = len(book_b['author_lower']) + len(book_b['title_lower'])
    return sum_author_book_a > sum_author_book_b

def quicksort(list, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    less_than_pointer = start
    for i in range(start, end):
        # if pivot_element > list[i]:
        if comparison_function(pivot_element, list[i]):
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    quicksort(list, start, less_than_pointer - 1, comparison_function)
    quicksort(list, less_than_pointer + 1, end, comparison_function)
