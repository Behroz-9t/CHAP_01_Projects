class StringCombinations:

    def __init__(self,string:list=None):
        
        if string==None:
            self.string=str(input("Enter the Characters without space in-between them:\n"))
        
        self.packet=[]
        self.l=len(self.string)       
        
        
    def char_to_str(self):

        
        if self.l>0:

            for i in range(self.l):
                for j in range(self.l):

                    if i!=j:
                    
                        self.p=(self.string[i])+(self.string[j])
                        self.packet.append(self.p)
                        
           
            for i in range(self.l):
                for j in range(self.l):
                    for k in range(self.l):
                        if len({i,j,k})==3:
                            self.p=(self.string[i]+self.string[j])+(self.string[k])
                            self.packet.append(self.p)
                            
           
            for i in range(self.l):
                for j in range(self.l):
                    for k in range(self.l):
                        for l in range(self.l):
                            if len({i,j,k,l})==4:
                                self.p=(self.string[i]+self.string[j]+self.string[k])+(self.string[l])
                                self.packet.append(self.p)
                                
           
            for i in range(self.l):
                for j in range(self.l):
                    for k in range(self.l):
                        for l in range(self.l):
                            for m in range(self.l):
                                if len({i,j,k,l,m})==5:
                                    self.p=(self.string[i]+self.string[j]+self.string[k]+self.string[l])+(self.string[m])
                                    self.packet.append(self.p)
                                    
           
            for i in range(self.l):
                for j in range(self.l):
                    for k in range(self.l):
                        for l in range(self.l):
                            for m in range(self.l):
                                for n in range(self.l):
                                    if len({i,j,k,l,m,n})==6:
                                        self.p=(self.string[i]+self.string[j]+self.string[k]+self.string[l]+self.string[m])+(self.string[n])
                                        self.packet.append(self.p)
                                        
        
            print(f"The Total number of combinations will be: {len(self.packet)}\n")

    def __str__(self):

        self.char_to_str()
        self.answer="n"
        self.answer=input("Do you want to print all the combinations? y/n\n")
        
        if self.answer=="y":        
            return f"\n{self.packet}"
        else:
            return f"\nProgram executed sucessfully!"
        
            
     

        



