"""Test which Entry 707 branch-symbol relations lift to pair residue geometry."""

import json
from pathlib import Path

import sympy as sp

root = Path(__file__).resolve().parents[2]
data = json.loads((root / "research/benincasa/generic_lower_collision_result.json").read_text())

a, b, c = sp.symbols("a b c")
X1, X2, X3, P1, P2, P3 = sp.symbols("X1 X2 X3 P1 P2 P3")
locals_ = {str(v): v for v in (a, b, c, X1, X2, X3, P1, P2, P3)}

pairs = data["pairs"]
k_2_23 = sp.sympify(pairs["g2__g23"]["restriction"], locals=locals_)
k_3_23 = sp.sympify(pairs["g3__g23"]["restriction"], locals=locals_)
assert sp.expand(k_2_23 - k_3_23) == 0

l2 = X2 + a + c
l3 = X3 + a + b
l23 = X2 + X3 + b + c
j_2_23 = sp.det(sp.Matrix([[sp.diff(l2, a), sp.diff(l2, b)], [sp.diff(l23, a), sp.diff(l23, b)]]))
j_3_23 = sp.det(sp.Matrix([[sp.diff(l3, a), sp.diff(l3, b)], [sp.diff(l23, a), sp.diff(l23, b)]]))
assert j_2_23 == j_3_23 == 1

delta_minus = sp.sympify(pairs["g2__g3"]["discriminant"], locals=locals_)
delta_plus = sp.sympify(pairs["g2__g23"]["discriminant"], locals=locals_)
ratio = sp.factor(delta_minus / delta_plus)
expected_ratio = sp.factor((P1**2 - (X2 - X3) ** 2) / (P1**2 - (X2 + X3) ** 2))
assert sp.factor(ratio - expected_ratio) == 0

numerator, denominator = sp.fraction(ratio)
for polynomial in (numerator, denominator):
    _, factors = sp.factor_list(polynomial)
    assert any(exponent % 2 for _, exponent in factors)

print("PLUS_OCCURRENCE_RESTRICTIONS_IDENTICAL=true")
print("PLUS_OCCURRENCE_RESIDUE_JACOBIANS=1,1")
print("PLUS_DIFFERENCE_LIFTS_STRICTLY=true")
print(f"SIGNED_DISCRIMINANT_RATIO={ratio}")
print("SIGNED_DISCRIMINANT_RATIO_SQUARE=false")
print("SIGNED_RELATION_RATIONAL_RESIDUE_ISOMORPHISM=false")
