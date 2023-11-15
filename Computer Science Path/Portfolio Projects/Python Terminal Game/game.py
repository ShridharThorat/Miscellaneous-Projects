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

    start_instructions = {
        0: ["Welcome to Terminal Minesweeper"],
        1: ["Easy Mode"],
        2: ["Hard Mode"],
        3: ["Expert Mode"],
        4: ["Exit"]
    }

    def __init__(self):
        self.game = Game(self.game_definitions)

    def print_instructions(self, screen):
        first_instruction_len = 0
        for number, instruction in self.start_instructions.items():
            screen_instr = "{}: {}".format(number, instruction[0])
            if number == 0:
                screen_instr = "{}".format(instruction[0])
                first_instruction_len = len(screen_instr)
            if number == 1:
                screen_instr = "{}: {}".format(number, instruction[0])
                first_instruction_len = len(screen_instr)

            centered_x_coord = int(self.center_width - first_instruction_len/2)
            instruction_coords = (centered_x_coord, self.center_height+number)
            # Add the position on the screen to dictionary
            instruction.append(instruction_coords)
            screen.addstr(instruction[1][1],
                          instruction[1][0],
                          screen_instr,
                          curses.color_pair(1))

        screen = curses.initscr()
        screen.move(self.center_height+1, centered_x_coord)


    def start_screen(self):
        screen = curses.initscr()
        curses.noecho()
        screen.clear()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)

        # Initialise screen heights
        self.screen_height, self.screen_width = screen.getmaxyx()
        self.center_width = self.screen_width // 2
        self.center_height = self.screen_height // 2

        self.print_instructions(screen)
        self.start_screen_move(screen, self.start_instructions)

        screen.getch()
        curses.endwin()

    def highlight_selection(self, screen, y_pos_of_key, instructions):
        for number, instruction in instructions.items():
            if number == 0:
                str = "{}".format(instruction[0])
            else:
                str = "{}: {}".format(number, instruction[0])

            # Colour where the cursor is and reset colour where it isn't
            if y_pos_of_key == instruction[1][1]:
                screen.addstr(
                    instruction[1][1], instruction[1][0], str, curses.color_pair(2))
            else:
                screen.addstr(
                    instruction[1][1], instruction[1][0], str, curses.color_pair(1))

    def start_screen_move(self, screen, instructions):
        distance_height, distance_width = 1, 0
        screen.refresh()
        # -1 to discount the welcome message
        max_height = self.center_height + len(instructions) - 1
        min_height = self.center_height + 1
        # centered_x_coord = int(self.center_width - len(instructions[1][0]) /2)
        x_pos, y_pos = instructions[1][1]
        screen.move(y_pos, x_pos)
        key = -1
        while True:
            screen.refresh()
            self.highlight_selection(screen, y_pos, self.start_instructions)

            key = screen.getch()
            if key == ord("s") and y_pos < max_height:
                y_pos += distance_height
            elif key == ord("w") and y_pos > min_height:
                y_pos -= distance_height

            # if enter is pressed
            elif key in [curses.KEY_ENTER, 10, 13]:
                if y_pos == min_height:
                    self.game.set_difficulty("easy")
                    self.game_screen(screen)
                elif y_pos == min_height+1:
                    self.game.set_difficulty("hard")
                elif y_pos == min_height+2:
                    self.game.set_difficulty("hard")
                elif y_pos == min_height+3:
                    screen.clear()
                    curses.endwin()
                    exit()
                else:
                    pass
            screen.move(y_pos, x_pos+1)

            time.sleep(0.1)
            
    def game_screen(self, screen):
        distance_height, distance_width = 1, 0
        x_start, y_start = 20, 5
        screen.clear()
        screen.refresh()
        screen.move(0, 0)
        q = screen.getch()
        while q != ord("q"):
            screen.refresh()
            barrier = self.game.draw_barrier()
            for i in range(self.game._difficulties[self.game._difficulty][0][1]):
                screen.addstr(y_start+i, x_start, barrier, curses.COLOR_WHITE | curses.A_BOLD)
            q = screen.getch()
        screen.clear()
        screen.refresh()


minesweeper = Minesweeper()
minesweeper.start_screen()
