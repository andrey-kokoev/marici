import json
from pathlib import Path

import sympy as sp

gamma, mu, a, c, h = sp.symbols(
    "gamma mu a c h", positive=True, finite=True
)
Q = mu**2/(2*a)
R = gamma**2*mu**6/(2*c*a**6)
rho = sp.factor(R/Q)
rho_star = sp.Rational(44376, 275)

assert rho == gamma**2*mu**4/(c*a**5)
rho_rescaled = sp.factor(rho.subs(c, h*c))
assert rho_rescaled == rho/h
assert sp.factor(sp.diff(sp.log(rho_rescaled), h)*h) == -1

# Exact simply-transitive witness: any positive rho1 is sent to any rho2 by
# h=rho1/rho2.
rho1, rho2 = sp.symbols("rho1 rho2", positive=True)
assert sp.factor((rho1/h).subs(h, rho1/rho2)) == rho2

# A fitted realization exists, but its c value is a freely chosen source
# parameter rather than a derived relation.
c_fit = sp.factor((gamma**2*mu**4/(rho_star*a**5)))
assert sp.factor(rho.subs(c, c_fit)) == rho_star
assert sp.factor(rho.subs(c, 2*c_fit)) == rho_star/2

# The WP1009 witness ceases to be stationary under the admitted h=2 move.
z, u, v = sp.symbols("z u v", real=True)
w = sp.Rational(1, 2)-u-v
n = 2*(z**2-z+1)
A = (z+1)**2/n
B = (2*z-1)**2/n
C = (z-2)**2/n
F_half = 2*(A*u+B*v+C*w) + 4*(rho_star/2)*A*B*C*u*v*w
point = {z: 0, u: sp.Rational(25, 172), v: sp.Rational(25, 172)}
gradient_half = [
    sp.factor(sp.diff(F_half, q).subs(point)) for q in (z, u, v)
]
assert gradient_half != [0, 0, 0]

# Deliberate-failure test: erasing c from the source domain would falsely
# make rho appear fixed even though the matching formula depends on it.
assert sp.diff(rho, c) != 0

result = {
    "schema": "marici.flavor.wp1010.v1",
    "status": "PASS",
    "matched_ratio": "gamma^2 mu^4/(c a^5)",
    "required_ratio": str(rho_star),
    "source_action": "c -> h c, h>0",
    "induced_action": "rho -> rho/h",
    "logarithmic_orbit_derivative": "-1",
    "h_equals_2_witness_gradient": [str(x) for x in gradient_half],
    "classification": "conditional global selector family; no source-generated numerical ratio",
    "remaining_gate": "independent source relation breaking the positive c-rescaling orbit",
}

out = Path(__file__).parents[1] / "results" / "wp1010_global_selector_source_ratio_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1010 PASS: admitted source rescaling remains transitive on the selector ratio")

