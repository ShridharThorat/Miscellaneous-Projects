letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# Build Point dictionary
letter_to_points = {
    key: value for key, value
    in zip(letters, points)
}
letter_to_points[" "] = 0

print(letter_to_points)


def score_word(word):
    '''
    returns:
        The integer score of a word
    params:
        word -- a string
    '''
    point_total = 0
    if word is None or "":
        return point_total

    for letter in word:        
        point_total += letter_to_points.get(letter.upper(), 0)

    return point_total


# brownie_points = score_word("brownie")
# print(brownie_points)

# Score a game

player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}


# Extended

player_to_points = {}

def play_word(player, word):
    '''
    Adds a word to the list of words a player has used
    params:
        - player: A string representing the players name
        - word: A string
    '''
    if isinstance(word, str):
        if player in player_to_words.keys():
            player_to_words[player].append(word.title())

play_word("player1", "doghouse")
print(player_to_words)

def update_points_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
