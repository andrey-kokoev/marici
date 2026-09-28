"""Common positive colour-blind quark/lepton measure audit.

Q=T3+Y. Weight q per quark state and ell per lepton state, consistently
for both gauge operators. Traces below are per generation.
Writes no artifacts; no observed coupling is used.
"""
from fractions import Fraction as F


def traces(q, ell):
    return (F(3,2)*q+F(1,2)*ell, F(11,6)*q+F(3,2)*ell)


def angle(q, ell):
    c2, cy = traces(q, ell)
    return c2/(c2+cy)


assert angle(F(1), F(1)) == F(3,8)
assert angle(F(1,3), F(1)) == F(9,28)
assert angle(F(0), F(1)) == F(1,4)
assert angle(F(1), F(0)) == F(9,20)
# For q,ell >= 0, 10*C2 - 3*CY = (19*q+ell)/2.
# Target C2/(C2+CY)=3/13 requires 10*C2=3*CY.
for q, ell in [(F(1),F(1)), (F(1,3),F(1)), (F(0),F(1)), (F(1),F(0))]:
    c2, cy = traces(q,ell)
    assert 10*c2-3*cy == (19*q+ell)/2
    assert F(1,4) <= angle(q,ell) <= F(9,20)
    print(f'q={q}, ell={ell}: C2={c2}, CY={cy}, angle={angle(q,ell)}')
print('All nonzero nonnegative two-weight measures have angle in [1/4,9/20].')
print('3/13 requires ell=-19*q, so no such positive measure realizes it.')

# Broader positive measures can realize 3/13. Example: retain unit weight
# on every multiplet except e_R, whose weight is z. Then C2=2,
# CY=7/3+z. Solving the target gives z=13/3.
z = F(13,3)
c2, cy = F(2), F(7,3)+z
assert c2/(c2+cy) == F(3,13)
print(f'Multiplet-specific target fit: e_R weight={z}, all others=1 gives 3/13.')
print('This weight is inferred from the target; carrier selection is unspecified.')
