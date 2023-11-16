class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Add code below
    def insert_end(self,value):
        new_node = Node(value)
        if self.head_node == None:
            self.head_node = new_node
            return
        
        # Find the last node
        current_node = self.head_node
        while current_node.get_next_node() != None:
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def print(self):
        current_node = self.get_head_node()
        while current_node is not None:
            print(f"{current_node.get_value()}", end=" ")
            current_node = current_node.get_next_node()
        print()


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


ll = LinkedList(3)
ll.print()
ll.insert_beginning(2)
ll.print()
ll.insert_end(4)
ll.print()
