import json
from pathlib import Path

import sympy as sp


a, b, c, q = sp.symbols("a b c q")


def shear(x):
    return sp.Matrix([[1, 0], [x, 1]])


T_ab = shear(b - a)
T_bc = shear(c - b)
T_ca = shear(a - c)

euler_log = sp.series(-2 * sp.log(1 - q), q, 0, 7).removeO()

checks = {
    "shears_add": sp.simplify(shear(a) * shear(b) - shear(a + b)) == sp.zeros(2),
    "shears_commute": sp.simplify(shear(a) * shear(b) - shear(b) * shear(a)) == sp.zeros(2),
    "endpoint_comparisons_compose": sp.simplify(T_ab * T_bc - shear(c - a)) == sp.zeros(2),
    "triangle_residual_is_identity": sp.simplify(T_ab * T_bc * T_ca - sp.eye(2)) == sp.zeros(2),
    "primitive_is_first_log_coefficient": euler_log.coeff(q, 1) == 2,
    "prime_square_is_second_log_coefficient": euler_log.coeff(q, 2) == 1,
    "all_checked_depths_share_one_logarithm": all(euler_log.coeff(q, k) == sp.Rational(2, k) for k in range(1, 7)),
}

result = {
    "schema": "marici.grothendieck.euler-jet-shear-triangle-flatness.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "Primitive, prime-square, and connected Euler currents are grades of one additive logarithmic shear. They retain boundary typing but yield no triangle curvature by themselves.",
}

out = Path(__file__).parents[1] / "results" / "euler_jet_shear_triangle_flatness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
