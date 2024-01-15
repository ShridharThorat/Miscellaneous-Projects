# --- Day 1: Trebuchet?! ---

# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

import typing


def trebuchet(s: str):
    """Returns a calibration value from a puzzle input. 
    It consists of the first digit and last digit to form
    a 2 digit number. If there is only 1 number then it is repeated.

    Args:
        s (str): _description_
    """
    calibration_value = ""
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    front = 0
    end = len(s) - 1

    if front == end:
        if s[front] in numbers:
            calibration_value += s[front] + s[front]
            return int(calibration_value)
        return None

    first_found = False
    last_found = False
    while (front <= end) and (first_found is False and last_found is False):
        if not first_found:
            if s[front] in numbers.values():
                calibration_value += s[front]
                first_found = True
            else:
                for num_word in numbers.keys():
                    end_word = len(num_word)
                    if end_word < len(s):
                        if s[front:end_word] == num_word:
                            calibration_value += numbers[num_word]
                            first_found = True
                            first_found += end_word - 1
                            break
        if not last_found:
            if s[end] in numbers.values():
                calibration_value += s[end]
                last_found = True
            else:
                for num_word in numbers.keys():
                    start_word = end-len(num_word)+1
                    if end < len(s):
                        if s[start_word:end+1] == num_word:
                            calibration_value += numbers[num_word]
                            first_found = True
                            end -= len(num_word) + 1
                            break

            front += 1
            end -= 1

    if len(calibration_value) == 1:
        calibration_value += calibration_value
    if first_found is False and last_found is False:
        return 0
    else:
        return int(calibration_value)


file_name = "Advent of Code 2023/input_1.txt"


def sum_trebuchet(file_name: str):
    file = open(file_name, 'r')
    sum = 0
    for line in file:
        sum += trebuchet(line.strip())
        print(f"{line.strip()}: {trebuchet(line.strip())}")

    return sum


print(sum_trebuchet(file_name))
