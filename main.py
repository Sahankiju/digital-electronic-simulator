import wiremanager as WM
import gate as G
import registry as RE

def createANDgate(A=0,B=0):
    andgate = G.AND(A,B)
    RE.ANDgates[andgate.id]=andgate


def createORgate(A=0,B=0):
    orgate = G.OR(A,B)
    RE.ORgates[orgate.id]=orgate


createANDgate(1,1)
createANDgate(1,0)
createANDgate(1,1)
createANDgate(1,0)
createORgate(1,0)
createORgate(1,0)
createORgate(1,0)
createORgate(1,0)
createORgate(1,0)

wire1=WM.Wire(RE.ANDgates["AND1"],RE.ANDgates["AND2"],"A")
wire2=WM.Wire(RE.ORgates["OR1"],RE.ANDgates["AND2"],"B")
wire3=WM.Wire(RE.ANDgates["AND3"],RE.ORgates["OR2"],"B")
wire4=WM.Wire(RE.ANDgates["AND2"],RE.ORgates["OR2"],"A")
wire5=WM.Wire(RE.ORgates["OR3"],RE.ANDgates["AND4"],"A")
wire6=WM.Wire(RE.ORgates["OR4"],RE.ANDgates["AND4"],"B")
wire7=WM.Wire(RE.ANDgates["AND4"],RE.ORgates["OR5"],"B")
wire8=WM.Wire(RE.ORgates["OR2"],RE.ORgates["OR5"],"A")



print(RE.ORgates["OR5"].inputA)
print(RE.ORgates["OR5"].inputB)
print(RE.ORgates["OR5"].output)