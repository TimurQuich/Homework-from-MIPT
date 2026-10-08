from random import randint


class Base:
    def input_answer(self, low_ans, high_ans, cur_ans):
        pass

class User(Base):
    def input_answer(self, low_ans, high_ans, cur_ans):
        while True:
            ans = int(input("Введите число "))
            if low_ans <= ans <= high_ans:
                return ans
            print(f"Число лежит между {low_ans} и {high_ans}")


class BinaryStrategy(Base):
    def input_answer(self, low_ans, high_ans, cur_ans):
        return (low_ans + high_ans) // 2


class RandomStrategy(Base):
    def input_answer(self, low_ans, high_ans, cur_ans):
        return randint(low_ans, high_ans)
