"""Test existing C_i/lambda_i boundary after correcting matter counts.
Inputs EM and strong at MZ; weak angle output. One-loop SM, no thresholds.
Two readings of the historical U1 normalization are kept separate.
No files written.
"""
import math
from fractions import Fraction as F
A,S,MZ=127.95,8.5,91.1876
C=(F(10),F(6),F(6))
lam=(F(12),F(4),F(4))
# Inverse-coupling boundary proportional to lambda_i/C_i.
inverse=tuple(l/c for l,c in zip(lam,C))
assert inverse[0]/inverse[1]==F(9,5)
assert inverse[2]/inverse[1]==1

# Boundary alphaY^-1 = r*t, alpha2^-1=alpha3^-1=t.
def solve(r):
    r=float(r)
    ell=(A-(r+1)*S)/(7*(r+1)+11/3)
    t=S+7*ell
    y=r*t+(41/6)*ell
    w=t-(19/6)*ell
    strong=t-7*ell
    assert min(t,y,w,strong)>0
    assert math.isclose(y+w,A,abs_tol=1e-12)
    assert math.isclose(strong,S,abs_tol=1e-12)
    return MZ*math.exp(2*math.pi*ell),w/A

for name,r in [('common trace control',F(5,3)),
               ('C/lambda: unrescaled hypercharge',F(9,5)),
               ('C/lambda numbers assigned to GUT-normalized g1',F(3))]:
    scale,angle=solve(r)
    print(f'{name}: inverse boundary ratio=({r},1,1), Lambda={scale:.9g} GeV, angle={angle:.9f}')
print('GUT conversion: g1^2=(5/3)gY^2, alphaY^-1=(5/3)alpha1^-1.')
print('Second historical reading retains its numeric boundary then converts; it is a distinct ansatz.')
print('All normalization/running identities passed; all three outputs miss the weak-angle neighbourhood.')
