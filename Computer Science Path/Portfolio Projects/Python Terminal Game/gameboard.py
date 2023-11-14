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
        self.character = State._set_character(state_values[0])
        self.background_colour = state_values[1]
        self.foreground_colour = state_values[2]

    @staticmethod
    def _load_game_states(filename):
        try:
            definitions = open(filename)
            names = definitions.readline().strip("\n")  # The first line has metadata
            names_list = State._get_formatted_list(names, ",")
            data = csv.DictReader(definitions, delimiter=",")
            bgs = []
            for bg in data:
                bg.append(bg['background_colour'])
            print(bgs)
            return data
        except Exception as e:
            print("ERROR: File doesn't exist. Check if you are in the working directory")

    @staticmethod
    def _get_formatted_list(string, delimiter):
        list = string.split(delimiter)
        for item in list:
            item = item.strip()
        return list

    @staticmethod
    def _set_character(string_character):
        if string_character[0].lower() == "none":
            return None
        else:
            return string_character


class Cell:
    is_flagged = False
    is_questioned = False

    def __init__(self, x, y, state_name, state_values):
        self.x = x
        self.y = y
        # should be defaulted to "empty" when used
        self.state = State(state_name, state_values)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"


file = State._load_game_states("definitions.csv")
print(file)
