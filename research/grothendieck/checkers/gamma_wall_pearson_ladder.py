import json
from pathlib import Path

import sympy as sp


x, j, a = sp.symbols("x j a")
rho_log_derivative = sp.Rational(1, 4) / x + 1 / (x - a) - 1
sigma = x * (x - a)

pearson = sp.expand(
    sp.diff(x**j * sigma, x) / x**j + sigma * rho_log_derivative
)
expected_general = (
    -x**2
    + (j + sp.Rational(19, 4)) * x
    - sp.Rational(3, 2) * (j + sp.Rational(5, 4))
)

correct_residual = sp.simplify(pearson.subs(a, sp.Rational(3, 2)) - expected_general)
wrong_wall_residual = sp.factor(pearson.subs(a, 1) - expected_general)

q = sp.symbols("q", real=True)
r = q * (1 + sp.exp(q - 1)) / (1 + sp.exp(q))
r3 = sp.factor(sp.diff(r, q, 3))
expected_r3 = (
    (sp.exp(-1) - 1)
    * sp.exp(q)
    * (
        q * sp.exp(2 * q)
        - 4 * q * sp.exp(q)
        + q
        - 3 * sp.exp(2 * q)
        + 3
    )
    / (sp.exp(q) + 1) ** 4
)
r3_residual = sp.simplify(r3 - expected_r3)
t = sp.symbols("t", positive=True)
q4_bracket = t**2 - 16 * t + 7
pearson_boundary_polynomial = x**2 - sp.Rational(19, 4) * x + sp.Rational(15, 8)
pearson_roots = sp.solve(pearson_boundary_polynomial, x)
expected_roots = [
    sp.Rational(19, 8) - sp.sqrt(241) / 8,
    sp.Rational(19, 8) + sp.sqrt(241) / 8,
]
pearson_d = sp.simplify(2 * expected_roots[1] / 3 - 1)
curvature_cubic_at_pearson_d = sp.factor(3 * pearson_d**3 - 4 * pearson_d - 8)

d1, d2, d3 = sp.symbols("d1 d2 d3")
u = sp.Function("u")
bell3_residual = sp.expand(
    (sp.diff(sp.exp(u(q)), q, 3) / sp.exp(u(q))).subs(
        {
            sp.diff(u(q), q): d1,
            sp.diff(u(q), q, 2): d2,
            sp.diff(u(q), q, 3): d3,
        }
    )
    - (d3 + 3 * d1 * d2 + d1**3)
)

result = {
    "schema": "marici.gamma_wall_pearson_ladder.v1",
    "checks": {
        "source_wall_residual_zero": correct_residual == 0,
        "wrong_wall_residual_nonzero": wrong_wall_residual != 0,
        "two_atom_third_derivative_identity": r3_residual == 0,
        "q4_bracket_positive_from_exp4_gt_16": bool(
            q4_bracket.subs(t, 16) > 0
            and sp.diff(q4_bracket, t).subs(t, 16) > 0
        ),
        "q4_cubic_response_negative": bool(sp.N(r3.subs(q, 4), 30) < 0),
        "pearson_threshold_factorization": all(
            sp.simplify(left - right) == 0
            for left, right in zip(pearson_roots, expected_roots)
        ),
        "pearson_threshold_beyond_curvature_fold": bool(
            curvature_cubic_at_pearson_d > 0 and pearson_d > sp.Rational(2, 3)
        ),
        "cubic_log_response_bell_identity": bell3_residual == 0,
    },
    "exact": {
        "pearson_polynomial": str(sp.factor(pearson.subs(a, sp.Rational(3, 2)))),
        "wrong_wall_residual": str(wrong_wall_residual),
        "two_atom_r3": str(r3),
        "two_atom_r3_at_q4": str(sp.factor(r3.subs(q, 4))),
        "pearson_boundary_polynomial": str(pearson_boundary_polynomial),
        "pearson_roots": [str(root) for root in pearson_roots],
        "curvature_cubic_at_pearson_d": str(curvature_cubic_at_pearson_d),
        "cubic_log_response_residual": str(bell3_residual),
    },
}

if not all(result["checks"].values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/gamma_wall_pearson_ladder.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
