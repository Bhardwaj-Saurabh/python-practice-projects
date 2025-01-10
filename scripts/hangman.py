import random


hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


hangman_title = """
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\\_| |_/\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

print(hangman_title)


vocab = word_list = [
    "python",
    "hangman",
    "challenge",
    "development",
    "algorithm",
    "computer",
    "programming",
    "software",
    "variable",
    "function",
    "keyboard",
    "internet",
    "database",
    "framework",
    "developer",
    "debugging",
    "hardware",
    "technology",
    "iteration",
    "recursion"
]


class Hangman:
    def __init__(self, life: int, vocab: list):
        self.life = life
        self.vocab = vocab
        self.word = random.choice(vocab)
        self.user_word = ['_' for _ in self.word]
        self.tries = 0
        self.win = False

    def check_for_win(self):
        if ''.join(self.user_word) == self.word:
            self.win = True
            print("That is CORRECT. Congraulations! You Won...")
    
    def get_user_input(self):

        while True:
            user_guess = input("Please guess a word: ")
            if len(user_guess) < 1:
                print(f"You have not entered anything. Please Guess a word.")
            elif user_guess in self.user_word:
                print(f"You have already entered {user_guess}. Please Guess another word.")
            else:
                break
        return user_guess

    def update_user_word(self, user_guess: str):
        if user_guess in self.word:
            for i, word in enumerate(self.word):
                if user_guess == word:
                    self.user_word[i] = word
            print(f"You have got it right --> {''.join(self.user_word)}")
        else:
            self.tries += 1
            print(hangman_stages[self.tries])
            print(f"Opps! {user_guess} is wrong. You have {self.life - self.tries} life left. Please Try again!.")
    
    def play(self):
        while not self.win:
            user_guess = self.get_user_input()
            self.update_user_word(user_guess)
            self.check_for_win()
            
            if self.tries >= 5:
                print("Oh Nooooo! You have lost the game...")
                break



if __name__ == "__main__":
    hangman = Hangman(5, vocab)
    hangman.play()

