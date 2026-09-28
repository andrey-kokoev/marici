"""Overconstrain the common matter-trace boundary with strong coupling.

Inputs: illustrative MSbar inverse EM coupling 127.95, inverse strong
coupling 8.5, MZ=91.1876 GeV. One-loop SM, no extra thresholds.
Hypercharge Q=T3+Y. Corrected three-generation matter indices (10,6,6).
Weak angle is output, never fitted. Writes no files.
"""
import math
from fractions import Fraction as F

# SU3 per generation: Q_L has TWO triplets; u_R,d_R each one.
c3_per_generation=2*F(1,2)+F(1,2)+F(1,2)
assert 3*c3_per_generation==6
A=127.95
S=8.5
MZ=91.1876
# A=16t+(11/3)ell, S=6t-7ell; ell=log(Lambda/MZ)/(2pi).
ell=(3*A-8*S)/67
t=(A-(11/3)*ell)/16
scale=MZ*math.exp(2*math.pi*ell)
y=10*t+(41/6)*ell
w=6*t-(19/6)*ell
strong=6*t-7*ell
assert t>0 and ell>0 and min(y,w,strong)>0
assert math.isclose(y+w,A,abs_tol=1e-12)
assert math.isclose(strong,S,abs_tol=1e-12)
angle=w/A
print(f'Corrected indices: CY=10, C2=6, C3=6')
print(f'Inputs: inverse EM={A}, inverse strong={S} at MZ={MZ} GeV')
print(f'Solved boundary: Lambda={scale:.9g} GeV, t={t:.9f}')
print(f'Output MSbar weak angle={angle:.9f}')
# Separate illustrative boundary from prior scale scan, no weak-angle fitting.
other_ell=math.log(1e13/MZ)/(2*math.pi)
other_t=(A-(11/3)*other_ell)/16
other_strong=6*other_t-7*other_ell
print(f'At Lambda=1e13 GeV instead: inverse strong={other_strong:.9f}, alphaS={1/other_strong:.9f}')
print('Boundary and running identities passed. Strong+EM normalization yields a weak-angle mismatch.')
