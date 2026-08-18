"""Audit the oriented disappearing-triple boundary and its normal coefficient."""

import sympy as sp

a, b, c = sp.symbols("a b c")
x, y, z = sp.symbols("X1 X2 X3")
n2, n3 = sp.symbols("nu2 nu3")

l2 = y + a + c
l3 = z + a + b
l23 = y + z + b + c

def iterated_residue(pair, remaining):
    pair_jacobian = sp.det(
        sp.Matrix([[sp.diff(line, a), sp.diff(line, b)] for line in pair])
    )
    solution = sp.solve(pair, (a, b), dict=True)[0]
    restricted = sp.expand(remaining.subs(solution))
    slope = sp.diff(restricted, c)
    return sp.simplify(1 / (pair_jacobian * slope)), restricted

r_23, remaining_23 = iterated_residue((l2, l3), l23)
r_2_23, remaining_2_23 = iterated_residue((l2, l23), l3)
r_3_23, remaining_3_23 = iterated_residue((l3, l23), l2)

assert (r_23, r_2_23, r_3_23) == (sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2))
assert tuple(sp.solve(expr, c)[0] for expr in (remaining_23, remaining_2_23, remaining_3_23)) == (-y, -y, -y)

t2 = z**2 * n2**2 + (x**2 - y**2 - z**2) * n2 * n3 + y**2 * n3**2
incidence = sp.Matrix([1, -1, 1])

# Entry 707 discriminant-symbol matrix restricted to the three nu2*nu3 columns.
l1 = x - y - z
l2e = x - y + z
l3e = x + y - z
l4 = x + y + z
c_minus = -4 * l1 * l2e**2 * l3e**2 * l4
c_plus = -4 * l1**2 * l2e * l3e * l4**2
symbol_row = sp.Matrix([[c_minus, c_plus, c_plus]])

assert symbol_row * incidence == sp.Matrix([c_minus])
assert c_minus != 0

print("PAIR_ORDER=[g2g3,g2g23,g3g23]")
print("ITERATED_RESIDUES=[1/2,-1/2,1/2]")
print("ORIENTED_INCIDENCE=[1,-1,1]")
print("PLUS_OCCURRENCE_TERMS_CANCEL=true")
print("DISCRIMINANT_SYMBOL_OF_BOUNDARY=C23minus")
print("WEIGHTED_SYMBOL_KERNEL_LIFT=false")
print(f"SECOND_REES_COSTALK_COVER=eta^2-({t2})")
