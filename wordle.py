import random
from colorama import init
from termcolor import colored

# Initialize colorama
init()


valid_words = [* open("valid-wordle-words.txt", "r")]


# WordleGame : _ -> WordleGame
# Allows for the creation of a new WordleGame
class WordleGame:
    def __init__(self) -> None:
        self.remaining_attempts = 6

        # letters avaiable to use
        self.available_letters = ["a", "b", "c", "d", "c", "e",
                                  "f", "g", "h", "i", "j", "k",
                                  "l", "m", "n", "o", "p", "q",
                                  "r", "s", "t", "u", "v", "w",
                                  "x", "y", "z"]

        # the word to guess of this game
        ind_of_word = random.randint(0, len(valid_words))
        self.word = valid_words[ind_of_word]

        # current player's progress
        self.word_progress = []
        for _ in range(len(self.word) - 1):
            self.word_progress.append("_")

    def makeGuess(self, guess: str) -> None:
        for i, letter in enumerate(guess):
            if letter in self.available_letters:
                self.available_letters.remove(letter)

            if letter in self.word:
                if i == self.word.index(letter):
                    updated_letter = colored(letter, "green")
                else:
                    updated_letter = colored(letter, "yellow")
                self.word_progress[i] = updated_letter
        self.remaining_attempts -= 1

    def __str__(self):
         print(f"Attempts Remaining: {self.remaining_attempts}. Word Progress: {self.word_progress}. Letters Available: {self.available_letters}")


def main():
    play_game = input("Would you like to play Wordle? ").lower()
    while play_game != "no":
        game = WordleGame()
        while game.remaining_attempts > 0:
            while True:
                guess = input("Guess: ")
                if len(guess) != 5:
                    guess = input("Guess: ")
                else:
                    break
            game.makeGuess(guess)
            game.__str__()
        if game.word_progress == game.word:
            print("Yay you got the word!!")
        else:
            print(f"The word was {game.word}. Better lukc next time!")
        play_game = input("Would you like to play again? ").lower()


if __name__ == "__main__":
    main()
