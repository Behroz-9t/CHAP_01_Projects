class StringCombinations:

    def __init__(self,s:str):
        
        self.s=s
        # self.string=["c","a","t","d","o","g"]
       
        # self.packet=[]
        # self.l=len(self.string)

        self.result=[]
        
        
        # self.total=""

    def char_to_str(self,s,chosen=""):

        length=len(s)
        if length==0:
            return (chosen)

        for i in range(length):

            self.comb=self.s[i]
            self.total=self.s[i]+self.s[i+1]

            self.result.extend(self.char_to_str(self.total,chosen+self.comb))
        
        
        
        
        # if self.l>0:

            # for i in range(self.l):
            #     for j in range(1,self.l):
                    
            #         self.p=(self.string[i])+(self.string[j])
            #         self.packet.append(self.p)
            #         # self.total+=self.packet
            # print (f"{self.packet}")
           
            # for i in range(self.l):
            #     for j in range(1,self.l):
            #         for k in range(2,self.l):
                    
            #             self.p=(self.string[i]+self.string[j])+(self.string[k])
            #             self.packet.append(self.p)
            #             # self.total+=self.packet
           
            # for i in range(self.l):
            #     for j in range(1,self.l):
            #         for k in range(2,self.l):
            #             for l in range(3,self.l):
                        
            #                 self.p=(self.string[i]+self.string[j]+self.string[k])+(self.string[l])
            #                 self.packet.append(self.p)
            #                 # self.total+=self.packet
           
            # for i in range(self.l):
            #     for j in range(1,self.l):
            #         for k in range(2,self.l):
            #             for l in range(3,self.l):
            #                 for m in range(3,self.l):
                        
            #                     self.p=(self.string[i]+self.string[j]+self.string[k]+self.string[l])+(self.string[m])
            #                     self.packet.append(self.p)
            #                     # self.total+=self.packet
           
            # for i in range(self.l):
            #     for j in range(1,self.l):
            #         for k in range(2,self.l):
            #             for l in range(3,self.l):
            #                 for m in range(3,self.l):
            #                     for n in range(3,self.l):
                        
            #                         self.p=(self.string[i]+self.string[j]+self.string[k]+self.string[l]+self.string[m])+(self.string[n])
            #                         self.packet.append(self.p)
            #                         # self.total+=self.packet

                 
        
        
                       
            # print(len(self.packet))
        
        
            
     

        

s=StringCombinations(['c','a','t','d','o','g'])
print(s.char_to_str())


