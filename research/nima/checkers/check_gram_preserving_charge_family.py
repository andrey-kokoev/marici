"""Gram-preserving witness-sector charges and invariant trace metric.
Adapted orthonormal basis: uniform, witness contrast, contrast doublet.
No files written; exact rational checks.
"""
from fractions import Fraction as F

def dot(x,y): return sum(a*b for a,b in zip(x,y))
G=(F(15),F(11),F(11),F(11))
Q0=(F(3),F(-1),F(-1),F(-1))
Qw=(F(0),F(2),F(-1),F(-1))
T3=(F(0),F(0),F(1,2),F(-1,2))
assert sum(Q0)==sum(Qw)==0
assert dot(Q0,Q0)==12 and dot(Qw,Qw)==6
assert dot(Q0,Qw)==dot(Q0,T3)==dot(Qw,T3)==0
assert dot(T3,T3)==F(1,2)

# Witness projector has diagonal (1/4,3/4,0,0) in this basis.
# Spectral dephasing removes its offdiagonal uniform/contrast entries.
Ypin=(F(0),F(1,2),F(-1,4),F(-1,4))
assert Ypin==tuple(q/4 for q in Qw)
assert dot(Ypin,Ypin)==F(3,8)
angle=F(1,2)/(F(1,2)+dot(Ypin,Ypin))
assert angle==F(4,7)
for x,y in [(F(1),F(0)),(F(0),F(1)),(F(1,3),F(1,4))]:
    Y=tuple(x*a+y*b for a,b in zip(Q0,Qw))
    assert dot(Y,Y)==12*x*x+6*y*y
    assert sum(Y)==0 and Y[2]==Y[3]
print('Gram-compatible traceless charge family: Y=x Q0+y Qw.')
print('Trace metric diag(12,6); weak T3 norm squared=1/2.')
print('Pinched witness charge Qw/4: trace square=3/8, conditional angle=4/7.')
print('Target 3/13 requires 12*x^2+6*y^2=5/3 under unit trace metric.')
print('Exact family checks passed; symmetry leaves x,y and kinetic coefficients free.')
