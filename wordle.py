import sys
import random
from rich import print


# looks for all the words in certain file
def read_all_words():

    # checks if any command line args present
    if len(sys.argv) > 1:

        # checks if number is 5-8
        if int(sys.argv[1]) in range(5, 9):

            # setting word length
            word_length = sys.argv[1]

            # opening file for reading
            with open(f"collections\{word_length}.txt", "r") as file:

                # reading whole file in list
                words = file.read().split("\n")
                return words
        else:
            raise ValueError("No such file")
    else:
        raise ValueError("No argument provided")



def select_random_word(all_words):
    word = random.choice(all_words)
    return word


# prompts the user for input
def get_guess(word):
    word_size = len(word)
    guess = input(f"Please enter {word_size}-letter word: ")
    return guess


# iterates over word and checks for correct/wrong letters
def check_guess(guess, word):
    # makes a strings for defining colors of letters
    # example: RRGYRY
    colorized_guess = "" * len(word)

    # loops through both letters and indices in word
    for position, letter in enumerate(guess):

        # exact guess 
        if word[position] == guess[position]:
            colorized_guess += "G" # G - green
        elif letter in word:
            colorized_guess += "Y" # Y - yellow
        else:
            colorized_guess += "R" # R - red

    return colorized_guess 


# prints out the word in correct colors
def print_word(colorized_guess, guess, guesses):

    colors = {
        "G": "green",
        "Y": "yellow",
        "R": "red"
    }

    print(f"Guess {guesses}: ", end="")
    for position, color in enumerate(colorized_guess):

        # using rich to print using colors
        # pattern: [color]text to print[/color]
        print(f"[{colors[color]}]{guess[position]}[/{colors[color]}]", end="")
    
    print() # ends line
    return None

# main logic
def main():
    try:
        all_words = read_all_words()
        word = select_random_word(all_words)
    except Exception as e:
        print(e)

    print("[green]This is WORDLE[/green]")
    guesses = 0 # for counting user inputs

    guess = ""

    # repeating prompting for input when word is too short or too long
    while guess != word: 
        guess = ""
        while len(guess) != len(word):
            guess = get_guess(word)

        guesses += 1 # next guess
        colorized_guess = check_guess(guess, word)
        print_word(colorized_guess, guess, guesses)

        if guesses > 5:
            print("No luck today!")
            break
    else:
        print("You guessed the word!")

if __name__ == "__main__":
    main()