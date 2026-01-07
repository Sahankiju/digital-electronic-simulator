
import wiremanager as WM
class Gate():
    def __init__(self,inputA: int,inputB: int):
        self.inputA=inputA
        self.inputB=inputB
        self.output=0
        self.executed=False
        self.inputA_connected = False
        self.inputB_connected = False
        self.inputA_connected_with = None
        self.inputB_connected_with = None
        self.wire_id=None
        self.evaluate()
    def evaluate(self):
        pass
    def enqueue(self):
        pass
    def changeInput(self,pin :str,value: int):
        if(pin=="A"):
            self.inputA=value
            self.evaluate()
        if(pin=="B"):
            self.inputB=value
            self.evaluate()

class AND(Gate):
    count=0
    def __init__(self, inputA=0,inputB=0):
        super().__init__(inputA,inputB)
        AND.count +=1
        self.id=f"AND{AND.count}"
       
    def evaluate(self):
        self.output=self.inputA and self.inputB
        # if(temp_output != self.output):
        #     WM.wires[self.wire_id]
            
        

class OR(Gate):
    count =0
    def __init__(self, inputA=0,inputB=0):
        OR.count+=1
        self.id=f"OR{OR.count}"
        super().__init__(inputA,inputB)
        
        
    def evaluate(self):
        self.output=self.inputA or self.inputB