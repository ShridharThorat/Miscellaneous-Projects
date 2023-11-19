import csv
from random import randint, seed, sample
from typing import Union
from collections import deque

seed(8)


class Minesweeper:
    screen_width = None
    screen_height = None
    vertical_centre = None
    horizontal_centre = None

    start_instructions = {
        0: ["Welcome to Terminal Minesweeper"],
        1: ["Easy Mode"],
        2: ["Hard Mode"],
        3: ["Expert Mode"],
        4: ["Exit"]
    }

    def __init__(self, definitions_file="definitions.csv", difficulties_file="difficulties.csv", game_board=None):
        self.definitions_file = definitions_file
        self.difficulties_file = difficulties_file
        self.difficulties = Minesweeper._read_file(difficulties_file)
        self.game_board = None

    def initialise_board(self, difficulty: str, definitions_file: str = "definitions.csv"):
        self.game_board = Board(
            difficulty, self.difficulties, self.definitions_file)

    @staticmethod
    def _read_file(filename):
        try:
            definitions = open(filename)
            data = csv.DictReader(definitions)
            formated_data = Minesweeper._unpack_dictReader(data)
            return formated_data
        except Exception as e:
            print(
                f"ERROR: File doesn't exist. Check if you are in the working directory\n\t{e}")

    @staticmethod
    def _unpack_dictReader(dictReader):
        formated_data = {}
        for dictionary in dictReader:
            id_key = list(dictionary.keys())[0]
            identifier = dictionary.pop(id_key)
            formated_data[identifier] = {}
            for key, value in dictionary.items():
                if isinstance(value, str):
                    value = value.strip()
                    if value.strip().lower() == "none":
                        value = " "
                if key.strip() == "board_size":
                    value = value.strip()
                    width, height = value.split(";")
                    width = width.split("(")[1].strip()
                    height = height.split(")")[0].strip()
                    value = (int(width), int(height))
                elif key.strip() == "mines":
                    value = int(value)

                new_data = {key.strip(): value}
                formated_data[identifier].update(new_data)

        return formated_data


class Cell:

    def __init__(self, states: dict[str, Union[str, int]] = None):
        if states is not None:
            self.character = states["hidden"]["character"]
        else:
            self.character = 0
        self.revealed = False
        self.flagged = False
        self.is_mine = False
        self.mines_nearby = 0

    def set_mines_nearby(self, mines_nearby: int):
        if not self.is_mine and not self.flagged:
            self.character = mines_nearby
        self.mines_nearby = mines_nearby

    def set_numbered(self):
        self.is_mine = False
        self.character = 0

    def set_mine(self, states: dict[str, dict[str, int]]):
        if not self.is_mine:
            self.is_mine = True
            self.character = states["mine"]["character"]

    def reveal_cell(self, states: dict[str, dict[str, int]]):
        if not self.revealed:
            self.revealed = True
            if self.flagged:
                return  # We don't want to reveal a flagged cell until it's unflagged
            elif self.is_mine:
                self.set_mine(states)
                
            return 1
        return 0

    def __repr__(self):
        if self.is_mine:
            return f"{self.character}"
        else:
            return f"{self.mines_nearby}"


class Board:

    def __init__(self, difficulty: str, difficulties: dict[str, tuple[int, int]], cell_definitions_file: str = "definitions.csv",):
        self.cell_definitions_file = cell_definitions_file
        self.states = Minesweeper._read_file(self.cell_definitions_file)
        self.difficulty = difficulty
        self.width, self.height = difficulties[difficulty]['board_size']
        self.num_mines = difficulties[difficulty]['mines']
        self.flags = 0
        self.mine_locations = []
        self.revealed_cells_count = 0
        self.max_revealed_cells = self.width * self.height
        self.board = None
        self.board = self.create_board()

    def __str__(self):
        """
        Prints a matrix representation of the board with `|` for the walls and one whitespace between elements
        """
        board_info = "Board: difficulty: {}, size: ({},{}), mines: {}".format(
            self.difficulty, self.width, self.height, self.num_mines)
        board_str = board_info + "\n"
        for row in self.board:
            board_str += "| "
            for cell in row:
                if cell.revealed:
                    if cell.is_mine or cell.flagged:
                        board_str += f"{cell.character}" + " "
                    else:
                        board_str += f"{cell.mines_nearby}" + " "
                else:
                    board_str += f"{self.states['hidden']['character']}" + " "
            board_str += "|\n"

        return board_str

    def flag_cell(self, location: tuple[int, int], states: dict[str, dict[str, int]]):
        cell = self.board[location[1]][location[0]]
        if not cell.revealed:
            if not cell.flagged and self.flags < self.num_mines:
                cell.revealed = True  # Since we want to see the character on the screen
                cell.flagged = True
                cell.character = states["flag"]["character"]
                self.revealed_cells_count += 1
                self.flags += 1

    def unflag_cell(self, location: tuple[int, int],  states: dict[str, dict[str, int]]):
        cell = self.board[location[1]][location[0]]
        if cell.flagged and self.flags > 0:
            cell.revealed = False
            cell.flagged = False
            self.revealed_cells_count -= 1
            self.flags -= 1
            if cell.is_mine:
                cell.character = states["mine"]["character"]
            else:
                cell.character = cell.mines_nearby

    def create_board(self):
        """ Initialises a board with `self.width` cells across and `self.height` cells vertically 
            that has `self.num_mines` mines. Add (x, y) coordinates for all mines

        ### Returns:
            - A board represented by A 2D array with rows for the y-axis and columns for the x-axis
                - Type: `Tuple[List[List[Union[str, int]]]`:
        """
        self.board = [[Cell() for _ in range(self.width)]
                      for _ in range(self.height)]

        num_placed_mines = 0

        # Place mines on the board
        while num_placed_mines < self.num_mines:
            x = randint(0, self.width-1)
            y = randint(0, self.height-1)
            if (x, y) not in self.mine_locations:
                self.board[y][x].set_mine(self.states)
                self.mine_locations.append((x, y))
            num_placed_mines += 1
        self.number_all_cells()
        return self.board

    def number_all_cells(self):
        """Numbers cells adjacent to mines on a board.

        ### Returns:
            - Void. Modifies the given board
        """
        all_neighbours = set()
        for mine_cell in self.mine_locations:
            x, y = mine_cell
            mine_neighbours = self.find_specified_neighbours(
                mine_cell, "numbered")
            for mine_neighbour in mine_neighbours:
                if mine_neighbour not in all_neighbours:  # Don't need to recalculate
                    x, y = mine_neighbour
                    # Need to recalculate the number of mines nearby since they're could be more than 1
                    nearby_mines = self.find_specified_neighbours(
                        mine_neighbour, "mine")
                    self.board[y][x].set_mines_nearby(len(nearby_mines))
                    all_neighbours.add(mine_neighbour)

    def find_specified_neighbours(self, location: tuple[int, int], neighbour_type: str, n: int = 3):
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
                - If `numbered` then the function finds neighbouring cells that are numbered. Useful when (x, y) is a mine
                - If `mine` then it finds neighbouring mines. Useful when (x, y) is a numbered cell
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
                if self.valid_adjacent_cell(location, (x_adj, y_adj)):
                    if neighbour_type == "mine":
                        if self.board[y_adj][x_adj].is_mine:
                            neighbours.append((x_adj, y_adj))
                    elif neighbour_type == "numbered":
                        if not self.board[y_adj][x_adj].is_mine:
                            neighbours.append((x_adj, y_adj))
        return neighbours

    def find_all_connected_empty_cells(self, location: tuple[int, int], n: int = 3):
        """
        Finds all numbered cells adjacent to the empty cell and connected and connected to empty cells
        searching in a `n by n` area surrounding each cell at a given location on the board    
        ### Args:
            - `location`: The `(x,y)` coordinations on the board of an empty cell-> found by `board[y][x]`
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
                    if self.valid_adjacent_cell(location, (x_adj, y_adj)):
                        if self.board[y_adj][x_adj].mines_nearby == 0:
                            if (x_adj, y_adj) not in connected_empty_cells:
                                connected_empty_cells.add((x_adj, y_adj))
                                # Add the new neighbour to the queue
                                cells_to_check.appendleft((x_adj, y_adj))
                        elif not self.board[y_adj][x_adj].is_mine:
                            connected_numbered_cells.add((x_adj, y_adj))
        return set.union(connected_empty_cells, connected_numbered_cells)

    def valid_adjacent_cell(self, current: tuple[int, int], adjacent: tuple[int, int]):
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
        not_beyond_right_corner = y_adj < self.height and x_adj < self.width
        not_the_same_cell = (y_adj, x_adj) != (y, x)
        return not_beyond_left_corner and not_beyond_right_corner and not_the_same_cell

    def move_mine(self, pos: tuple[int, int]):
        """
        Moves a mine from one location to another while updating neighbouring cells 

        Uses:
            - Moving a mine if a user clicks a mine on the first try

        Returns:
            - False if a move is unsuccesful and True otherwise
        """
        if pos not in self.mine_locations:
            # print("WARNING: the location {} doesn't contain a mine".format(pos)) # Just for testing
            return False

        pos_x, pos_y = pos
        # [(2, 0), (4, 0), (2, 1), (3, 1), (4, 1)]
        # Get the neighbours for the mine to move
        cells_to_update = self.find_specified_neighbours(
            (pos_x, pos_y), "numbered")
        x = randint(0, self.width-1)
        y = randint(0, self.height-1)
        new_mine_neighbours = []
        if (x, y) not in self.mine_locations:  # We can move it
            new_mine_neighbours = self.find_specified_neighbours(
                (x, y), "numbered")
            print("Mine moved from {} to {}".format(pos, (x, y)))
            self.board[y][x].set_mine(self.states)
            self.board[pos_y][pos_x].set_numbered()
        cells_to_update += new_mine_neighbours

        self.number_specific_cells(cells_to_update)

        print("Mine exists")

    def number_specific_cells(self, cells_to_update: list[tuple[int, int]]):
        """
        Finds a list of a mines for the `cells_to_update` and updates the values for cells

        Args:
            - `cells_to_update` is a list of coordinates of the cells to update on the `board`
            - `board` is a list of lists representing numbered `cells: int` and `mines: str`
        """
        for cell_coords in cells_to_update:
            x, y = cell_coords
            mines_nearby = self.find_specified_neighbours(cell_coords, "mine")
            self.board[y][x].set_mines_nearby(len(mines_nearby))

    def reveal_all_cells(self, location: tuple[int, int]):
        """
        Reveals all cells that are connected to the cell at `location` and are numbered cells

        ### Returns:
            - `False` if a cell is a flag or a number. `True` if a mine
        """
        x, y = location
        cell = self.board[y][x]
        if not cell.is_mine and not cell.flagged:
            if cell.character == 0:
                all_connected_cells = self.find_all_connected_empty_cells(
                    location)
                for neighbour in all_connected_cells:
                    x, y = neighbour
                    self.revealed_cells_count += self.board[y][x].reveal_cell(self.states)
                    self.revealed_cells_count += cell.reveal_cell(self.states)
            else:
                self.revealed_cells_count += cell.reveal_cell(self.states)
            return True
        if cell.flagged:
            self.revealed_cells_count += cell.reveal_cell(self.states)
            return True
        if cell.is_mine:
            self.revealed_cells_count += cell.reveal_cell(self.states)
            return False

    def map_screen_to_board(self, pos: tuple[int, int], top_left_corner: tuple[int, int]):
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
        board_x = (x - offset_x) / (self.cell_width + 1)
        board_y = (y - offset_y) / (self.cell_height + 1)
        return (int(board_x), int(board_y))


minesweeper = Minesweeper()
minesweeper.initialise_board("super easy")
board = minesweeper.game_board

# print(board)
# board.reveal_all_cells((1, 1))
print(board)
keep_playing = True
while (keep_playing):
    choice = input("Enter a coord as x, y: ")
    # x, y to tuple
    choice = choice.split(",")
    cords = (int(choice[0])-1, int(choice[1])-1)
    if len(choice) == 3:
        if choice[2].lower() == "f":
            board.flag_cell(cords, board.states)
            print("You FLAGGED: '{} Total Revealed: {}".format(cords, board.revealed_cells_count))
    else:
        keep_playing = board.reveal_all_cells(cords)
        print("You REVEALED: '{}' Total Revealed: {}".format(cords, board.revealed_cells_count))
    print(board)
    
    if board.revealed_cells_count == board.max_revealed_cells:
        keep_playing = False

if board.revealed_cells_count == board.max_revealed_cells:
    print("You won")
else:
    print("You lost")


# print("Moving\n")
# board.move_mine((3, 0))
# print(board)
# board.flag_cell((0, 3), board.states)
# print(board)
# board.unflag_cell((0, 3), board.states)
# board.reveal_all_cells((3, 3))

# all = minesweeper.game_board.find_all_connected_empty_cells((3,2))
# for cell_loc in all:
#     x, y = cell_loc
#     minesweeper.game_board.board[y][x].reveal_cell(minesweeper.game_board.states)

# print(board)

# states = minesweeper.game_board.states
# difficulties = minesweeper.difficulties
# print("\nDifficulties:")
# for difficulty in difficulties.items():
#     print(difficulty)

# print("\nStates:")
# for state in states.items():
#     print(state)

# print("\nCell")
# empty = Cell(states)
# print(empty)
