import hashlib
import json
from pathlib import Path

import sympy as sp


w, delta, c, u = sp.symbols("w delta c u", real=True)
z = sp.symbols("z")
F = sp.cosh(z) + c * sp.cosh(2 * z)
collision = {z: sp.I * sp.pi, c: 1}

assert sp.simplify(F.subs(collision)) == 0
assert sp.simplify(sp.diff(F, z).subs(collision)) == 0
assert sp.simplify(sp.diff(F, z, 2).subs(collision)) == 3
assert sp.simplify(sp.diff(F, c).subs(collision)) == 1

local = -sp.cosh(w) + (1 + delta) * sp.cosh(2 * w)
series = sp.series(local, w, 0, 5).removeO().expand()
assert series.coeff(w, 0) == delta
assert series.coeff(w, 2) == sp.Rational(3, 2) + 2 * delta
assert series.coeff(w, 4) == sp.Rational(5, 8) + sp.Rational(2, 3) * delta

s = sp.sqrt(1 + 8 * c**2)
a = (1 + s) / (4 * c)
a_prime_at_one = sp.simplify(sp.diff(a, c).subs(c, 1))
assert a_prime_at_one == -sp.Rational(1, 3)

acosh_unit_ratio = sp.limit(sp.acosh(1 + u) ** 2 / u, u, 0, dir="+")
acos_unit_ratio = sp.limit(sp.acos(1 - u) ** 2 / u, u, 0, dir="+")
assert acosh_unit_ratio == 2
assert acos_unit_ratio == 2

below_excess = sp.limit((a.subs(c, 1 - u) - 1) / u, u, 0, dir="+")
above_deficit = sp.limit((1 - a.subs(c, 1 + u)) / u, u, 0, dir="+")
assert below_excess == sp.Rational(1, 3)
assert above_deficit == sp.Rational(1, 3)
assert sp.simplify(acosh_unit_ratio * below_excess) == sp.Rational(2, 3)
assert sp.simplify(acos_unit_ratio * above_deficit) == sp.Rational(2, 3)

unfolding = -2 * sp.diff(F, c).subs(collision) / sp.diff(F, z, 2).subs(collision)
assert sp.simplify(unfolding) == -sp.Rational(2, 3)

payload = {
    "status": "pass",
    "theorem": "hostile_pair_crosses_threshold_by_quadratic_seam_collision",
    "collision": {"c": "1", "z": "i*pi", "multiplicity": 2},
    "collision_jet": {"F": "0", "F_z": "0", "F_zz": "3", "F_c": "1"},
    "local_normal_form": "w^2 = -(2/3)*(c-1) + O((c-1)^2)",
    "below_threshold_direction": "real transverse",
    "above_threshold_direction": "imaginary seam tangent",
    "below_squared_rate": "2/3",
    "above_squared_rate": "2/3",
    "unfolding_coefficient": "-2/3",
    "divisor_multiplicity_conserved": True,
    "simple_zero_velocity_regular_at_collision": False,
    "regular_compiler_coordinate": "quadratic divisor jet",
    "theta_unfolding_inferred": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "quadratic-seam-collision.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
