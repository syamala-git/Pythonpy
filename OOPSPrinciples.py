
class Calc:
    num = 10  # class variables

    # default constructor
    def __init__(self, a, b):  # parameters should match with the objects created
        self.firstnum = a  # self is the objects : a and b are instance variables
        self.secondnum = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am getData method in Calc class")

    def Addition(self):
        return self.firstnum + self.secondnum + Calc.num

obj = Calc(2, 3)  # syntax to create objects
obj.getData()
print(obj.Addition())
