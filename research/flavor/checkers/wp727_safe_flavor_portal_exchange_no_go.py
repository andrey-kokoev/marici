"""Exact exchange obstruction for a universal asymptotically safe flavor portal."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
Rn, Rm, h2 = sp.symbols("R_n R_m h2", real=True)
delta, epsilon = sp.symbols("delta epsilon", real=True)

exchange = sp.Matrix([[0, 1], [1, 0]])
even = sp.Matrix([1, 1])
odd = sp.Matrix([1, -1])
P_even = (sp.eye(2) + exchange) / 2
P_odd = (sp.eye(2) - exchange) / 2

universal_potential = delta * h2 * (Rn + Rm)
universal_pair = sp.Matrix([
    sp.diff(universal_potential, h2, Rn),
    sp.diff(universal_potential, h2, Rm),
])
universal_contrast = sp.expand((odd.T * universal_pair)[0])

broken_potential = universal_potential + epsilon * h2 * (Rn - Rm)
broken_pair = sp.Matrix([
    sp.diff(broken_potential, h2, Rn),
    sp.diff(broken_potential, h2, Rm),
])
broken_contrast = sp.expand((odd.T * broken_pair)[0])

# A relevant critical-surface amplitude remains a free source coordinate.
c, theta, t, alpha_star, v_odd = sp.symbols(
    "c theta t alpha_star v_odd", real=True, nonzero=True
)
critical_coordinate = alpha_star + v_odd * c * t**theta

checks = {
    "exchange_is_an_involution": exchange**2 == sp.eye(2),
    "universal_source_image_is_exchange_even": sp.simplify(exchange * universal_pair - universal_pair) == sp.zeros(2, 1),
    "odd_projector_annihilates_universal_portal": sp.simplify(P_odd * universal_pair) == sp.zeros(2, 1),
    "universal_portal_has_zero_ordered_contrast": universal_contrast == 0,
    "even_and_odd_channels_are_orthogonal": (odd.T * even)[0] == 0,
    "hostile_exchange_breaking_creates_contrast": sp.simplify(broken_contrast - 2 * epsilon) == 0,
    "hostile_contrast_is_continuously_tunable": sp.diff(broken_contrast, epsilon) == 2,
    "free_critical_surface_amplitude_changes_readout": sp.simplify(sp.diff(critical_coordinate, c) - v_odd * t**theta) == 0,
    "one_unlabelled_sum_channel_kills_contrast": sp.Matrix([[1, 1]]) * odd == sp.zeros(1, 1),
    "two_labelled_channels_retain_contrast": sp.eye(2).rank() == 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP727",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the universal U(3)-flavor portal sector of arXiv:2008.08606v1, restricted only for the hostile test to two ordered real norm coordinates",
    "faithful_coordinate": "the ordered portal pair (g_n,g_m), with exchange-odd physical contrast g_n-g_m",
    "source_authorized_operation": "the single invariant Higgs portal delta (Hdagger H) Tr(Sdagger S) evolved by the completed gauge-Yukawa-quartic RG system",
    "contextual_partition": "the admitted universal source has image only in the exchange-even line; every exchange-odd contrast class is absent",
    "classification": "genuine RG source and symmetric portal carrier, but neither an asymmetric selector nor a physical16 presentation rigidifier",
    "smallest_exact_falsifier": "the odd projector sends the universal portal pair (delta,delta) to zero",
    "hostile_extension": "epsilon h^2(R_n-R_m) yields contrast 2 epsilon and therefore restores only an adjustable coordinate unless epsilon is uniquely irrelevant and nonzero",
    "rg_gate": "a fixed point predicts only irrelevant coordinates; the audited matching-scale BSM couplings are scanned inputs on a viable critical surface",
    "threshold_gate": "the study uses a common matching mass and step decoupling, not a complete finite contrast-preserving threshold map",
    "instrument_gate": "representation-dependent production and decay channels exist, but no calibrated rank-two map from the ordered Marici portal contrast to detector units is derived",
    "remaining_source_principle": "an anomaly-free theory whose non-isomorphic representations explicitly orient the portal channels, produce a unique nonzero fixed contrast, make fluctuations about it irrelevant, and independently fix the relevant clock deformation",
    "primary_source": "https://arxiv.org/abs/2008.08606",
}
(ROOT / "results" / "wp727_safe_flavor_portal_exchange_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
