import hashlib
import json
from pathlib import Path

import sympy as sp


c, eps = sp.symbols("c eps", positive=True)
y = sp.symbols("y")

disc = sp.sqrt(1 + 8 * c**2)
y_plus = (-1 + disc) / (4 * c)
y_minus = (-1 - disc) / (4 * c)
a = -y_minus
polynomial = 2 * c * y**2 + y - c

assert sp.simplify(polynomial.subs(y, y_plus)) == 0
assert sp.simplify(polynomial.subs(y, y_minus)) == 0
assert sp.simplify(a.subs(c, 1)) == 1
assert sp.simplify(sp.diff(a, c).subs(c, 1)) == -sp.Rational(1, 3)

linear_excess = sp.simplify(sp.limit((a.subs(c, 1 - eps) - 1) / eps, eps, 0, dir="+"))
assert linear_excess == sp.Rational(1, 3)

# arcosh(1+u)^2/u -> 2, composed with the exact excess above.
u = sp.symbols("u", positive=True)
arcosh_ratio = sp.limit(sp.acosh(1 + u) ** 2 / u, u, 0, dir="+")
assert arcosh_ratio == 2
square_rate = sp.simplify(arcosh_ratio * linear_excess)
assert square_rate == sp.Rational(2, 3)

samples = {}
for cutoff in (2, 4, 8, 16, 32):
    c_value = sp.Rational(cutoff - 1, cutoff)
    a_value = sp.N(a.subs(c, c_value), 18)
    alpha_value = sp.N(sp.acosh(a_value), 18)
    assert a_value > 1
    samples[str(cutoff)] = {
        "c": str(c_value),
        "a": str(a_value),
        "off_seam_distance": str(alpha_value),
    }

payload = {
    "status": "pass",
    "theorem": "hostile_cosh_pair_collapses_to_seam_at_square_root_rate",
    "negative_cosh_root": "-(1+sqrt(1+8*c^2))/(4*c)",
    "threshold": "c=1",
    "a_at_threshold": "1",
    "a_derivative_at_threshold": "-1/3",
    "limit_alpha_squared_over_one_minus_c": "2/3",
    "asymptotic": "alpha(c) ~ sqrt(2*(1-c)/3)",
    "finite_hostile_limit_confined_family": "c_N=1-1/N",
    "uniform_off_seam_gap": False,
    "samples": samples,
    "theta_completion_identified": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "hostile-cosh-seam-collision.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
