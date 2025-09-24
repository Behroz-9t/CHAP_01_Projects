import random

class birthday_paradox:
    def __init__(self,trials,start,stop,step):

        self.trials=trials
        self.start=start
        self.stop=stop
        self.step=step
        

    def check_duplicates(self,n):
        return len(n) != len(set(n))


    def experiments(self,p,q):

        count=0
        

        for _ in range(q):
            
            birthdays=[random.randint(1,365) for _ in range(p)]
            
            if self.check_duplicates(birthdays):
                 
                count+=1
            
        return count/self.trials

    def loop(self):
        
        for i in range (self.start,self.stop,self.step):
            self.probability=self.experiments(i,self.trials)
            print(f"for {i} persons group , the probablity of re-occuring birthdays will be {self.probability:.2f} ")


    def __str__(self):
       
        return f"{self.loop()}"
        
        





