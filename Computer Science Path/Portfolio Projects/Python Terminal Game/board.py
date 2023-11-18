from random import randint, seed
from typing import Union
seed(8)  # Set constant for controlled testing

number_to_cell = {
    -1: "mine",
    0: "empty",
}


def createBoard(width: int = 9, height: int = 9, num_mines: int = 10):
    # A board[x][y] is of size width x height
    board = [[0 for j in range(width)] for i in range(height)]
    num_placed_mines = 0
    mine_locations = []

    # Place mines on the board
    while num_placed_mines < num_mines:
        x = randint(0, width-1)
        y = randint(0, height-1)
        if (x, y) not in mine_locations:
            board[y][x] = "*"
            mine_locations.append((x, y))
        num_placed_mines += 1

    # Determine the number of neighbouring mines for any given cell

    return board, mine_locations


def number_all_cells(board: list[list[Union[int, str]]]):
    '''
    Numbers all cells on the board with the number of adjacent mines. 

    Returns:
        - Void. Modifies the given board
    '''
    for y in range(len(board)):  # For each row
        for x in range(len(board[0])):  # For each column
            # If we see a mine, ignore it

            if board[y][x] == "*":  # Not a mine
                continue
            # Otherwise do our tests:
            # print(f"\tColumn: {x+1}", end='')

            # Every Element has 8 surrounding cells
            # (y-1, x-1), (y-1, x), (y-1,x+1)
            # (y,   x-1), (y  , x), (y,x+1)
            # (y+1, x-1), (y+1, x), (y+1,x+1)
            mines_nearby = find_specified_neighbours((x, y), str, board)

            # Once the 3x3 area has been explored, change the cell value
            # if mines_nearby > 0:
            #     print(": has {} mines nearby".format(mines_nearby))
            # else:
            #     print("")
            board[y][x] = len(mines_nearby)

            # Element in edge -> check 2 sides


def find_specified_neighbours(location: tuple[int,int], neighbour_type: Union[str, int], n:int, board: list[list[Union[int, str]]]):
    '''
    Finds neighbours in a `n by n` area surrounding the cell at location on the board
        Every Element has 8 surrounding cells. Some may or may not exist        
        such as if the cell is in a corner or an edge
        ```py
        (y-1, x-1), (y-1, x), (y-1,x+1)
        (y,   x-1), (y  , x), (y,x+1)
        (y+1, x-1), (y+1, x), (y+1,x+1)
        ```

    ### Args:
        - `location`: The `(x,y)` coordinations on the board -> found by `board[y][x]`
        - `neighbour_type`: 
            - If `int` then the function finds neighbouring cells. 
            - If `str` then it finds neighbouring mines
        - `n`: is the size of the entire sub-area being searched including the cell at `location` on the board
            - WARNING:: n must be odd
        - `board`: a list of lists with `int`s (for cells) and `str`s (for mines). 
        
    ### Returns:
        - A list of tuples(int, int) representing the locations for the neighbours. 
    '''
    x, y = location
    
    if (n+1)%2 != 0:
        print("ERROR: Invalid. n must be odd")
        return None 
    
    # Looking in a 3x3 area the item all elements
    neighbours = []
    for y_neighbour in range(y-1, y+2):
        for x_neighbour in range(x-1, x+2):
            not_in_left_corner = y_neighbour >= 0 and x_neighbour >= 0
            not_in_right_corner = y_neighbour < len(board) and x_neighbour < len(board[0])
            not_the_same_cell = (y_neighbour, x_neighbour) != (y, x)
            if not_in_left_corner and not_in_right_corner and not_the_same_cell:
                if isinstance(board[y_neighbour][x_neighbour], neighbour_type):
                    neighbours.append((x_neighbour, y_neighbour))
    return neighbours


def move_mine(pos: tuple[int, int], board: list[list[Union[int, str]]], mine_locations: list[int]):
    '''
    Moves a mine from one location to another while updating neighbouring cells 

    Uses:
        - Moving a mine if a user clicks a mine on the first try

    Returns:
        - False if a move is unsuccesful and True otherwise
    '''
    if pos not in mine_locations:
        # print("WARNING: the location {} doesn't contain a mine".format(pos)) # Just for testing
        return False

    width = len(board[0])
    height = len(board)
    pos_x, pos_y = pos

    # Get the neighbours for the mine to move
    cells_to_update = find_specified_neighbours((pos_x, pos_y), int, board)
    x = randint(0, width-1)
    y = randint(0, height-1)
    new_mine_neighbours = []
    if (x, y) not in mine_locations:  # We can move it
        new_mine_neighbours = find_specified_neighbours(
            (pos_x, pos_y), int, board)
        print("Mine moved from {} to {}".format(pos, (x, y)))
        board[y][x] = "*"
        board[pos[1]][pos[0]] = 0
    cells_to_update += new_mine_neighbours
    # Update just the required cells
    number_specific_cells(cells_to_update, board)

    print("Mine exists")


def number_specific_cells(cells_to_update: list[tuple[int, int]],  board: list[list[Union[int, str]]]):
    '''
    Finds a list of a mines for the `cells_to_update` and updates the values for cells

    Args:
        - `cells_to_update` is a list of coordinates of the cells to update on the `board`
        - `board` is a list of lists representing numbered `cells: int` and `mines: str`
    '''
    for cell_coords in cells_to_update:
        x, y = cell_coords
        mines_nearby = find_specified_neighbours(cell_coords, str, board)
        board[y][x] = len(mines_nearby)


def printBoard(board: list[list[Union[int, str]]]):
    '''
    Prints a matrix representation of the board with `|` for the walls and one whitespace between elements
    Returns:
        Void. Prints on the command line instead
    '''
    for row in board:
        print("| ", end='')
        for el in row:
            print(f"{el} ", end='')
        print("|")


test, mine_locations = createBoard(9, 9)
printBoard(test)
# x = 2
# y = 1
# mines_nearby, neighbours = find_specified_neighbours((x, y), str, test)
# print("Element ({},{}) has {} mines nearby".format(x+1, y+1, mines_nearby))
print("Numbering cells")
number_all_cells(test)
print("Final: ")
printBoard(test)

test_pos = (3, 0)
print("Mine: {}".format(test_pos))
neighbours = find_specified_neighbours(test_pos, int, test)
print(len(neighbours))
print(neighbours)

print("Moving\n")
move_mine((3, 0), test, mine_locations)
printBoard(test)
