"""Gram spectral weights for the witness-fixed candidate gauge action.
Exact conditional kinetic traces, no fitted coefficients, no output files.
"""
from fractions import Fraction as F

T3=(F(0),F(0),F(1,2),F(-1,2))
Q0=(F(3),F(-1),F(-1),F(-1))
Qw=(F(0),F(2),F(-1),F(-1))
Y=tuple(q/4 for q in Qw)

def trace_pair(a,b,x,y):
    return a*x[0]*y[0]+b*sum(x[i]*y[i] for i in range(1,4))

for label,a,b in [('identity',F(1),F(1)),('Gram',F(15),F(11)),
                  ('inverse Gram',F(1,15),F(1,11)),
                  ('Gram squared',F(225),F(121))]:
    k2=trace_pair(a,b,T3,T3)
    ky=trace_pair(a,b,Y,Y)
    assert k2==b/2 and ky==3*b/8
    assert k2/(k2+ky)==F(4,7)
    assert trace_pair(a,b,Q0,Q0)==9*a+3*b
    assert trace_pair(a,b,Qw,Qw)==6*b
    assert trace_pair(a,b,Q0,Qw)==0
    print(f'{label}: weak={k2}, witness hypercharge={ky}, angle={k2/(k2+ky)}')

# In the adapted basis G=diag(15,11,11,11). Every weak generator has
# support within the last two coordinates; the charge family is diagonal.
# For matrix unit E_ij, [G,E_ij]=(G_i-G_j)E_ij.
g=(15,11,11,11)
for i,j in [(2,2),(2,3),(3,2),(3,3),(0,0),(1,1)]:
    assert g[i]-g[j]==0
print('All selected gauge generators commute with G: commutator norm is zero.')
print('For any positive W=f(G), the pinched witness angle stays exactly 4/7.')
print('Spectral-weight and commutator checks passed.')
