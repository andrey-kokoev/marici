import json
from pathlib import Path

import sympy as sp


r, f = sp.symbols("r f", real=True)
Q = sp.Matrix([[1, 2 * r], [2 * r, 1]])
b = sp.Matrix([-f, 0])
rho = sp.simplify((b.T * Q.inv() * b)[0])

# A canonical square root is unnecessary: for every C with C* C = Q,
# the least-norm solution of C* d = -b has norm squared b* Q^-1 b.
# Appending columns to D cannot change the norm requirement on its first column.
inverse_residual = Q.inv() - sp.Matrix([[1, -2 * r], [-2 * r, 1]]) / (1 - 4 * r**2)

checks = {
    "Q_inverse": all(sp.simplify(entry) == 0 for entry in inverse_residual),
    "forced_column_minimum_norm": sp.simplify(rho - f**2 / (1 - 4 * r**2)) == 0,
    "theta_overdrive_sample": sp.simplify(rho.subs({r: 0, f: sp.sqrt(2)}) - 2) == 0,
    "unit_column_contradiction": bool(sp.sqrt(2) > 1),
    "boundary_sample": sp.simplify(rho.subs({r: 0, f: 1}) - 1) == 0,
    "contractive_sample": sp.simplify(rho.subs({r: 0, f: sp.Rational(1, 2)}) - sp.Rational(1, 4)) == 0,
}

result = {
    "schema": "marici.aspect.theta-extra-input-no-go.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "theorem": "Appending positive lossless input columns cannot repair rho>1 with the original source column fixed.",
    "repairs": [
        "renormalize or split the original source excitation",
        "change the state balance Q through an active reservoir coupling",
        "change the positive state metric",
        "use an indefinite supply metric",
    ],
}

out = Path(__file__).parents[1] / "results" / "theta_extra_input_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
