from game import Game
from players import (User, BinaryStrategy, RandomStrategy)


def choose_player():
    print("Choose the option:")
    print("1 — Binary Strategy")
    print("2 — Random Choice")
    print("3 — User")

    choice = input("Ваш выбор: ")
    players = {
        "1": BinaryStrategy,
        "2": RandomStrategy,
        "3": User
    }
    return players.get(choice, BinaryStrategy)()


if __name__ == "__main__":
    player = choose_player()
    game = Game(1, 20, player)
    game.play()