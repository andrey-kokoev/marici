"""Compute the labelled normal expansion of the disappearing lower triple."""

import json
from pathlib import Path

import sympy as sp

root = Path(__file__).resolve().parents[2]
data = json.loads((root / "research/benincasa/generic_lower_collision_result.json").read_text())

x, y, z = sp.symbols("X1 X2 X3")
p1, p2, p3 = sp.symbols("P1 P2 P3")
u1, u2, u3 = sp.symbols("U1 U2 U3")
n1, n2, n3 = sp.symbols("nu1 nu2 nu3")
locals_ = {str(v): v for v in (x, y, z, p1, p2, p3)}
raw = sp.sympify(data["triples"]["g2__g3__g23"]["K_value"], locals=locals_)

poly_p = sp.Poly(raw, p1, p2, p3)
raw_squared = 0
for monomial, coefficient in poly_p.terms():
    assert all(exponent % 2 == 0 for exponent in monomial)
    raw_squared += (
        coefficient
        * u1 ** (monomial[0] // 2)
        * u2 ** (monomial[1] // 2)
        * u3 ** (monomial[2] // 2)
    )

normal = sp.expand(raw_squared.subs({u1: x**2 + n1, u2: y**2 + n2, u3: z**2 + n3}))
poly_n = sp.Poly(normal, n1, n2, n3)

def grade(degree: int) -> sp.Expr:
    return sp.factor(
        sum(
            coefficient * n1 ** monomial[0] * n2 ** monomial[1] * n3 ** monomial[2]
            for monomial, coefficient in poly_n.terms()
            if sum(monomial) == degree
        )
    )

grade_0 = grade(0)
grade_1 = grade(1)
grade_2 = grade(2)
grade_3 = grade(3)
expected_2 = z**2 * n2**2 + (x**2 - y**2 - z**2) * n2 * n3 + y**2 * n3**2

assert grade_0 == 0
assert grade_1 == 0
assert sp.expand(grade_2 - expected_2) == 0
assert grade_3 == n1 * n2 * n3

discriminant = sp.factor((x**2 - y**2 - z**2) ** 2 - 4 * y**2 * z**2)
signed_energy_product = (x - y - z) * (x - y + z) * (x + y - z) * (x + y + z)
assert sp.expand(discriminant - signed_energy_product) == 0

print("TRIPLE=g2,g3,g23")
print("NORMAL_ORDERS_0_1_ZERO=true")
print(f"GRADE_2={grade_2}")
print(f"GRADE_2_DISCRIMINANT={discriminant}")
print(f"GRADE_3={grade_3}")
print("GRADE_2_MIXES_DIAGONAL_AND_SQUARE_FREE=true")
