# Exercise 10
print("-----Understanding class creation-----")


class BasicCalculator:

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


calc = BasicCalculator(10, 5)
print(f"Addition: {calc.num1} + {calc.num2} = {calc.addition()}")
print(f"Subtraction: {calc.num1} - {calc.num2} = {calc.subtraction()}")
print(f"Multiplication: {calc.num1} * {calc.num2} = {calc.multiplication()}")
print(f"Division: {calc.num1} / {calc.num2} = {calc.division()}")