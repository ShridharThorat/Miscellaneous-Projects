from gameboard import Cell, Game
import curses
from curses import wrapper
import time

class Minesweeper:
    screen_height = None
    screen_width = None
    center_width = None
    center_height = None
    game_definitions = "definitions.csv"

    start_directions = {
        0: "Welcome to Terminal Minesweeper",
        1: "Easy Mode",
        2: "Hard Mode",
        3: "Expert Mode",
        4: "Exit"
    }

    def __init__(self):
        self.game = Game(self.game_definitions)

    def print_instructions(self, screen):
        first_instruction_len = 0        
        for number, instruction in self.start_directions.items():
            screen_instr = "{}: {}".format(number, instruction)
            if number == 0:
                screen_instr = "{}".format(instruction)
                first_instruction_len = len(screen_instr)
            if number == 1:
                screen_instr = "{}: {}".format(number, instruction)
                first_instruction_len = len(screen_instr)

            centered_x_coord = int(self.center_width - first_instruction_len/2)
            screen.addstr(self.center_height+number,
                          centered_x_coord,
                          screen_instr,
                          curses.color_pair(1))
            
        screen = curses.initscr()
        screen.move(self.center_height+1, centered_x_coord)
        # Minesweeper.cursor_move(screen,1,1)
    
    
    @staticmethod
    def cursor_move(screen, distance_height=1, distance_width=1):
        # How far the cursor movies
        distance_height, distance_width = distance_height, distance_width
        

    def start_screen(self):
        screen = curses.initscr()
        curses.noecho()
        # screen.keypad(1)
        screen.clear()
        
        # Initialise colours
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE) # Blue background, white text
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)

        # Initialise screen heights
        self.screen_height, self.screen_width = screen.getmaxyx()
        self.center_width = self.screen_width // 2
        self.center_height = self.screen_height // 2
                        
        self.print_instructions(screen)
        self.start_screen_move(screen, self.start_directions)

        screen.getch()
        curses.endwin()
        
    def start_screen_move(self, screen, instructions):
        distance_height, distance_width = 1, 0
        
        max_height = self.center_height + len(instructions) - 1 # -1 to discount the welcome message
        min_height = self.center_height + 1
        centered_x_coord = int(self.center_width - len(instructions[1]) /2)
        x_pos, y_pos = centered_x_coord-1, min_height
        
        key = -1
        while key != ord('q'):
            screen.move(y_pos,x_pos)
            screen.refresh()
            key = screen.getch()
            if key == ord("s") and y_pos < max_height:
                y_pos += distance_height
            elif key == ord("w") and y_pos > min_height:
                y_pos -= distance_height
            
                
            time.sleep(0.1)
                



minesweeper = Minesweeper()
minesweeper.start_screen()
