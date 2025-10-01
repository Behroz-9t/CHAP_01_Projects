from P_OOP_Q33 import HandHeldCalc

class Application:
    def __init__(self,confirmation="y"):
        self.confirmation=confirmation

    def app(self):

        while self.confirmation!="n":
            h=HandHeldCalc()
            print(h)
            self.confirmation=input("\nDo you want to include more number?:y/n \n\n")


a=Application()
a.app()
