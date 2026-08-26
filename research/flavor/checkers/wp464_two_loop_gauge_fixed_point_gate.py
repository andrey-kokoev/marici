import json
from pathlib import Path

import sympy as sp


CA = sp.Integer(3)
C2F = sp.Rational(4, 3)
C2S = sp.Integer(3)
S2F = sp.Integer(6) * sp.Rational(1, 2)
S2S = sp.Integer(3) * sp.Integer(3)

b0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * S2F - sp.Rational(1, 6) * S2S
b1 = (
    sp.Rational(34, 3) * CA**2
    - (4 * C2F + sp.Rational(20, 3) * CA) * S2F
    - (2 * C2S + sp.Rational(1, 3) * CA) * S2S
)
g2_star = sp.simplify(-16 * sp.pi**2 * b0 / b1)
alpha_star = sp.simplify(g2_star / (4 * sp.pi))
width_ratio = alpha_star

assert b0 == sp.Rational(11, 2)
assert b1 == -37
assert g2_star == 88 * sp.pi**2 / 37
assert alpha_star == 22 * sp.pi / 37
assert sp.simplify(width_ratio - 1) > 0

result = {
    "work_package": "WP464",
    "domain": {
        "gauge_group": "SU(3)_F",
        "dirac_fundamentals": 6,
        "real_adjoint_scalars": 3,
        "yukawa_beta_contribution_included": False,
        "thresholds_included": False,
    },
    "coefficients": {"b0": str(b0), "b1": str(b1)},
    "formal_root": {
        "g_squared": str(g2_star),
        "alpha": str(alpha_star),
        "alpha_numeric": float(sp.N(alpha_star, 16)),
    },
    "width_gate": {
        "gamma_over_mass": str(width_ratio),
        "gamma_over_mass_numeric": float(sp.N(width_ratio, 16)),
        "excess_over_unity": str(sp.simplify(width_ratio - 1)),
    },
    "classification": "formal two-loop root outside admitted perturbative pole domain",
    "selector_admitted": bool(width_ratio < 1),
}

out = Path(__file__).parents[1] / "results" / "wp464_two_loop_gauge_fixed_point_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

