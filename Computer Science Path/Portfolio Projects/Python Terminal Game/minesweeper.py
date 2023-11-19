import csv
from random import randint, seed, sample
from typing import Union
from collections import deque


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
        self.game_board = Board("easy", self.difficulties, definitions_file)

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

    def __init__(self, name: str = None, states: dict[str, Union[str, int]] = None):
        self.name = name
        if states is not None:
            self.character = states["hidden"]["character"]
        else:
            self.character = 0
        self.revealed = False
        self.flagged = False
        self.mines_nearby = 0

    def set_mines_nearby(self, mines_nearby: int):
        self.mines_nearby = mines_nearby
        if self.name not in ["mine", "flagged"]:
            self.name = "numbered"

    def set_name(self, name: str, states: dict[str, dict[str, int]]):
        self.name = name
        self.character = states[name]["character"]

    def flag_cell(self, states: dict[str, dict[str, int]]):
        if not self.flagged:
            self.flagged = True
            self.character = states["flag"]["character"]

    def reveal_cell(self, states: dict[str, dict[str, int]]):
        if not self.revealed:
            self.revealed = True
            if self.name in ["flag", "mine"]:
                self.character = states[self.name]["character"]
            else:
                self.character = self.mines_nearby

    def __repr__(self):
        return f"{self.character}"


class Board:

    def __init__(self, difficulty: str, difficulties: dict[str, tuple[int, int]], cell_definitions_file: str = "definitions.csv",):
        self.cell_definitions_file = cell_definitions_file
        self.states = Minesweeper._read_file(self.cell_definitions_file)
        self.difficulty = difficulty
        self.width, self.height = difficulties[difficulty]['board_size']
        self.num_mines = difficulties[difficulty]['mines']
        self.flags = 0
        self.board = self.create_board()

    def __str__(self):
        board_info = "Board: difficulty: {}, size: ({},{}), mines: {}".format(
            self.difficulty, self.width, self.height, self.num_mines)
        board_str = board_info + "\n"
        for row in self.board:
            board_str += "| "
            for cell in row:
                if cell.revealed:
                    board_str += f"{cell.character}" + " "
                else:
                    board_str += f"{self.states['hidden']['character']}" + " "
            board_str += "|\n"

        return board_str

    def create_board(self):
        board = [[Cell() for j in range(self.width)]
                 for i in range(self.height)]

        num_placed_mines = 0
        mine_locations = []

        # Place mines on the board
        while num_placed_mines < self.num_mines:
            x = randint(0, self.width-1)
            y = randint(0, self.height-1)
            if (x, y) not in mine_locations:
                board[y][x].set_name("mine", self.states)
                mine_locations.append((x, y))
            num_placed_mines += 1
        return board


minesweeper = Minesweeper()
board = minesweeper.game_board
print(board)
states = minesweeper.game_board.states
difficulties = minesweeper.difficulties
print("\nDifficulties:")
for difficulty in difficulties.items():
    print(difficulty)

print("\nStates:")
for state in states.items():
    print(state)

print("\nCell")
empty = Cell("empty", states)
print(empty.name)
print(f"`{empty.character}`")
