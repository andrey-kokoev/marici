"""Exact audit of the matter traces used by check_gauge_coupling_norm.py.
Convention Q=T3+Y. Three generations, optional neutral right-handed neutrino.
No running or physical common-normalization scale is inferred. No files written.
"""
from fractions import Fraction as F

# name, colour multiplicity, weak multiplicity, hypercharge
fields = [('Q_L',3,2,F(1,6)),('u_R',3,1,F(2,3)),
          ('d_R',3,1,F(-1,3)),('L_L',1,2,F(-1,2)),
          ('e_R',1,1,F(-1)),('nu_R',1,1,F(0))]
c2 = cy = F(0)
for name, colours, weak, y in fields:
    su2 = colours*F(1,2) if weak == 2 else F(0)
    u1 = colours*weak*y*y
    c2 += su2
    cy += u1
    print(f'{name}: SU2 trace={su2}, hypercharge trace={u1}')
assert c2 == 2 and cy == F(10,3)
c2 *= 3
cy *= 3
angle = c2/(c2+cy)  # conditional on g_i^2=k/C_i
assert (c2,cy,angle) == (6,10,F(3,8))
assert F(3,13) != angle
print(f'Three generations: C_SU2={c2}, C_Y={cy}')
print(f'Common inverse-trace normalization gives sin^2(theta)={angle}.')
print('Original 3/13 uses SU2=3 by omitting quark colour multiplicity there,')
print('while retaining colour multiplicity in the hypercharge trace.')

# Apply the same colour-averaging weight to both operators on quark states.
weighted2 = weighted_y = F(0)
for name, colours, weak, y in fields:
    weight = F(1, 3) if colours == 3 else F(1)
    weighted2 += weight * (colours*F(1,2) if weak == 2 else F(0))
    weighted_y += weight * colours*weak*y*y
weighted2 *= 3
weighted_y *= 3
weighted_angle = weighted2/(weighted2+weighted_y)
assert (weighted2, weighted_y, weighted_angle) == (3, F(19,3), F(9,28))
print(f'Consistent colour averaging: C_SU2={weighted2}, C_Y={weighted_y}, angle={weighted_angle}')
