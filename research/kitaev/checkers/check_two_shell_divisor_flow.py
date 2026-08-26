import hashlib
import json
from pathlib import Path

import sympy as sp


c = sp.symbols("c", positive=True)
s = sp.sqrt(1 + 8 * c**2)
a = (1 + s) / (4 * c)
expected_a_prime = -(1 + 1 / s) / (4 * c**2)

assert sp.simplify(sp.diff(a, c) - expected_a_prime) == 0
assert expected_a_prime.subs(c, sp.Rational(1, 2)) < 0
assert sp.limit(a, c, 0, dir="+") == sp.oo
assert sp.simplify(a.subs(c, 1)) == 1

# The hostile region is exactly 0<c<1: a(c)>1 reduces to c<1.
hostile_condition = sp.solve_univariate_inequality(a > 1, c)
assert hostile_condition == (c < 1)

alpha_prime = sp.simplify(expected_a_prime / sp.sqrt(a**2 - 1))
assert alpha_prime.subs(c, sp.Rational(1, 2)) < 0

samples = {}
previous_alpha = None
for c_value in (sp.Rational(1, 8), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4), sp.Rational(7, 8)):
    alpha_value = sp.N(sp.acosh(a.subs(c, c_value)), 18)
    velocity_value = sp.N(alpha_prime.subs(c, c_value), 18)
    lyapunov_value = sp.N(alpha_value * velocity_value, 18)
    assert velocity_value < 0
    assert lyapunov_value < 0
    if previous_alpha is not None:
        assert alpha_value < previous_alpha
    previous_alpha = alpha_value
    samples[str(c_value)] = {
        "alpha": str(alpha_value),
        "alpha_prime": str(velocity_value),
        "distance_squared_derivative_over_two": str(lyapunov_value),
    }

payload = {
    "status": "pass",
    "theorem": "two_shell_hostile_divisor_flows_monotonically_from_infinity_to_seam",
    "a_prime": "-(1+1/sqrt(1+8*c^2))/(4*c^2)",
    "hostile_interval": "0<c<1",
    "alpha_limit_at_zero": "+infinity",
    "alpha_limit_at_one": "0",
    "branch_independent_inward_test": "Re(z)*d_c Re(z) < 0",
    "positive_product_is_falsifier": True,
    "requires_source_oriented_parameter": True,
    "static_scalar_endpoint_determines_trajectory": False,
    "multiple_zero_implicit_velocity_admitted": False,
    "samples": samples,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "two-shell-divisor-flow.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
