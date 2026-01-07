import wiremanager as WM
import gate as G




ANDgates={}
ORgates={}

def createANDgate(A=0,B=0):
    andgate = G.AND(A,B)
    ANDgates[andgate.id]=andgate


def createORgate(A=0,B=0):
    orgate = G.OR(A,B)
    ORgates[orgate.id]=orgate

createORgate(1,0)
createANDgate(1,1)
createANDgate(1,1)
createORgate()

wire1=WM.Wire(ANDgates["AND1"],ORgates["OR2"],"A")
wire2=WM.Wire(ANDgates["AND2"],ORgates["OR2"],"B")



print(ANDgates["AND2"].inputA)
print(ANDgates["AND2"].inputB)


print(ANDgates["AND2"].output)
print(ORgates["OR2"].inputA)
print(ORgates["OR2"].inputB)