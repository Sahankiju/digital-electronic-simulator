class Gate():
    output=0
    inputA_connected = False
    inputB_connected = False
    def __init__(self,inputA,inputB):
        self.inputA=inputA
        self.inputB=inputB
    def evaluate(self):
        pass
    def changePin(self,input_pin,connection_pin,connected):
        if(input_pin=="A"):
            if(connected==True):
                self.inputA=connection_pin
                self.inputA_connected=True
              
            if(connected==False):
                self.inputA=0
        if(input_pin=="B"):
            if(connected==True):
                self.inputB=connection_pin
                self.inputB_connected=True
                
            if(connected==False):
                self.inputB=0       

class AND(Gate):
    count=0
    def __init__(self, inputA=0,inputB=0):
        super().__init__(inputA,inputB)
        AND.count +=1
        self.id=f"AND{AND.count}"
    def evaluate(self):
        Gate.output=self.inputA and self.inputB
        

class OR(Gate):
    count =0 
    def __init__(self, inputA=0,inputB=0):
        OR.count+=1
        self.id=f"OR{OR.count}"
        super().__init__(inputA,inputB)
    def evaluate(self):
        Gate.output=self.inputA or self.inputB
        



ANDgates={}
ORgates={}

def createANDgate(A=0,B=0):
    gate = AND(A,B)
    ANDgates[gate.id]=gate


def createORgate(A=0,B=0):
    gate = OR(A,B)
    ORgates[gate.id]=gate

createORgate(1,0)
createANDgate(1,1)
createANDgate(1,1)
createORgate()

ANDgates['AND2'].evaluate()
ORgates['OR1'].evaluate()
# connection


ANDgates['AND1'].changePin("A",ANDgates['AND2'].output,True)
ANDgates['AND1'].changePin("B",ORgates['OR1'].output,True)


ANDgates['AND1'].evaluate()

# ANDgates['AND2'].inputA=ORgates['OR1'].evaluate()
# ANDgates['AND2'].inputsB=ORgates['OR1'].evaluate()


# ORgates['OR2'].inputsA=ANDgates['AND1'].evaluate()
# ORgates['OR2'].inputsB=ANDgates['AND2'].evaluate()

print(ANDgates['AND1'].output)



