import os
import sys
import csv


class Cell:
    name = None
    character = None
    background_colour = None
    foreground_colour = None

    def __init__(self, cell_name, cell_values):
        '''
        Constructs a Cell with a give name, character, background colour and foreground (text) colour
        params:
            - cell_name is the name of the cell
            - cell_values is a list of information about the cell
        '''
        self.set_cell(cell_name, cell_values)

    def set_cell(self, cell_name, cell_values):
        self.name = cell_name
        self.character = cell_values[0]
        self.background_colour = cell_values[1]
        self.foreground_colour = cell_values[2]

    @staticmethod
    def _get_formatted_list(string, delimiter):
        list = string.split(delimiter)
        for item in list:
            item = item.strip()
        return list

    def __repr__(self):
        return f"Cell({self.name}, {self.character}, {self.background_colour}, {self.foreground_colour})"


class Game:
    _difficulties = {
        "easy": [(9, 9)],
        "hard": [(15, 15)],
        "expert": [(30, 15)]
    }

    cell_length = 5
    cell_width = 3
    corner = "+"
    ceil_floor = "-"
    wall = "|"

    def __init__(self, filename="definitions.csv"):
        '''
        Initialises a minesweeper game by reading a csv file.
        '''
        self._difficulty = None
        self.states = Game._read_file(filename)
        self._read_states()

    def set_difficulty(self, difficulty):
        if difficulty in self._difficulties.keys():
            self._difficulty = difficulty
        else:
            print("ERROR: {} is not a valid difficulty".format(difficulty))

    def _draw_cell(self, x, y, cell_name):
        cell = Cell(cell_name, self.states[cell_name])
        print(cell)
        center = self._cell_center(cell)
        print(center)
        return center

    def _cell_center(self, cell):
        center = ""
        cell_center = (self.cell_length-1)/2
        for i in range(self.cell_length):
            if i == 0 or i == (self.cell_length-1):
                center += self.wall
            elif i == cell_center:
                center += cell.character
            else:
                center += " "
        return center

    def draw_barrier(self):
        barrier = ""
        game_height_length = self._difficulties[self._difficulty][0]
        cells_vertical, cells_across = game_height_length
        num_cells_across = cells_across * self.cell_length
        for i in range(num_cells_across):
            if i % (self.cell_length-1) == 0:
                barrier += self.corner
            else:
                barrier += self.ceil_floor
        return barrier

    def _read_states(self):
        print("All cell states:")
        for key, value in self.states.items():
            print("{}: {}".format(key, value))
        print()

    @staticmethod
    def _read_file(filename):
        try:
            definitions = open(filename)
            data = csv.DictReader(definitions)
            cells = Game._unpack_dictReader(data)
            return cells
        except Exception as e:
            print("ERROR: File doesn't exist. Check if you are in the working directory")

    @staticmethod
    def _unpack_dictReader(dictReader):
        '''
        Returns a dictionary with keys being the different cells and values being the cell's attributes
        params:
            - dictReader: A dictReader object with each item being a dictionary describing the cell. 

                          For example, a dictionary would be:
                          `{"cell": "empty", "character": "none"}`
        '''
        formatted_dictionary = {}
        for dictionary in dictReader:
            cell_name = dictionary["state"]
            formatted_dictionary[cell_name] = []
            for key, value in dictionary.items():
                if key.lower() != "state":
                    if value.lower() != "none":
                        formatted_dictionary[cell_name].append(value)
                    else:
                        formatted_dictionary[cell_name].append(" ")
        return formatted_dictionary



# game = Game()
# print(game._draw_cell(0, 0, "empty"))

# game.set_difficulty("easy")
# print(game._difficulty)
# print(game._difficulties)

# print(game.draw_barrier())
