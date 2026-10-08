from game import Game
from players import (User, BinaryStrategy, RandomStrategy)


def choose_player():
    print("Выбери режим:")
    print("1 - Дихотомия")
    print("2 - Случайный выбор")
    print("3 - Пользователь")

    choice = input("Выбери: ")
    players = {"1": BinaryStrategy, "2": RandomStrategy, "3": User}
    return players.get(choice, BinaryStrategy)()


if __name__ == "__main__":
    player = choose_player()
    game = Game(1, 20, player)
    game.play()