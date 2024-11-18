from Crypto.Util.number import bytes_to_long
from numpy import eye, matrix
from random import randint
from secret import flag

assert len(flag) % 4 == 0
Length = len(flag)//4

Noise   = [[randint( 1, pow(2,90) ) for i in range(4)] for j in range(4)]

Noise[0]= [bytes_to_long(flag[i * Length : (i+1)* Length]) for i in range(4)]
M   = matrix(Noise)

def Orthogonal_Matrix(n, p):
    up  = matrix(eye(n, dtype=int))
    low = matrix(eye(n, dtype=int))
    for i in range(n-1):
        for j in range(i+1, n):    
            up[ i,j] = randint(1, p)
            low[j,i] = randint(1, p)
    return up * low

C = Orthogonal_Matrix(4, 65537)

print((C*M).tolist())

'''
[[1849784703482951012865152264025674575, 2664848085955925754350117767673627932, 2099783527396520151610274180590854166, 1020558595577301617108111920545804527], [1207449566811121614020334020195802372, 1954621976999112878661150903673543232, 1326050406731534201574943690688237338, 1361813208094227445768111591959011963], [888810907577479776819993141014777624, 1216302736807928240875874427765340645, 1027359437421599069599327712873719567, 238961447144792739830554790892164336], [60622164517940943037274386912282, 82958508138755168576836012717468, 70072118066826856564329627650828, 16296740862142507745322242235326]]
'''