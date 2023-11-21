from collections import deque
# Define your "TreeNode" Python class below


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing {} from {}".format(child_node.value, self.value))
        self.children = [child
                         for child in self.children
                         if child.value != child_node.value]
        
    def __repr__(self):
        return self.value
    
    
    def traverse(self):
        print("Traversing...")
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

    def __str__(self):
        stack = deque()
        stack.append([self, 0])
        level_str = "\n"
        prev_level = 0
        level = 0
        while len(stack) > 0:
            prev_level = level
            node, level = stack.pop()
            
            if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
                level_str += "   "*(level-1)+ "├─"
                
            elif level > 0:
                level_str += "   "*(level-1)+ "└─"


            level_str += str(node.value)
            level_str += "\n"
            level += 1
            for child in reversed(node.children):
                stack.append([child, level])

        return level_str
    
    def print_path(path):
        # If path is None, no path was found
        if path == None:
            print("No paths found!")

        # If a path was found, print path
        else:  
            print("Path found:")
            for node in path:
                print(node.value)


# root = TreeNode("CEO")
# first_child = TreeNode("Vice-President")
# second_child = TreeNode("Head of Marketing")
# third_child = TreeNode("Marketing Assistant")

# root.add_child(first_child)
# root.add_child(second_child)
# second_child.add_child(third_child)

# print(root)

# root.traverse()

sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]
three.children = [seven, six]

# print(sample_root_node)
