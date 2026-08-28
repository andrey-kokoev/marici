import json
from pathlib import Path

import sympy as sp


r, f = sp.symbols("r f", real=True, nonzero=True)
Q = sp.Matrix([[1, 2 * r], [2 * r, 1]])
b = sp.Matrix([-f, 0])
rho = sp.simplify((b.T * Q.inv() * b)[0])
delta = sp.simplify((rho - 1) / rho) * (b * b.T)
Q_active = sp.simplify(Q + delta)
rho_active = sp.simplify((b.T * Q_active.inv() * b)[0])
normalized_cost = sp.simplify(sp.trace(Q.inv() * delta))

checks = {
    "rho": sp.simplify(rho - f**2 / (1 - 4 * r**2)) == 0,
    "rank_one_update": sp.simplify(delta.det()) == 0,
    "boundary_saturation": sp.simplify(rho_active - 1) == 0,
    "normalized_cost": sp.simplify(normalized_cost - (rho - 1)) == 0,
    "zero_on_original_boundary": all(
        sp.simplify(e.subs(f**2, 1 - 4 * r**2)) == 0 for e in delta
    ),
    "seam_overdrive_update": delta.subs({r: 0, f: sp.sqrt(2)}) == sp.diag(1, 0),
    "seam_repaired_balance": Q_active.subs({r: 0, f: sp.sqrt(2)}) == sp.diag(2, 1),
    "seam_repaired_rho": sp.simplify(rho_active.subs({r: 0, f: sp.sqrt(2)}) - 1) == 0,
}

result = {
    "schema": "marici.aspect.minimal-active-theta-reservoir.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "update": "Delta_* = ((rho-1)/rho) b b^*",
    "optimal_cost": "Tr(Q^-1 Delta_*) = rho-1",
    "interpretation": "one active balance-changing mode aligned with the theta source",
}

out = Path(__file__).parents[1] / "results" / "minimal_active_theta_reservoir.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
