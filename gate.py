
import registry as RE



class Gate():

    def __init__(self,inputA: int,inputB: int):
        self.inputA=inputA
        self.inputB=inputB
        self.output=0
        self.wire_id=None
        self.connected=False
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
        temp_output=int(self.inputA and self.inputB)
        if(self.connected==True):
            if(temp_output != self.output):
                RE.wires[self.wire_id].outputchanged()
        self.output=temp_output   
        

class OR(Gate):
    count =0
    def __init__(self, inputA=0,inputB=0):
        OR.count+=1
        self.id=f"OR{OR.count}"
        super().__init__(inputA,inputB)
        
        
    def evaluate(self):
        temp_output=int(self.inputA or self.inputB)
        if(self.connected==True):
            if(temp_output != self.output):
                RE.wires[self.wire_id].outputchanged()
        self.output=temp_output   


class NOT(Gate):
    count=0
    def __init__(self, inputA=0):
        NOT.count += 1
        self.id=f"NOT{NOT.count}"
        super().__init__(inputA,inputA)
    
    def evaluate(self):
        temp_output=int( not self.inputA)
        if(self.connected==True):
            if(temp_output != self.output):
                RE.wires[self.wire_id].outputchanged()
        self.output=temp_output


class XOR(Gate):
    count =0
    def __init__(self, inputA=0,inputB=0):
        XOR.count+=1
        self.id=f"XOR{XOR.count}"
        super().__init__(inputA,inputB)
        
        
    def evaluate(self):
        temp_output=self.inputA ^ self.inputB
        if(self.connected==True):
            if(temp_output != self.output):
                RE.wires[self.wire_id].outputchanged()
        self.output=temp_output


class XNOR(Gate):
    count =0
    def __init__(self, inputA=0,inputB=0):
        XOR.count+=1
        self.id=f"XOR{XOR.count}"
        super().__init__(inputA,inputB)
        
        
    def evaluate(self):
        temp_output=int(not(self.inputA ^ self.inputB))
        if(self.connected==True):
            if(temp_output != self.output):
                RE.wires[self.wire_id].outputchanged()
        self.output=temp_output