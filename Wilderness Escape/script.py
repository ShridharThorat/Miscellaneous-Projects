######
# TREENODE CLASS
class Treenode:

    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        if node.story_piece not in self.choices:
            self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice.strip() not in ["1", "2"]:
                choice = input("Enter 1 or 2 to continue the story: ")
            else:
                # -1 since index starts at 0
                chosen_index = int(choice.strip()) - 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child
######


######
# VARIABLES FOR TREE
story_root_val = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""
choice_a_val = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""

choice_a_1_val = """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""

choice_a_2_val = """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
"""

choice_b_val = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""

choice_b_1_val = """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""

choice_b_2_val = """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""


story_root = Treenode(story_root_val)
choice_a = Treenode(choice_a_val)
choice_a_1 = Treenode(choice_a_1_val)
choice_a_2 = Treenode(choice_a_2_val)
choice_b_1 = Treenode(choice_b_1_val)
choice_b_2 = Treenode(choice_b_2_val)

choice_b = Treenode(choice_b_val)
story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
######

######
# TESTING AREA
user_choice = input("What is your name? ")
print(user_choice)
print("Once upon a time…")
# print(story_root.story_piece)

story_root.traverse()
######
