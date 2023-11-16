class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert(self, pos, new_value):
        if pos == 0:
            self.add_to_head(new_value)
        else:
            current_node = self.head_node
            for i in range(pos):
                if current_node.get_next_node() is None:
                    self.add_to_tail(new_value)
                    return
                current_node = current_node.get_next_node()

            new_node = Node(new_value)
            # Add code below
            before_new_node = current_node.get_prev_node()
            
            # First make the new_node point to others
            new_node.set_next_node(current_node)
            new_node.set_prev_node(before_new_node)
            # Reset pointers to existing nodes
            before_new_node.set_next_node(new_node)
            current_node.set_prev_node(new_node)

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail

    def print(self):
        current_node = self.head_node
        while current_node is not None:
            print(f"{current_node.get_value()}", end=" ")
            current_node = current_node.get_next_node()
        print()


class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value


dll = DoublyLinkedList()
dll.add_to_head('a')
dll.add_to_tail('c')
dll.print()
dll.insert(1, 'b')
dll.print()
