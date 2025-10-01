import random

class SentencePunishmentIterator:
        
        def __init__(self,sentence=None,stop=None):
        
                if sentence==None and stop==None:
                
                        self.sentence=input("Enter the sentence you want to write as a punishment:\n")                        
                        self.start=int(input("\nEnter the amount of times you want to write:\n"))
                       
                        print("")

        def punishment(self):
        
                self.list=[]

                for i in range(1,9):

                        self.list.append(random.randrange(1,self.start+1))
                        self.typo=sorted(self.list)
                        
       
                print(f"The typos present at index number: {self.typo}\n")
            
                for j in range(1,self.start+1):

                        if j==self.typo[0]:
                                
                                self.newsentence=self.sentence.replace("e","a",2)            
                                print(f"{j}. {self.newsentence}")

                        elif j==self.typo[1]:

                                self.newsentence=self.sentence.replace("i","",2)            
                                print(f"{j}. {self.newsentence}")

                        elif j==self.typo[2]:
                                
                                self.newsentence=self.sentence.replace("ll","l")            
                                print(f"{j}. {self.newsentence}")

                        elif j==self.typo[3]:
                                
                                self.newsentence=self.sentence.replace("m","n")            
                                print(f"{j}. {self.newsentence}")

                        elif j==self.typo[4]:
                                
                                self.newsentence=self.sentence.replace(".","",1)            
                                print(f"{j}. {self.newsentence}")

                        elif j==self.typo[5]:
                                
                                self.newsentence=self.sentence.replace("ie","ei",2)            
                                print(f"{j}. {self.newsentence}")

                        elif j==self.typo[6]:

                                self.newsentence=self.sentence.replace("m","mn",2)            
                                print(f"{j}. {self.newsentence}")

                        else:

                                print(f"{j}. {self.sentence}")
        
        def __str__(self):
                return f"{self.punishment()}"


