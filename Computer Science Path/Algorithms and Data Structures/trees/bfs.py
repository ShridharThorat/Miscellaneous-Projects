from collections import deque
from tree import TreeNode

# Breadth-first search function


def bfs(root_node, goal_value):

    # initialize frontier queue
    path_queue = deque()

    # add root path to the frontier
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue: # While there a paths to find in our queue
        current_path = path_queue.pop() # Get the first path
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")

        # check if the goal node is found
        if current_node.value == goal_value:
            return current_path

        # add paths to children to the  frontier
        for child in current_node.children:            
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    # return an empty path if goal not found
    return None


sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)
goal_path = bfs(sample_root_node, "Fluffy.jpg")
if goal_path is None:
    print("No path found")
else:
    print("Path found")
    for node in goal_path:
        print(node.value)
