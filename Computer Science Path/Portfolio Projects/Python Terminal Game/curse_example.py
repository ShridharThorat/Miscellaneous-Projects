import curses
from curses import wrapper
import time
import emoji


def black_bg(stdscr):
    # Your application logic here
    stdscr.clear()
    stdscr.addstr(10, 10, "Hello world", curses.A_UNDERLINE)
    stdscr.addstr(15, 25, "Awesome")
    stdscr.refresh()
    stdscr.getch()


def screen(stdscr):
    screen = curses.initscr()
    screen.clear()

    height, width = screen.getmaxyx()
    middle_h = height/2
    middle_w = width/2

    text = "Hello world"
    text_len = len(text)
    actual_middle_w = int(middle_w - text_len/2)
    # screen.addstr(int(middle_h), int(actual_middle_w), text)

    # # Horizontally moving text
    # for i in range(width-text_len):
    #     screen.clear()
    #     screen.addstr(int(text_len/2), i,  text)
    #     screen.refresh()
    #     time.sleep(0.1)

    # more animation - bouncing text
    # vertical, horizontal = 1,1
    # q = -1
    # x,y = 0,0
    # while q < 0:
    #     screen.clear()
    #     screen.addstr(y, x,  text)
    #     screen.refresh()
    #     x += horizontal
    #     y += vertical

    #     if y >= height - 1:
    #         vertical = -1
    #     elif y == 0 :
    #         vertical = 1

    #     if x >= width - text_len - 1:
    #         horizontal = -1
    #     elif x == 0:
    #         horizontal = 1

    #     time.sleep(0.1)

    # user input

    # screen.refresh()
    screen.getch()
    curses.endwin()


def screensaver(stdscr):
    screen = curses.initscr()
    screen.clear()
    curses.start_color()
    # foregroud, background
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # foregroud, background
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    # foregroud, background
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    screen.nodelay(1)
    height, width = screen.getmaxyx()
    middle_h = height/2
    middle_w = width/2

    text = "Hello world"
    text_len = len(text)
    actual_middle_w = int(middle_w - text_len/2)

    # 1,2,3, are read as ord("1") = 49, ord("2") = 50
    vertical, horizontal = 1, 1
    q = -1
    x, y = 0, 0
    g = 0  # colour tracker. g=0 is the default
    while q < 0 or q in range(48, 52):
        q = screen.getch()
        if q in range(48, 52):
            # chr is the ord function in reverse -> the actual key
            g = int(chr(q))
        screen.clear()
        # Combine attributes with |
        screen.addstr(y, x,  text, curses.color_pair(g) | curses.A_REVERSE)
        screen.refresh()
        x += horizontal
        y += vertical
        if y >= height - 1:
            vertical = -1
        elif y == 0:
            vertical = 1

        if x >= width - text_len - 1:
            horizontal = -1
        elif x == 0:
            horizontal = 1

        time.sleep(0.1)


def inputExample(stdscr):
    screen = curses.initscr()
    screen.clear()
    curses.noecho()  # Removes refresh frames after input
    screen.keypad(1)  # allows key usage
    height, width = screen.getmaxyx()
    middle_h = int(height/2)
    middle_w = int(width/2)

    text = "Hello world"
    text_len = len(text)
    actual_middle_w = int(middle_w - text_len/2)

    vertical, horizontal = 1, 1
    q = -1
    x, y = 0, 0
    while q != ord('q'):  # if some char q is pressed, exit
        screen.clear()
        screen.addstr(y, x, text)
        screen.move(height-1, width-1)  # Starting positiond
        screen.refresh()
        q = screen.getch()
        if q == ord("w") and y > 0:
            y -= 1
        elif q == ord("s") and y < height-1:
            y += 1
        elif q == ord("a") and x > 0:
            x -= 1
        elif q == ord("d") and x < width - text_len:
            x += 1
        if q == ord("1"):
            exit()
        if y == height-1 and x == width - text_len:
            if q == ord("s"):
                y -= 1
            elif q == ord("d"):
                x -= 1

        time.sleep(0.1)


def inputExample2(stdscr):
    screen = curses.initscr()
    screen.clear()
    curses.noecho()  # Removes refresh frames after input
    height, width = screen.getmaxyx()
    middle_h = int(height/2)
    middle_w = int(width/2)

    text = "Hello world"
    text_len = len(text)
    actual_middle_w = int(middle_w - text_len/2)

    vertical, horizontal = 1, 1
    q = -1
    x, y = 0, 0
    screen.addstr(middle_h, actual_middle_w, text)
    while q != ord('q'):  # if some char q is pressed, exit
        # screen.clear()
        
        screen.addstr(y, x, "")
        screen.refresh()
        q = screen.getch()
        if q == ord("w") and y > 0:
            y -= 1
        elif q == ord("s") and y < height-1:
            y += 1
        elif q == ord("a") and x > 0:
            x -= 1
        elif q == ord("d") and x < width - text_len - 1:
            x += 1
        if q == ord("1"):
            exit()

        time.sleep(0.1)

import curses

def main(stdscr):
    # Set up the terminal
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)  # Define a color pair (pair number, foreground color, background color)

    # Draw a rectangle with a specific color
    height, width = stdscr.getmaxyx()
    y, x = height // 2, width // 4
    text = "Colored Area"
    color_pair = 1  # Use the color pair defined above

    stdscr.addstr(y, x, text, curses.color_pair(color_pair) | curses.A_REVERSE)

    stdscr.refresh()
    stdscr.getch()

# Run the curses application
# curses.wrapper(black_bg)
# screen(curses.initscr())
inputExample2(curses.initscr())
# screensaver(curses.initscr())
# print(emoji.emojize('Python is :white_large_square:'))
