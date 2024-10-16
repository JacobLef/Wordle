import random
# from colorama import init
# from termcolor import colored

# Initialize colorama
# init()


def colored(text: str, color: int) -> str:
    return f"\033[{color}m{text}\033[0m"


valid_words: list = [* open("valid-wordle-words.txt", "r")]
reset_progress: list = ["_", "_", "_", "_", "_"]


# WordleGame : _ -> WordleGame
# Allows for the creation of a new WordleGame
class WordleGame:
    def __init__(self) -> None:
        self.remaining_attempts: int = 6

        # letters avaiable to use
        self.available_letters: list = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        # the word to guess of this game
        ind_of_word = random.randint(0, len(valid_words))
        self.word: str = valid_words[ind_of_word]

        # current player's progress
        self.word_progress: list = reset_progress

        self.guess: str = ""

    # make into its own function possibly outisde of the class
    def guess_handler(self) -> str:
        while True:
            self.guess = input("Guess: ")
            if len(self.guess) > 5 and self.guess in valid_words:
                self.guess = input("Guess: ")
            else:
                break
        return self.guess

    def makeGuess(self, guess: str) -> None:
        for i, letter in enumerate(guess):
            if letter in self.word:
                if i == self.word.index(letter):
                    updated_letter = colored(letter, 32)
                else:
                    updated_letter = colored(letter, 33)
                if letter in self.available_letters:
                    avail_letters_index = self.available_letters.index(letter)
                    self.available_letters[avail_letters_index] = updated_letter
            else:
                if letter in self.available_letters:
                    self.available_letters.remove(letter)
                updated_letter = "_"

            self.word_progress[i] = updated_letter
        self.remaining_attempts -= 1

    def __str__(self):
        progress_msg = " ".join(self.word_progress)
        available_msg = " ".join(self.available_letters)
        print(
            "--------------------------------------"
            + f"\nAttempts Remaining: {self.remaining_attempts}"
            + f"\nWord Progress: {progress_msg}"
            + f"\nLetters Available: {available_msg}"
        )


def main():
    play_game = input("Would you like to play Wordle? ").lower()
    while play_game != "no":
        game = WordleGame()
        while game.remaining_attempts > 0:
            guess = game.guess_handler()
            if guess == game.word:
                break
            game.makeGuess(guess)
            game.__str__()
        if game.word_progress == game.word:
            print("Yay you got the word!!")
        else:
            print(f"The word was {game.word}. Better luck next time!")
        play_game = input("Would you like to play again? ").lower()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
