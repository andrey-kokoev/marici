"""Exact WP614 single-spurion charge-gap hierarchy and coefficient fibers."""

import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

charges = (3, 2, 0)
exponents = sp.Matrix(
    3, 3, lambda row, column: abs(charges[row] - charges[column])
)
target_exponents = sp.Matrix([[0, 1, 3], [1, 0, 2], [3, 2, 0]])

epsilon, c12, c23, c13, delta = sp.symbols(
    "epsilon c12 c23 c13 delta", positive=True, real=True
)
s12 = c12 * epsilon
s23 = c23 * epsilon**2
s13 = c13 * epsilon**3
jarlskog = sp.simplify(
    s12
    * sp.sqrt(1 - s12**2)
    * s23
    * sp.sqrt(1 - s23**2)
    * s13
    * (1 - s13**2)
    * sp.sin(delta)
)
jarlskog_reduced = sp.simplify(jarlskog / epsilon**6)

# Exact same-charge hostile pair at epsilon=1/5 and unit coefficients.
hostile_common = {epsilon: sp.Rational(1, 5), c12: 1, c23: 1, c13: 1}
cp_even_j = sp.simplify(jarlskog.subs(hostile_common).subs(delta, 0))
cp_odd_j = sp.simplify(jarlskog.subs(hostile_common).subs(delta, sp.pi / 2))
amplitude_hostile_1 = s13.subs(hostile_common)
amplitude_hostile_2 = s13.subs(
    {epsilon: sp.Rational(1, 5), c13: 2}
)

# Central observed compatibility from flavor-nine-link-conventions.md.
vus, vub, vcb = 0.22517, 0.003763, 0.04189
vcd, vtd, vts = 0.22503, 0.00863, 0.04117
gamma = math.radians(66.4)
vud = math.sqrt(1 - vus**2 - vub**2)
j_central = vud * vub * vcd * vcb * math.sin(gamma)
observed_coefficients = {
    "c_us": vus / vus,
    "c_cd": vcd / vus,
    "c_cb": vcb / vus**2,
    "c_ts": vts / vus**2,
    "c_ub": vub / vus**3,
    "c_td": vtd / vus**3,
    "c_J": j_central / vus**6,
}

checks = {
    "charge_distances_give_wolfenstein_exponents": exponents
    == target_exponents,
    "long_gap_is_sum_of_adjacent_gaps": exponents[0, 2]
    == exponents[0, 1] + exponents[1, 2]
    == 3,
    "charge_assignment_is_recovered_up_to_shift_from_gaps": (
        charges[0] - charges[1], charges[1] - charges[2]
    )
    == (1, 2),
    "jarlskog_has_epsilon_six_factor": sp.simplify(
        jarlskog - epsilon**6 * jarlskog_reduced
    )
    == 0,
    "same_charges_allow_cp_conserving_point": cp_even_j == 0,
    "same_charges_allow_cp_violating_point": cp_odd_j > 0,
    "same_charges_allow_different_13_amplitudes": amplitude_hostile_1
    == sp.Rational(1, 125)
    and amplitude_hostile_2 == sp.Rational(2, 125),
    "central_magnitudes_have_order_one_coefficients": all(
        0.2 < value < 5 for value in observed_coefficients.values()
    ),
    "central_j_is_nonzero": j_central > 0,
    "one_two_three_link_depths_are_distinct": sorted(
        {exponents[0, 1], exponents[1, 2], exponents[0, 2]}
    )
    == [1, 2, 3],
}

if not all(checks.values()):
    raise SystemExit(f"WP614 check failed: {checks}")

result = {
    "work_package": "WP614",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "conditional_source_architecture": "one Froggatt-Nielsen-type spurion epsilon and ordered integer charges (3,2,0), realized by messenger paths whose lengths are charge gaps",
    "forced_exponent_matrix": [[int(value) for value in row] for row in exponents.tolist()],
    "forced_cp_scaling": "J=epsilon^6 times a continuous order-one coefficient and sin(delta), including exact unitarity cosine factors",
    "observed_order_one_coefficients": observed_coefficients,
    "contextual_partition": "charges fix the hierarchy-exponent lens, while continuous Wilson coefficients and delta leave non-singleton physical16 fibers",
    "classification": "conditional hierarchy selector and messenger-topology rigidifier; neither a numerical physical16 selector nor a CP selector",
    "smallest_exact_falsifier": "the same charges and epsilon admit delta=0 with J=0 and delta=pi/2 with J nonzero",
    "threshold_falsifier": "a resolved 1-to-3 flavor operator generated with fewer than three spurion insertions, or failure of the predicted one/two/three-stage messenger topology",
    "source_authority_gate": "derive the charge vector and one-spurion grammar independently, for example from anomaly or representation data; inferring (3,2,0) from CKM powers is target encoding",
    "instrument_gate": "resolve the flavon, vectorlike messenger stages, their charge-changing decays, and the same low-energy Wilson coefficients in one calibrated frame",
}

out = ROOT / "results" / "wp614_single_spurion_charge_gap_architecture.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
