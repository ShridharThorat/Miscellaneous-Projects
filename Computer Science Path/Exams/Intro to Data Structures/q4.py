from q1 import Node


class Stack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def pop(self):
        if self.is_empty():
            return None

        # Add code below
        removed_value = self.top_node.get_value()
        new_top = self.top_node.get_next_node()
        if self.size == 1:
            self.top_node = None
        else:            
            self.top_node = new_top
        self.size -= 1
        return removed_value

    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_node)
        self.top_node = item
        self.size += 1

    def peek(self):
        if not self.is_empty():
            return self.top_node.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0


s = Stack()
s.push(1)
print("Pushed value: 1")
print("Output of peek: " + str(s.peek()))
s.push(2)
print("Pushed value: 2")
print("Output of pop: " + str(s.pop()))
