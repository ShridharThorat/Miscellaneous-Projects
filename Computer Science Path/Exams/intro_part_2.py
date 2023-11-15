# Q1
# All of our store items
all_items = [["Taffy", 1], ["Chocolate", 2], ["Cup", 5],
             ["Plate", 10], ["Bowl", 11], ["Silverware", 22]]

# Empty discounted_items list
discounted_items = []

# Your code here
for item in all_items:
    if item[1] % 2 == 1:  # Odd values items
        discounted_items.append(item)

# For testing purposes: print discounted list
print(discounted_items)


# Q2
def buy_items(money, dog_treat_count, price):
    num_bought = 0

    while money >= 0:
        if money >= price:
            num_bought += 1
            money -= price
        else:
            break
        if num_bought == dog_treat_count:
            break

    return num_bought


total_1 = buy_items(100, 20, 4)
print("Test 1: " + str(total_1))
total_2 = buy_items(10, 10, 4)
print("Test 2: " + str(total_2))


# Q3 Terminal command for commit a file

# Q4
class HashtagsCreator:

    def __init__(self, list_of_terms):
        self.hashtags = []

        for term in list_of_terms:
            # Fix this section of code
            if term[0] == "@":
                new_term = "#" + term[1:]
                self.hashtags.append(new_term)
            elif term[0] != "#":
                self.hashtags.append("#" + term)
            else:
                self.hashtags.append(term)

    def list_hashtags(self):
        for hashtag in self.hashtags:
            print(hashtag)


# Do not edit testing code
test_hashtags = HashtagsCreator(
    ["@codecademy", "#python", "programming", "#strings"])
test_hashtags.list_hashtags()


# Q5
# Import random class
import random
class Number_Guesser:

    def __init__(self, player_names):
        self.player_guesses = {}

        # Adds names and -1 to player_guesses
        for name in player_names:
            self.player_guesses[name] = -1

        # Update to choose a random number
        self.secret_number = random.randint(1,10)

    def add_player_guess(self, name, guess):
        # Fill in this method
        if name in self.player_guesses:
            self.player_guesses[name] = guess

    def print_answer(self):
        print(str(self.secret_number), "is the secret number!")

    def print_guesses(self):
        for player in self.player_guesses.items():
            if player[1] != -1:
                print(player[0], "guessed", str(player[1]))
            else:
                print(player[0], "needs to guess!")


game1 = Number_Guesser(["Thuy", "Joe", "Diya"])
game1.add_player_guess("Roger", 10)
game1.add_player_guess("Diya", 8)
game1.add_player_guess("Thuy", 1)
game1.add_player_guess("Joe", 5)
game1.print_guesses()
game1.print_answer()


# Q6