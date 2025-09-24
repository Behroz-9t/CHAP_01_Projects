class change_calculator:

    def __init__(self,charged:float=None,togive:float=None):
        
        self.charged= charged
        self.togive= togive
            
        if self.charged !=None and self.togive !=None:
          
            self.charged= charged
            self.togive= togive

        else:
            self.charged=float(input("Enter the monetary amount charged: "))
            self.togive=float(input("Enter the amount you have given: "))

    def calc(self):

        self.diff = self.togive - self.charged
        
        a=self.diff

        if (self.togive<self.charged):
            b=self.charged-self.togive
            print(f"The amount you have given is lesser than the charged amount. You have to give {b} more rupees to purchase!")

        if (self.togive==self.charged):
            print("You have given exact amount. Nothing has to be returned!")

        if (a//5000)>0:
            to_return=divmod(a,5000)
            print(f"\nNumber of notes of 5000: {float(to_return[0])}\n") 
            a=to_return[1]     

        if (a//1000)>0:
            to_return=divmod(a,1000)
            print(f"Number of notes of 1000: {float(to_return[0])}\n")
            a=to_return[1]         

        if (a//500)>0:
            to_return=divmod(a,500)
            print(f"Number of notes of 500: {float(to_return[0])}\n")
            a=to_return[1] 

        if (a//100)>0:
            to_return=divmod(a,100)
            print(f"Number of notes of 100: {float(to_return[0])}\n")
            a=to_return[1] 

        if (a//50)>0:
            to_return=divmod(a,50)
            print(f"Number of notes of 50: {float(to_return[0])}\n")
            a=to_return[1] 

        if (a//10)>0:
            to_return=divmod(a,10)
            print(f"Number of notes of 10: {float(to_return[0])}\n")
            a=to_return[1] 

        if (a//5)>0:
            to_return=divmod(a,5)
            print(f"Number of coins of 5: {float(to_return[0])}\n")
            a=to_return[1] 

        if (a//2)>0:
            to_return=divmod(a,2)
            print(f"Number of coins of 2: {float(to_return[0])}\n")
            a=to_return[1] 

        if (a//1)>0:
            to_return=divmod(a,1)
            print(f"Number of coins of 1: {float(to_return[0])}\n")
            a=to_return[1] 
        

    def __str__(self):
        return f"{self.calc()}"
            


