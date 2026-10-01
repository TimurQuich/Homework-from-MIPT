from random import randint
from players import (User, BinaryStrategy, RandomStrategy)


class Game:
    def __init__(self, low_ans=0, high_ans=20, player=None):
        self.low = low_ans
        self.high = high_ans
        self.player = player
        self.secret = randint(low_ans, high_ans)
        self.attempts = 0


    def play(self):
        print(f"The number in the from interval {self.low} to {self.high}.")
        current_low, current_high = self.low, self.high
        last_result = None

        while True:
            guess = self.player.input_answer(current_low, current_high, last_result)
            self.attempts += 1
            print(f"Attempt {self.attempts}: {guess}")

            if guess == self.secret:
                print(f"This is it! The number: {self.secret}. Attempts: {self.attempts}")
                return self.attempts

            if guess < self.secret:
                last_result = "higher"
                current_low = max(current_low, guess + 1)
                print("Larger")
            else:
                last_result = "lower"
                current_high = min(current_high, guess - 1)
                print("Smaller")