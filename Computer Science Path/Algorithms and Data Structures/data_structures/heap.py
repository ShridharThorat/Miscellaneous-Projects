from random import randrange


class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    # DO NOT CHANGE!
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        """Determines if a node at index 'idx' has a left child or right child."""
        return self.left_child_idx(idx) <= self.count
    # END OF HEAP HELPER METHODS

    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        """Fixes the heap relationship from a node at the end of the list to the root.
        """
        print("Heapifying up")
        # add your code below
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if child > parent:
                print(f"swapping {parent} with {child}")
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            idx = self.parent_idx(idx)
        print("HEAP RESTORED! {}".format(self.heap_list))

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            print("Heapifying down!")
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            if child > parent:
                self.heap_list[larger_child_idx] = parent
                self.heap_list[idx] = child

            idx = larger_child_idx
        # add code below
        print("HEAP RESTORED! {}".format(self.heap_list))

    # If we remove the first element we lose the binary tree relationship
    # A solution to this to to just take the last element in the heap
    # which is guaranteed to be a leaf, and put it at the top
    # We can then just heapify down to restore the heap
    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None

        max_val = self.heap_list[1]
        print(f"Removing {max_val} from {self.heap_list}")
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print(f"Last element moved to first: {self.heap_list}")
        self.heapify_down()
        return max_val

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                print("Left child " + str(left_child) +
                      " is larger than right child " + str(right_child))
                return self.left_child_idx(idx)
            else:
                print("Right child " + str(right_child) +
                      " is larger than left child " + str(left_child))
                return self.right_child_idx(idx)


def heapsort(lst):
    print("\nSorting: {0}".format(lst))
    sort = []
    max_heap = MaxHeap()
    for idx in lst:
        max_heap.add(idx)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)
    return sort


my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
# print the sorted list
print("\nSorted list below!")
print(sorted_list)

# import random number generator
# import heap class

# make an instance of MaxHeap
max_heap = MaxHeap()

# populate max_heap with random numbers
random_nums = [randrange(1, 11) for n in range(6)]
for el in random_nums:
    max_heap.add(el)


# test it out, is the maximum number at index 1?
print(max_heap.heap_list)
