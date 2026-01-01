class Gate():
    def __init__(self,inputs):
        self.inputs=inputs
        self.output=0
    def evaluate(self):
        pass

class AND(Gate):
    count=0
    def __init__(self, inputA=0,inputB=0):
        self.inputA=inputA
        self.inputB=inputB
        super().__init__([inputA,inputB])
        AND.count +=1
        self.id=f"AND{AND.count}"
    def evaluate(self):
          self.output=all(self.inputs)
          return self.output

class OR(Gate):
    count =0 
    def __init__(self, inputA=0,inputB=0):
        OR.count+=1
        self.id=f"OR{OR.count}"
        self.inputA=inputA
        self.inputB=inputB
        super().__init__([inputA,inputB])

    def evaluate(self):
            self.output=any(self.inputs)
            return self.output



ANDgates={}
ORgates={}

def createANDgate(A=0,B=0):
    gate = AND(A,B)
    ANDgates[gate.id]=gate


def createORgate(A=0,B=0):
    gate = OR(A,B)
    ORgates[gate.id]=gate

createORgate(0,0)
createANDgate(1,1)
createANDgate(1,1)
createORgate()


# connection

ANDgates['AND2'].inputs[0]=ORgates['OR1'].evaluate()
ANDgates['AND2'].inputs[1]=ORgates['OR1'].evaluate()


ORgates['OR2'].inputs[0]=ANDgates['AND1'].evaluate()
ORgates['OR2'].inputs[1]=ANDgates['AND2'].evaluate()

print(ORgates['OR1'].evaluate())