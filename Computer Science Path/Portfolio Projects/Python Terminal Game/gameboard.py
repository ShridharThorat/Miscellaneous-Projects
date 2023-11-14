import os
import sys
import csv


class State:
    name = None
    character = None
    background_colour = None
    foreground_colour = None

    def __init__(self, state_name, state_values):
        '''
        Constructs a State with a give name, character, background colour and foreground (text) colour
        params:
            - state_name is the name of the state
            - state_values is a list of information about the state

        '''
        self.set_state(state_name, state_values)

    def set_state(self, state_name, state_values):
        self.name = state_name
        self.character = state_values[0]
        self.background_colour = state_values[1]
        self.foreground_colour = state_values[2]

    @staticmethod
    def _read_game_states(filename):
        try:
            definitions = open(filename)
            data = csv.DictReader(definitions)
            states = State._get_states_and_values(data)
            return states
        except Exception as e:
            print("ERROR: File doesn't exist. Check if you are in the working directory")

    @staticmethod
    def _get_states_and_values(dictReader):
        '''
        Returns a dictionary with keys being the different states and values being the state's attributes
        params:
            - dictReader: A dictReader object with each item being a dictionary describing the state. 
                         
                          For example, a dictionary would be:
                          `{"state": "empty", "character": "none"}`
        '''
        formatted_dictionary = {}
        for dictionary in dictReader:
            state_name = dictionary['state']
            formatted_dictionary[state_name] = []
            for key, value in dictionary.items():
                if key.lower() != "state":
                    if value.lower() != "none":
                        formatted_dictionary[state_name].append(value)
                    else:
                        formatted_dictionary[state_name].append(None)
        return formatted_dictionary

    @staticmethod
    def _get_formatted_list(string, delimiter):
        list = string.split(delimiter)
        for item in list:
            item = item.strip()
        return list

    def __repr__(self):
        return f"State({self.name}, {self.character}, {self.background_colour}, {self.foreground_colour})"


class Cell:
    is_flagged = False
    is_questioned = False

    def __init__(self, x, y, state_name, state_values):
        self.x = x
        self.y = y
        self.state = State(state_name, state_values)

    def __repr__(self):
        return f"Cell:\n   x: {self.x}\n   y: {self.y}\n   state: {self.state}\n"


states = State._read_game_states("definitions.csv")
for key, value in states.items():
    print("{}: {}".format(key, value))

empty = Cell(0, 0, "empty", states["empty"])
print(empty)
