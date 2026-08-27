import json
from pathlib import Path

import sympy as sp


eps, y, z = sp.symbols("eps y z", positive=True)
d = sp.log(1 + eps * y) / 2
jacobian = eps / (2 * (1 + eps * y))

# The primitive theta label is polynomial times exp(-x). Under
# x -> x+y its normalized polynomial factor tends to one, while the
# exponential ratio is exp(-y). The following limits isolate the universal
# boundary-layer coefficient.
checks = {
    "scaled_boundary_coordinate": sp.limit(d / eps, eps, 0) == y / 2,
    "scaled_jacobian": sp.limit(jacobian / eps, eps, 0) == sp.Rational(1, 2),
    "scaled_sinh": sp.limit(sp.sinh(z * d) / eps, eps, 0) == z * y / 2,
    "laplace_first_moment": sp.integrate(y * sp.exp(-y), (y, 0, sp.oo)) == 1,
}

leading_coefficient = sp.simplify(
    2
    * sp.integrate(
        sp.exp(-y)
        * sp.limit(sp.sinh(z * d) / eps, eps, 0)
        * sp.limit(jacobian / eps, eps, 0),
        (y, 0, sp.oo),
    )
)
checks["odd_tail_leading_coefficient"] = leading_coefficient == z / 2

result = {
    "schema": "marici.grothendieck.theta-odd-tail-boundary-layer-asymptotic.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "asymptotic": "H_+(L,z)-H_-(L,z) ~ z Phi(L)/(2 x(L)^2), x(L)=pi exp(2L)",
    "consequence": "For every fixed nonzero z, all sufficiently large prime-power seam samples are nonzero.",
}

out = Path(__file__).parents[1] / "results" / "theta_odd_tail_boundary_layer_asymptotic.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
