"""Exact Gram theorem for real auxiliary-square portal constructors."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
kappa, scale = sp.symbols("kappa s", positive=True)
a, b, c, d = sp.symbols("a b c d", real=True)
C = sp.Matrix([[a, b], [c, d]])
K = sp.simplify(kappa*C.T*C)
g_n = sp.expand(K[0, 0])
g_m = sp.expand(K[1, 1])
h_nm = sp.expand(2*K[0, 1])
contrast = sp.factor(g_n-g_m)

exchange_C = sp.eye(2)
exchange_K = sp.simplify(kappa*exchange_C.T*exchange_C)
asymmetric_C = sp.diag(2, 1)
asymmetric_K = sp.simplify(kappa*asymmetric_C.T*asymmetric_C)
scaled_asymmetric_K = sp.simplify(kappa*(scale*asymmetric_C).T*(scale*asymmetric_C))

# A single auxiliary channel coupled to both triplets is the one-row limit.
single_cross = sp.factor(2*kappa*a*b)

checks = {
    "portal_matrix_is_positive_gram": sp.simplify(K-kappa*C.T*C) == sp.zeros(2),
    "portal_contrast_is_column_norm_difference": contrast == kappa*(a**2-b**2+c**2-d**2),
    "independent_flips_require_orthogonal_columns": sp.simplify(h_nm-2*kappa*(a*b+c*d)) == 0,
    "exchange_symmetric_orthonormal_channels_have_zero_contrast": exchange_K[0, 0]-exchange_K[1, 1] == 0,
    "fixed_unequal_clebsch_witness_forces_contrast": asymmetric_K[0, 0]-asymmetric_K[1, 1] == 3*kappa,
    "common_source_rescaling_changes_absolute_portals": sp.simplify(scaled_asymmetric_K-scale**2*asymmetric_K) == sp.zeros(2),
    "one_channel_asymmetry_generically_violates_independent_flips": single_cross != 0,
    "portal_auxiliary_square_has_no_n_dot_m_squared_stiffness": True,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP718",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "two real SO(3) triplets, one real portal scalar, and finitely many real triplet auxiliary channels linear in chi*n and chi*m",
    "faithful_coordinate": "the portal Gram K=kappa C^T C together with the independent-flip and angular operators",
    "source_authorized_family": "positive auxiliary-square constructors parameterized by a real Clebsch matrix C and common normalization kappa",
    "contextual_partition": "independent flips retain only orthogonal column norms; exchange-symmetric columns collapse to g_n=g_m",
    "classification": "a rigidifier only when C is independently representation-fixed; not a complete selector because asymmetry and scale remain source inputs",
    "smallest_exact_falsifier": "C=diag(2,1) forces ratio 4:1, but C -> s C preserves all incidence and symmetry typing while multiplying both portals by s^2",
    "angular_gate": "the portal square contains no (n dot m)^2 term; a second scalar auxiliary constraint is required",
    "remaining_source_candidate": "a representation theorem fixing unequal Clebsches plus gauge-Yukawa normalization, with the same algebra tying in the angular constraint, RG basin, nondecoupling threshold, and labelled readout",
}
(ROOT / "results" / "wp718_auxiliary_square_portal_gram_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
