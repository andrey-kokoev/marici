"""Exact domain-wall localization versus overlap-magnitude audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols("x", positive=True)  # x = M L

# Dimensionless normalized boundary densities L |f(0)|^2 for the two
# opposite kink-mass signs on an interval. The normalized zero modes are
# proportional to exp(-M y) and exp(+M y).
density_plus = sp.simplify(2 * x / (1 - sp.exp(-2 * x)))
density_minus = sp.simplify(2 * x / (sp.exp(2 * x) - 1))
ratio = sp.simplify(density_plus / density_minus)
contrast = sp.simplify(density_plus - density_minus)

# The domain-wall index is constant throughout x>0, whereas the overlap
# readout varies continuously. Two explicit members of the same index class
# provide the hostile pair.
x1 = sp.Rational(1, 2)
x2 = sp.Rational(3, 2)
contrast_1 = sp.simplify(contrast.subs(x, x1))
contrast_2 = sp.simplify(contrast.subs(x, x2))

checks = {
    "normalized_boundary_density_ratio_is_exponential": sp.simplify(ratio - sp.exp(2 * x)) == 0,
    "boundary_density_contrast_is_exactly_two_x": sp.simplify(contrast - 2 * x) == 0,
    "wall_orientation_reverses_the_labelled_contrast": sp.simplify((density_minus - density_plus) + contrast) == 0,
    "same_positive_index_class_contains_x_one_half": x1 > 0,
    "same_positive_index_class_contains_x_three_halves": x2 > 0,
    "hostile_pair_has_different_overlap_magnitudes": contrast_1 != contrast_2,
    "hostile_pair_exact_difference_is_two": sp.simplify(contrast_2 - contrast_1) == 2,
    "arbitrary_positive_contrast_has_a_positive_preimage": sp.solve(sp.Eq(contrast, sp.symbols("Delta", positive=True)), x)[0] == sp.symbols("Delta", positive=True) / 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP757",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one source-derived scalar kink and one anomaly-neutral vectorlike fermion pair on an interval, with dimensionless localization strength x=M L>0 and opposite kink-mass signs",
    "faithful_coordinate": "the labelled wall orientation and continuous localization strength x=M L, together with normalized zero-mode profiles",
    "source_authorized_operation": "the first-order domain-wall Dirac operator and normalizability of its chiral zero modes",
    "contextual_partition": "the topological zero-mode index identifies every x>0, while normalized boundary overlaps separate x continuously",
    "exact_readout": {
        "boundary_density_ratio": "exp(2*x)",
        "dimensionless_boundary_density_contrast": "2*x",
    },
    "classification": "conditional localization selector and presentation rigidifier, but not a numerical portal selector",
    "smallest_exact_falsifier": "x=1/2 and x=3/2 have the same domain-wall index and chirality but boundary-density contrasts 1 and 3",
    "sign_gate": "wall orientation and the assignment of kink-mass signs to the labelled n and m channels must be source-fixed; reversing the orientation reverses the labelled contrast",
    "magnitude_gate": "the index fixes only x>0; the Yukawa coupling, kink scale, interval length, and hence every positive contrast remain a continuous fiber",
    "rg_threshold_gate": "running of the Yukawa and wall parameters, finite wall width, KK thresholds, and radion stabilization are not protected by the index",
    "instrument_gate": "normalized profile overlap is a formal coupling until a threshold-resolved, detector-calibrated process measures the labelled contrast",
    "deutschian_status": "the kink explains why a chiral zero mode exists, but not why the required portal has its observed sign and magnitude; those can be varied without changing the topological explanation",
    "next_source_gate": "seek a quantized or fixed-point condition for x=M L and a source-fixed wall orientation that also survives RG and threshold matching",
}
(ROOT / "results" / "wp757_domain_wall_localization_magnitude_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
