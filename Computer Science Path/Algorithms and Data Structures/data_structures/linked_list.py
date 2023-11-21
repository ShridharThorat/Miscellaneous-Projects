class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
    #Fill in Function
    def find_max(self):
        #Write Code Here
        current_node = self.head_node
        maximum = current_node.get_value()
        while current_node != None:
            current_node = current_node.get_next_node()
            if current_node != None and current_node.get_value() != None:
                if current_node.get_value() > maximum:
                    maximum = current_node.get_value()

        return maximum
    
    def sort_linked_list(self):
        print("The original linked list is:\n{0}".format(self.stringify_list()))
        new_linked_list = LinkedList()
        #Write Code Here!
        maximum = self.find_max()
        new_linked_list.insert_beginning(maximum)
        self.remove_node(maximum)
        while self.head_node != None:
            maximum = self.find_max()
            new_linked_list.insert_beginning(maximum)
            self.remove_node(maximum)

        return new_linked_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    @staticmethod
    def swap_nodes(input_list, val1, val2):
        if val1 == val2:
            print("Elements are the same - no swap needed")
            return

        node1 = input_list.head_node
        node2 = input_list.head_node
        node1_prev = None
        node2_prev = None

        # Find the node with val1 and its parent
        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        # Find the node with val2 and its parent
        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        # If the node isn't found
        if (node1 is None or node2 is None):
            print("Swap not possible - one or more element is not in the list")
            return

        # Swap node1 and node2 by changing the link of their parent's
        if node1_prev is None:
            input_list.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            input_list.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        # Update pointers of node1 and node2
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

    # Complete this function:
    @staticmethod
    def nth_last_node(linked_list, n):
        nth_last_node = None
        count = 1
        tail = linked_list.head_node
        while tail:
            tail = tail.get_next_node()
            count += 1

            # When the difference between the tail to the head is n
            # > since we want this to execute until tail is none
            if count >= n + 1:
                if nth_last_node == None:
                    nth_last_node = linked_list.head_node
                else:
                    nth_last_node = nth_last_node.get_next_node()
        return nth_last_node

    # Complete this function:
    def find_middle(linked_list):
        fast_node = linked_list.head_node
        slow_node = linked_list.head_node
        while fast_node != None:
            fast_node = fast_node.get_next_node()
            if fast_node != None:
                fast_node = fast_node.get_next_node()
                slow_node = slow_node.get_next_node()
        return slow_node

    @staticmethod
    def generate_test_linked_list():
        linked_list = LinkedList()
        for i in range(50, 0, -1):
            linked_list.insert_beginning(i)
        return linked_list


# Test your code by uncommenting the statements below - did your list print to the terminal?
# ll = LinkedList(5)
# ll.insert_beginning(70)
# ll.insert_beginning(5675)
# ll.insert_beginning(90)
# print(ll.stringify_list())
test_list = LinkedList.generate_test_linked_list()

# print("Before swapping 9 and 5")
# print(ll.stringify_list())
# LinkedList.swap_nodes(ll, 9, 5)
# print("After swapping 9 and 5")
# print(ll.stringify_list())

# Use this to test your code:
# print(test_list.stringify_list())
nth_last = LinkedList.nth_last_node(test_list, 4)
middle_node = LinkedList.find_middle(test_list)
# print(nth_last.value)
# print(middle_node.value)

# Sorting
#Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(ll.sort_linked_list().stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(ll_2.sort_linked_list().stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(ll_3.sort_linked_list().stringify_list()))

#Runtime
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))