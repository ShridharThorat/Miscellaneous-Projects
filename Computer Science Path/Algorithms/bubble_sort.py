nums = [5, 2, 9, 1, 5, 6]


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


# define bubble_sort():
def bubble_sort(arr):
    num_iterations = 0
    for item in arr:
        for i in range(len(arr)-1):
            num_iterations += 1
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
    print("Num iterations: {}".format(num_iterations))


# Each iteration adds another value to the end of the list
def bubble_sort_optimised(arr):
    num_iterations = 0
    count = 0
    for item in arr:
        num_iterations += 1
        for i in range(len(arr)-num_iterations):
            count += 1
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)

    print("Num iterations: {}".format(count))


# Same as above but different style
def bubble_sort_optimised_2(arr):
    iteration_count = 0
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


# test statements
print("Pre-Sort: {0}".format(nums))
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))
bubble_sort_optimised(nums)
print("Post-Sort: {0}".format(nums))
bubble_sort_optimised_2(nums)
print("Post-Sort: {0}".format(nums))
