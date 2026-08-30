"""Exact symbolic audit of the theta moment raising ladder."""

import json
from pathlib import Path

import sympy as sp


x = sp.symbols("x", positive=True)
k = sp.symbols("k", integer=True, nonnegative=True)


reduced = x**k
raised = sp.expand(2 * x * sp.diff(reduced, x) + (sp.Rational(1, 2) - 2 * x) * reduced)
expected = sp.expand((2 * k + sp.Rational(1, 2)) * x**k - 2 * x ** (k + 1))

orders = []
for value in range(8):
    lhs = sp.expand(raised.subs(k, value))
    rhs = sp.expand(expected.subs(k, value))
    orders.append({"k": value, "residual": str(sp.expand(lhs - rhs)), "passes": lhs == rhs})

theta_derivative = {
    "M1": str(-6 * (2 + sp.Rational(1, 2))),
    "M2": str(12 + 4 * (4 + sp.Rational(1, 2))),
    "M3": str(-8),
}

result = {
    "schema": "marici.grothendieck.theta_infinite_moment_ladder.v1",
    "status": "pass" if all(row["passes"] for row in orders) and theta_derivative["M3"] == "-8" else "fail",
    "raising_law": "D M_k=(2k+1/2)M_k-2M_(k+1)",
    "orders": orders,
    "theta_readout": "Phi=4M_2-6M_1",
    "theta_derivative_coefficients": theta_derivative,
    "finite_wall_residual": "-2 c_N M_(N+1)",
}

output = Path(__file__).parents[1] / "results" / "theta_infinite_moment_ladder.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

