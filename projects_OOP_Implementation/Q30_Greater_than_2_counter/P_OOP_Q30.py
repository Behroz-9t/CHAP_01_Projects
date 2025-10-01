class Counter:
     
    def __init__(self,n=None):
        if n==None:
            self.n=int(input("Enter any number greater than 2: "))

        self.divide=2
        self.count=0

    def CountTimes(self):


        
        while self.divide>=2:    
            self.divide=self.n/2    
            self.n=self.divide
            self.count+=1
        

    def __str__(self):
        self.CountTimes()
        return f"\nIf you divide the given number by 2 '{self.count}' number of times then it will get less than 2.\n"

        

