counts={}
class separator:
    def __init__(self,char:str=None):
        
        if char is None:
            char=input("Enter sentence:\n")
            
        self.words=list(char.split( ))
  
    def count(self):

        for i in self.words:
            counts[i]=counts.get(i,0) + 1
        
        return list(counts.items())
    
    def __str__(self):
        
        return self.words
    






        