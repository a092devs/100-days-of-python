from random import randint

class MathProblem:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.answer = 0
        self.new_problem()

    def __new_number(self):
        return randint(1, 999)

    def new_problem(self):
        self.num1 = self.__new_number()
        self.num2 = self.__new_number()
        self.answer = self.num1 + self.num2