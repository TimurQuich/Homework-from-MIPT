from random import randint


class Base:
    def input_answer(self, low_ans, high_ans, cur_ans):
        raise NotImplementedError("Wrong implementation")


class User(Base):
    def input_answer(self, low_ans, high_ans, cur_ans):
        while True:
            ans = int(input("Input an integer number "))
            if low_ans <= ans <= high_ans:
                return ans
            print(f"A number needs to be between {low_ans} and {high_ans}")


class BinaryStrategy(Base):
    def input_answer(self, low_ans, high_ans, cur_ans):
        return (low_ans + high_ans) // 2


class RandomStrategy(Base):
    def input_answer(self, low_ans, high_ans, cur_ans):
        return randint(low_ans, high_ans)
