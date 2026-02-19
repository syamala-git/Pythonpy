from OOPSPrinciples import Calc

class ChildImp(Calc):
    num2 = 100

    def __init__(self):
        Calc.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Addition()


obj2 = ChildImp()
print(obj2.getCompleteData())
