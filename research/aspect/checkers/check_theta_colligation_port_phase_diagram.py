import json
from pathlib import Path

import sympy as sp


r, y = sp.symbols("r y", real=True)
f = 2 * sp.exp(-sp.pi * y)
Q = sp.Matrix([[1, 2 * r], [2 * r, 1]])
rho = sp.simplify(f**2 / Q.det())
yc = (sp.log(2) - sp.log(1 - 4 * r**2) / 2) / sp.pi

checks = {
    "Q_determinant": sp.simplify(Q.det() - (1 - 4 * r**2)) == 0,
    "Q_eigenvalues": set(Q.eigenvals()) == {1 - 2 * r, 1 + 2 * r},
    "rho_formula": sp.simplify(rho - 4 * sp.exp(-2 * sp.pi * y) / (1 - 4 * r**2)) == 0,
    "boundary_solves_rho_one": sp.simplify(rho.subs(y, yc) - 1) == 0,
    "reflection_symmetry": sp.simplify(rho.subs(r, -r) - rho) == 0,
    "boundary_seam": sp.simplify(yc.subs(r, 0) - sp.log(2) / sp.pi) == 0,
    "boundary_monotone_r_positive": sp.simplify(sp.diff(yc, r) - 4 * r / (sp.pi * (1 - 4 * r**2))) == 0,
    "two_output_sample": sp.simplify(rho.subs({r: 0, y: sp.log(2) / sp.pi}) - 1) == 0,
    "three_output_sample": sp.simplify(rho.subs({r: 0, y: sp.log(4) / sp.pi}) - sp.Rational(1, 4)) == 0,
    "three_output_slack": sp.simplify(sp.sqrt(1 - rho.subs({r: 0, y: sp.log(4) / sp.pi})) - sp.sqrt(3) / 2) == 0,
    "extra_input_sample": sp.simplify(rho.subs({r: 0, y: sp.log(2) / (2 * sp.pi)}) - 2) == 0,
}

result = {
    "schema": "marici.aspect.theta-colligation-port-phase-diagram.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": {name: bool(value) for name, value in checks.items()},
    "check_count": len(checks),
    "formulas": {
        "rho": "4 exp(-2*pi*y)/(1-4*r^2)",
        "critical_y": "(log(2)-log(1-4*r^2)/2)/pi",
    },
    "regimes": {
        "rho_lt_1": "three outputs; slack sqrt(1-rho)",
        "rho_eq_1": "two-output lossless completion",
        "rho_gt_1": "additional independent input reservoir or indefinite completion",
    },
}

out = Path(__file__).parents[1] / "results" / "theta_colligation_port_phase_diagram.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
