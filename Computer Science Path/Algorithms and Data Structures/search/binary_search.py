# define binary_search()
def binary_search(sorted_list, target):
    if not sorted_list:
        return "Value not Found"

    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx

    elif mid_val < target:
        right_half = sorted_list[mid_idx+1:]  # Don't include mid_idx
        result = binary_search(right_half, target)
        if result == "Value not Found":
            return result
        return result + mid_idx + 1

    elif mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)


def binary_search_iterative(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)

    # fill in the condition for the while loop
    while left_pointer < right_pointer:
        # calculate the middle index using the two pointers
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
            # set the right_pointer to the appropriate value
            right_pointer = mid_idx
        if target > mid_val:
            # set the left_pointer to the appropriate value
            left_pointer = mid_idx + 1

    return "Value not in list"


def binary_search_pointers(sorted_list, left_pointer, right_pointer, target):
    # this condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return "value not found"

    # We calculate the middle index from the pointers now
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # we reduce the sub-list by passing in a new right_pointer
        return binary_search_pointers(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        # we reduce the sub-list by passing in a new left_pointer
        return binary_search_pointers(sorted_list, mid_idx + 1, right_pointer, target)


# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 17))

values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search_pointers(values, start_of_values, end_of_values, 288)
print("element {0} is located at index {1}".format(288, result))

# test cases
print(binary_search_iterative([5, 6, 7, 8, 9], 9))
print(binary_search_iterative([5, 6, 7, 8, 9], 10))
print(binary_search_iterative([5, 6, 7, 8, 9], 8))
print(binary_search_iterative([5, 6, 7, 8, 9], 4))
print(binary_search_iterative([5, 6, 7, 8, 9], 6))
