import json

import sympy as sp


x, a, c = sp.symbols("x a c", positive=True)
T = sp.Function("T")(x)
H = sp.Function("H")(x)
f = sp.Function("f")(x)

tail_rule = {sp.diff(T, x): -a * T - f}
residual_rule = {sp.diff(H, x) * T: (H - 1) * f}
Y = (H - 1) * T
Y_prime = sp.diff(Y, x).subs(tail_rule).subs(residual_rule)

# An exact source-shaped representative makes the endpoint mismatch explicit.
# T0 has the theta superexponential scale; Y0 is the only homogeneous defect.
T0 = sp.exp(-sp.pi * sp.exp(2 * x))
Y0 = c * sp.exp(-a * x)
multiplier_defect = sp.simplify(Y0 / T0)

checks = {
    "defect_obeys_homogeneous_equation": sp.simplify(Y_prime + a * Y) == 0,
    "homogeneous_solution_is_exponential": sp.simplify(
        sp.diff(Y0, x) + a * Y0
    )
    == 0,
    "theta_tail_is_superexponential": sp.limit(
        sp.exp(a * x) * T0, x, sp.oo
    )
    == 0,
    "nonzero_defect_forces_unbounded_multiplier": sp.limit(
        multiplier_defect.subs(c, 1), x, sp.oo
    )
    == sp.oo,
    "zero_defect_selects_identity_multiplier": sp.simplify(
        multiplier_defect.subs(c, 0)
    )
    == 0,
}

result = {
    "schema": "marici.aspect.common-forcing-tail-rigidity.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "residual_gate": "H' T + (1-H) f = 0",
    "homogeneous_defect": "Y=(H-1)T=c exp(-a x)",
    "endpoint_multiplier_defect": str(multiplier_defect),
    "interpretation": (
        "Same-forcing preservation leaves only an exponential homogeneous "
        "defect, and theta endpoint admissibility removes it."
    ),
}

print(json.dumps(result, indent=2))
