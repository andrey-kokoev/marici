import json
from pathlib import Path

import sympy as sp


CA = sp.Integer(3)
C2F = sp.Rational(4, 3)
C2S = sp.Integer(3)
T_F = sp.Rational(1, 2)
T_ADJ = sp.Integer(3)
N_REAL_ADJ = sp.Integer(3)


def coefficients(n_dirac_fundamental):
    s2f = n_dirac_fundamental * T_F
    s2s = N_REAL_ADJ * T_ADJ
    b0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * s2f - sp.Rational(1, 6) * s2s
    b1 = (
        sp.Rational(34, 3) * CA**2
        - (4 * C2F + sp.Rational(20, 3) * CA) * s2f
        - (2 * C2S + sp.Rational(1, 3) * CA) * s2s
    )
    return sp.simplify(b0), sp.simplify(b1)


b0_high, b1_high = coefficients(sp.Integer(12))
b0_low, b1_low = coefficients(sp.Integer(6))
g2_high = sp.simplify(-16 * sp.pi**2 * b0_high / b1_high)
alpha_high = sp.simplify(g2_high / (4 * sp.pi))
loop_high = sp.simplify(g2_high / (16 * sp.pi**2))
low_bracket_at_high_root = sp.simplify(b0_low + b1_low * loop_high)

assert (b0_high, b1_high) == (sp.Rational(3, 2), -113)
assert (b0_low, b1_low) == (sp.Rational(11, 2), -37)
assert g2_high == 24 * sp.pi**2 / 113
assert alpha_high == 6 * sp.pi / 113
assert loop_high == sp.Rational(3, 226)
assert low_bracket_at_high_root == sp.Rational(566, 113)
assert low_bracket_at_high_root > 0

result = {
    "work_package": "WP465",
    "active_spectrum": {
        "ordinary_dirac_fundamentals": 6,
        "messenger_dirac_fundamentals": 6,
        "real_adjoint_scalars": 3,
        "b0": str(b0_high),
        "b1": str(b1_high),
    },
    "formal_active_spectrum_root": {
        "g_squared": str(g2_high),
        "alpha": str(alpha_high),
        "alpha_numeric": float(sp.N(alpha_high, 16)),
        "loop_coordinate": str(loop_high),
    },
    "decoupled_spectrum": {
        "dirac_fundamentals": 6,
        "b0": str(b0_low),
        "b1": str(b1_low),
        "beta_bracket_at_active_root": str(low_bracket_at_high_root),
    },
    "threshold_compatibility": "failed",
    "classification": "conditional weak active-spectrum root, not a selected finite-scale coupling after massive-messenger decoupling",
    "smallest_exact_falsifier": "low-spectrum beta bracket at the high-spectrum root equals 566/113 rather than zero",
    "selector_admitted": low_bracket_at_high_root == 0,
}

out = Path(__file__).parents[1] / "results" / "wp465_messenger_fixed_point_threshold_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

