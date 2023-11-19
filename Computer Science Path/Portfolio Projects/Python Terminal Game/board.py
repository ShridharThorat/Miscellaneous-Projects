from random import randint, seed
from typing import Union
from collections import deque

seed(8)  # Set constant for controlled testing

number_to_cell = {
    "*": "mine",
    0: "empty",
}


def map_screen_to_board(pos: tuple[int, int], top_left_corner: tuple[int, int], cell_width: int, cell_height: int):
    """
    Maps a position on the screen to a cell on the board

    ### Args:
        - `pos` (tuple[int, int]): The position of the cell on the screen
        - `board` (list[list[Union[int, str]]]): A 2D array with rows for the y-axis and columns for the x-axis

    ### Returns:
        - A tuple(int, int) representing the location of the cell on the board
    """
    x, y = pos
    offset_x, offset_y = top_left_corner
    board_x = (x - offset_x) / (cell_width + 1)
    board_y = (y - offset_y) / (cell_height + 1)
    return (int(board_x), int(board_y))


def initialise_board(width: int = 9, height: int = 9, num_mines: int = 10):
    """ Initialises a board with `width` cells across and `height` cells vertically 
        that has `num_mines` mines

    ### Args:
        - `width` (int, optional): The number of cells across. Defaults to 9.
        - `height` (int, optional): The number of cells vertically. Defaults to 9.
        - `num_mines` (int, optional): The number of mines on the board. Defaults to 10.

    ### Returns:
        - A tuple where the first element is a A 2D array with rows for the y-axis and columns for the x-axis,    
          and the second element is a list of tuples representing the locations of the mines on the board.
            - Type: `Tuple[List[List[Union[str, int]]], List[Tuple[int, int]]]`:
    """

    # A board[y][x] is of size width x height
    board = [[0 for j in range(width)] for i in range(height)]
    revealed_board = [[False for j in range(width)] for i in range(height)]
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
    number_all_cells(mine_locations, board)

    return board, revealed_board, mine_locations


def number_all_cells(mine_locations: list[tuple[int, int]], board: list[list[Union[int, str]]]):
    """Numbers cells adjacent to mines on a board.

    ### Args:
        - mine_locations (list[tuple): The (x, y) coordinates of all mines on the board
        - board (list[list[Union[int, str]]]): A 2D array with rows for the y-axis and columns for the x-axis

    ### Returns:
        - Void. Modifies the given board
    """
    all_neighbours = set()
    for mine_cell in mine_locations:
        x, y = mine_cell
        mine_neighbours = find_specified_neighbours(mine_cell, int, board)
        for mine_neighbour in mine_neighbours:
            if mine_neighbour not in all_neighbours:  # Don't need to recalculate
                x, y = mine_neighbour
                # Need to recalculate the number of mines nearby since they're could be more than 1
                nearby_mines = find_specified_neighbours(
                    mine_neighbour, str, board)
                board[y][x] = len(nearby_mines)
                all_neighbours.add(mine_neighbour)


def find_specified_neighbours(location: tuple[int, int],
                            neighbour_type: Union[str, int],
                            board: list[list[Union[int, str]]],
                            n: int = 3):
    """
    Finds neighbours in a `n by n` area surrounding the cell at location on the board
        ```py
        # For example: A 3 by 3 area has 8 cells surrounding the cell at the specified location
        (y-1, x-1), (y-1, x), (y-1, x+1)
        (y,   x-1), (y  , x), (y  , x+1)
        (y+1, x-1), (y+1, x), (y+1, x+1)
        ```

    ### Args:
        - `location`: The `(x,y)` coordinations on the board -> found by `board[y][x]`
        - `neighbour_type`: 
            - If `int` then the function finds neighbouring cells. Useful when (x, y) is a mine
            - If `str` then it finds neighbouring mines. Useful when (x, y) is a numbered cell
        - `board`: a list of lists with `int`s (for cells) and `str`s (for mines). 
        - `n`: is the size of the entire sub-area being searched including the cell at `location` on the board
            - #### Note: defaults to 3
            - ### WARNING: n should be odd for a uniform area

    ### Returns:
        - A list of tuples(int, int) representing the locations for the neighbours. 
    """
    x, y = location

    if (n+1) % 2 != 0:
        print("ERROR: Invalid. n must be odd")
        raise ValueError("n must be odd")
    else:
        max_left_down = n//2
        max_right_up = max_left_down + 1  # + 1 since a range stops before the second value

    neighbours = []
    for y_adj in range(y - max_left_down, y + max_right_up):
        for x_adj in range(x - max_left_down, x + max_right_up):
            if valid_adjacent_cell(location, (x_adj, y_adj), board):
                if isinstance(board[y_adj][x_adj], neighbour_type):
                    neighbours.append((x_adj, y_adj))
    return neighbours


def find_all_connected_empty_cells(location: tuple[int, int],
                                board: list[list[Union[int, str]]],
                                n: int = 3):
    """
    Finds all numbered cells adjacent to the empty cell, searching in a `n by n` area surrounding each cell at a given location on the board    
    ### Args:
        - `location`: The `(x,y)` coordinations on the board of an empty cell-> found by `board[y][x]`
        - `board`: a list of lists with `int`s (for cells) and `str`s (for mines). 
        - `n`: is the size of the entire sub-area being searched including the cell at `location` on the board
            - #### Note: defaults to 3
            - ### WARNING: n should be odd for a uniform area and greater than 3 for a nonzero search

    ### Returns:
        - A list of tuples(int, int) representing the locations for connected numbered cells.
    """

    if (n+1) % 2 != 0:
        print("ERROR: Invalid. n must be odd")
        raise ValueError("n must be odd")
    else:
        max_left_down = n//2
        max_right_up = max_left_down + 1  # + 1 since a range stops before the second value

    connected_numbered_cells = set()
    connected_empty_cells = set()
    cells_to_check = deque()  # Operates as a stack -> LIFO

    connected_empty_cells.add(location)
    cells_to_check.appendleft(location)
    while len(cells_to_check) > 0:
        cell = cells_to_check.popleft()
        x, y = cell
        for y_adj in range(y - max_left_down, y + max_right_up):
            for x_adj in range(x - max_left_down, x + max_right_up):
                if valid_adjacent_cell(location, (x_adj, y_adj), board):
                    if board[y_adj][x_adj] == 0:
                        if (x_adj, y_adj) not in connected_empty_cells:
                            connected_empty_cells.add((x_adj, y_adj))
                            # Add the new neighbour to the queue
                            cells_to_check.appendleft((x_adj, y_adj))
                    else:
                        connected_numbered_cells.add((x_adj, y_adj))
    return set.union(connected_empty_cells, connected_numbered_cells)


def valid_adjacent_cell(current: tuple[int, int], adjacent: tuple[int, int], board: list[list[Union[int, str]]]):
    """Determines if an adjacent cell exists

    ### Args:
        - current (tuple[int, int]): The position of the cell being checked
        - adjacent (tuple[int, int]): The position of the cell adjacent to the current cell
        - board (list[list[Union[int, str]]]): A 2D array with rows for the y-axis and columns for the x-axis

    ### Returns:
        - True or False: `True` if the adjacent cell is within the bounds of the board and isn't the same cell. `False` otherwise
    """
    x, y = current
    x_adj, y_adj = adjacent
    not_beyond_left_corner = y_adj >= 0 and x_adj >= 0
    not_beyond_right_corner = y_adj < len(
        board) and x_adj < len(board[0])
    not_the_same_cell = (y_adj, x_adj) != (y, x)
    return not_beyond_left_corner and not_beyond_right_corner and not_the_same_cell


def move_mine(pos: tuple[int, int], board: list[list[Union[int, str]]], mine_locations: list[int]):
    """
    Moves a mine from one location to another while updating neighbouring cells 

    Uses:
        - Moving a mine if a user clicks a mine on the first try

    Returns:
        - False if a move is unsuccesful and True otherwise
    """
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
    """
    Finds a list of a mines for the `cells_to_update` and updates the values for cells

    Args:
        - `cells_to_update` is a list of coordinates of the cells to update on the `board`
        - `board` is a list of lists representing numbered `cells: int` and `mines: str`
    """
    for cell_coords in cells_to_update:
        x, y = cell_coords
        mines_nearby = find_specified_neighbours(cell_coords, str, board)
        board[y][x] = len(mines_nearby)


def print_board(board: list[list[Union[int, str]]], revealed_board: list[list[bool]] = None):
    """
    Prints a matrix representation of the board with `|` for the walls and one whitespace between elements

    ### Args:
        - board (list[list[Union[int, str]]]): A 2D array with rows for the y-axis and columns for the x-axis
        - revealed_board (list[list[bool]], optional): A board equivalent to `board` but with booleans describing whether a cell is revealed or not

    ### Returns:
        Void. Prints on the command line instead
    """
    if revealed_board is None:
        for row in board:
            print("| ", end='')
            for el in row:
                print(f"{el} ", end='')
            print("|")
        return

    for row in range(len(board[0])):
        print("| ", end='')
        for col in range(len(board)):
            if revealed_board[row][col]:
                print(f"{board[row][col]} ", end='')
            else:
                print("X ", end='')
        print("|")


def reveal_cell(cell_to_reveal: tuple[int, int], board: list[list[Union[int, str]]], revealed_board: list[list[bool]]):
    """Reveals the cell at `cell_to_reveal` on the board as well as the neighbouring cells if the cell is empty

    Args:
        cell_to_reveal (tuple[int, int]): The (x, y) coordinates of the cell to reveal on the board
        board (list[list[Union[int, str]]]): A 2D array with rows for the y-axis and columns for the x-axis
        revealed_board (list[list[bool]]): A 2D mirror of the board with booleans describing whether a cell is revealed or not
    """
    x, y = cell_to_reveal
    print()
    if revealed_board[y][x] == True:
        return

    if board[y][x] == "*":
        revealed_board[y][x] = True
        print_board(board, revealed_board)
        print("FAIL: You hit a mine")
    elif board[y][x] >= 1:
        revealed_board[y][x] = True
        print_board(board, revealed_board)
        print("Nice: You hit a cell with {} mines nearby".format(board[y][x]))
    else:
        connected_empty_cells = find_all_connected_empty_cells(
            cell_to_reveal, board)
        for empty in connected_empty_cells:
            x, y = empty
            revealed_board[y][x] = True
        print_board(board, revealed_board)
        print("Excellent: You hit an empty cell")
    print()


test, revealed, mine_locations = initialise_board(9, 9)
print_board(test)

cell = (2, 0)
reveal_cell(cell, test, revealed)

cell = (3, 3)
reveal_cell(cell, test, revealed)

# mine = (3, 0)
# reveal_cell(mine, test, revealed)

# x = 2
# y = 1
# mines_nearby, neighbours = find_specified_neighbours((x, y), str, test)
# print("Element ({},{}) has {} mines nearby".format(x+1, y+1, mines_nearby))
# print("Numbering cells")
# number_all_cells(test)
# print("Final: ")
# print_board(test)

# test_pos = (3, 0)
# print("Mine: {}".format(test_pos))
# neighbours = find_specified_neighbours(test_pos, int, test)
# print(len(neighbours))
# print(neighbours)

# print("Moving\n")
# move_mine((3, 0), test, mine_locations)
# print_board(test)
# print(map_screen_to_board((45+(4*9), 22), (45, 20), 3, 1))
