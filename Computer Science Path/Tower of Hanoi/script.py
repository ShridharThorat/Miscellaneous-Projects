from stack import Stack
print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = 0
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    stacks[0].push(i)

num_optimal_moves = 2**(num_disks-1)
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))


# Get User Input
def get_input():
    choices = [
        i.get_name()[0].upper() for i in stacks
    ]
    while True:
        # Display the choice
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {} for {}".format(letter, name))
        user_input = input(" ")

        # Determine the choice
        if user_input in choices:
            for i in range(len(stacks)):
                if choices[i][0].upper() == user_input:
                    return stacks[i]
                # prevent need for shift key
                elif choices[i][0].lower() == user_input:
                    return stacks[i]


# Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()

    # Ask for input
    while (True):
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        # Can't move from an empty stack
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again. Tower empty")

        elif to_stack.is_empty() or (from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:  # only thing left is an ->
            print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}".format(
    num_user_moves, num_optimal_moves))
