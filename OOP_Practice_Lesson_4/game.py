from random import randint


class Game:
    def __init__(self, low_ans=0, high_ans=20, player=None):
        self.low = low_ans
        self.high = high_ans
        self.player = player
        self.secret = randint(low_ans, high_ans)
        self.attempts = 0


    def play(self):
        print(f"Число между {self.low} и {self.high}.")
        current_low, current_high = self.low, self.high
        last_result = None

        while True:
            guess = self.player.input_answer(current_low, current_high, last_result)
            self.attempts += 1
            print(f"Номер попытки {self.attempts}: {guess}")

            if guess == self.secret:
                print(f"ПРавильно! Ответ: {self.secret}. Число попыток: {self.attempts}")
                return self.attempts

            if guess < self.secret:
                last_result = "higher"
                current_low = max(current_low, guess + 1)
                print("Больше")
            else:
                last_result = "lower"
                current_high = min(current_high, guess - 1)
                print("Меньше")