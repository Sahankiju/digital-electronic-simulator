import gate as G

class WireManager:
    wires={}
    def __init__(self,wire):
        WireManager.wires[wire.wireID]=wire
    def delWire(self,wireID):
        WireManager.pop(wireID)



class Wire(WireManager):
    count=0
    def __init__(self,output_gate:G.Gate,input_gate: G.Gate,pin):
        Wire.count+=1
        self.wireID=Wire.count
        self.input_gate=input_gate
        self.output_gate=output_gate
        self.pin=pin
        self.changeInput(self.pin,self.output_gate.output)
        super().__init__(self)

    def outputChanged(self):
        self.input_gate.changeInput(self.pin,self.output_gate.output)

    def changeInput(self,pin,value:int):
        if(pin=="A"):
            self.input_gate.inputA=value
        if(pin=="B"):
            self.input_gate.inputB=value