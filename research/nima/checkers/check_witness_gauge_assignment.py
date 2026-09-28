"""Gauge actions on witness sectors: explicit conditional complex realization.

Basis: uniform line, witness-contrast line, two contrast-plane vectors.
Unit comparison measure. No carrier-selected charge assignment is assumed.
No files written.
"""
from fractions import Fraction as F

T3 = (F(0), F(0), F(1,2), F(-1,2))
c2 = sum(t*t for t in T3)
assert c2 == F(1,2)

def readout(y0, yw, yd):
    Y = (y0,yw,yd,yd)
    cy = sum(y*y for y in Y)
    # Y is scalar on the doublet: it commutes with all three weak generators.
    assert Y[2] == Y[3]
    assert sum(y*t for y,t in zip(Y,T3)) == 0
    return cy, c2/(c2+cy)

examples = [
    ('neutral singlets, half-charged doublet', F(0),F(0),F(1,2)),
    ('one unit-charged singlet, half-charged doublet', F(1),F(0),F(1,2)),
    ('target-selected example', F(1),F(2,3),F(1,3)),
]
for label,y0,yw,yd in examples:
    cy,angle=readout(y0,yw,yd)
    print(f'{label}: Y=({y0},{yw},{yd},{yd}), C2={c2}, CY={cy}, mixing={angle}')
assert readout(F(1),F(2,3),F(1,3)) == (F(5,3),F(3,13))
assert readout(F(1),F(0),F(1,2))[1] == F(1,4)
print('Same sector geometry admits different charge normalizations and mixing fractions.')
print('Conditional action checks passed; no physical matter or anomaly construction supplied.')
