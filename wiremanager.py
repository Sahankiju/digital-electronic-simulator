import registry as RE

class WireManager:

    def __init__(self,wire):
        RE.wires[wire.wireID]=wire
    def delWire(self,wireID):
        RE.wires[wireID].output_gate.connected=False
        RE.pop(wireID)



class Wire(WireManager):
    count=0
    def __init__(self,output_gate,input_gate,pin):
        Wire.count+=1
        self.wireID=Wire.count
        self.input_gate=input_gate
        self.output_gate=output_gate
        self.pin=pin
        self.changeInput(self.pin,self.output_gate.output)
        self.output_gate.wire_id=self.wireID
        self.output_gate.connected=True
        super().__init__(self)

    def outputChanged(self):
        self.input_gate.changeInput(self.pin,self.output_gate.output)

    def changeInput(self,pin,value:int):
        if(pin=="A"):
            self.input_gate.inputA=value
            self.outputChanged()
        if(pin=="B"):
            self.input_gate.inputB=value
            self.outputChanged()