class HandHeldCalc:

    def __init__(self,num=None):
        if num ==None :

            
            self.num=int(input("\nEnter the digit 1: "))
            self.check=input("\nFor clear:c\nor Enter to continue\n\n")
            
            if self.check=="c":
                self.num=int(input("Value cleared!\nRe-Enter the digit 1: "))


            self.num2=int(input("Enter the digit 2: ")) 
            self.check=input("\nFor clear:c\nor Enter to continue\n\n")
            
            if self.check=="c":
                self.num2=int(input("Value cleared!\nRe-Enter the digit 2: "))
               
              
            print("For add enter:1\nFor subtract enter:2\nFor divide enter:3\nFor multiply enter:4\n")
            self.storeinput=int(input()) 
            self.check=input("\nFor Reset:r\nor Enter to continue\n\n")

            if self.check=="r":
                self.num=int(input("Enter the digit 1: "))
                self.check=input("\nFor clear:c\nor Enter to continue\n\n")
                
                if self.check=="c":
                    self.num=int(input("Value cleared!\nRe-Enter the digit 1: "))


                self.num2=int(input("Enter the digit 2: ")) 
                self.check=input("\nFor clear:c\nor Enter to continue\n\n")
                
                if self.check=="c":
                    self.num2=int(input("Value cleared!\nRe-Enter the digit 2: "))
               
                print("For add enter:1\nFor subtract enter:2\nFor divide enter:3\nFor multiply enter:4\n")
                self.storeinput=int(input()) 
                

                
                

    def add(self):
        if self.storeinput==1:
            self.addition=self.num+self.num2
            print(f"\n{self.num} + {self.num2} = {self.addition}\n")

    def sub(self):
        if self.storeinput==2:
            self.subtraction=self.num-self.num2
            print(f"\n{self.num} - {self.num2} = {self.subtraction}\n")

    def div(self):
        if self.storeinput==3:
            if self.num2>0:

                self.subtraction=self.num/self.num2
                print(f"\n{self.num} / {self.num2} = {self.subtraction}\n")
            else:
                raise ValueError("Math Error")

    def mul(self):
        if self.storeinput==4:
            self.multiplication=self.num*self.num2
            print(f"\n{self.num} x {self.num2} = {self.multiplication}\n")


    

    def __str__(self):
        self.add()
        self.sub()
        self.div()
        self.mul()
        return ""



