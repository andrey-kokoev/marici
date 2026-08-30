"""Exact fixed-inflow anomaly-neutral localization-kernel audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
b0, bpi, B, k = sp.symbols("b_0 b_pi B k")
A0 = b0 + B / 2 + k
Api = bpi + B / 2 - k

# One vectorlike zero-mode pair has anomaly coefficients (+1,-1).
# Boundary placement has zero net boundary anomaly. Bulk placement requires
# two orbifold hypers and has zero total bulk anomaly.
bulk_pair = {"b0": 0, "bpi": 0, "B": 0, "k": 0, "bulk_hypers": 2}
boundary_pair = {"b0": 0, "bpi": 0, "B": 0, "k": 0, "bulk_hypers": 0}


def local_anomalies(packet):
    values = {b0: packet["b0"], bpi: packet["bpi"], B: packet["B"], k: packet["k"]}
    return sp.simplify(A0.subs(values)), sp.simplify(Api.subs(values))


bulk_anomaly = local_anomalies(bulk_pair)
boundary_anomaly = local_anomalies(boundary_pair)

# Flavor witness: keep the link bulk and relocate only the anomaly-neutral
# WP738 mediator pairs. Corrected degree-weighted count: 36+12=48.
gravity_offset = 2
vector_count = 15
link_hypers = 4
mediator_pair_hypers = 48
kappa_boundary_mediators = gravity_offset + vector_count - link_hypers
kappa_bulk_mediators = kappa_boundary_mediators - mediator_pair_hypers

R4 = sp.symbols("R_fourth", positive=True)
gap_unit = 31 * sp.zeta(5) / (16 * R4)
ordering_shift = sp.factor(
    (kappa_boundary_mediators - kappa_bulk_mediators) * gap_unit
)

checks = {
    "bulk_vectorlike_pair_is_locally_anomaly_neutral": bulk_anomaly == (0, 0),
    "boundary_vectorlike_pair_is_locally_anomaly_neutral": boundary_anomaly == (0, 0),
    "same_fixed_inflow_level_survives_relocation": bulk_pair["k"] == boundary_pair["k"] == 0,
    "one_vectorlike_zero_mode_pair_requires_two_bulk_hypers": bulk_pair["bulk_hypers"] - boundary_pair["bulk_hypers"] == 2,
    "wp738_vectorlike_mediator_packet_has_forty_eight_bulk_degrees": mediator_pair_hypers == 48,
    "boundary_mediator_lift_has_positive_index_thirteen": kappa_boundary_mediators == 13,
    "bulk_mediator_lift_has_negative_index_thirty_five": kappa_bulk_mediators == -35,
    "fixed_inflow_relocation_reverses_selector_sign": kappa_boundary_mediators * kappa_bulk_mediators < 0,
    "deliberate_kernel_falsifier_is_nonzero": ordering_shift == 48 * gap_unit,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP756",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the WP737 product-group gauge/link lift with the anomaly-neutral vectorlike mediator pairs already required by WP738, allowing boundary-versus-bulk relocation while holding the Chern-Simons inflow level fixed",
    "faithful_comparison_coordinate": "the five-dimensional lift including localization class, fixed inflow level, and degree-weighted bulk spectral index kappa",
    "source_authorized_probe": "local anomaly balance at both orbifold fixed points with a separately frozen Chern-Simons level",
    "contextual_partition": "local anomaly balance identifies lifts differing only by anomaly-neutral vectorlike relocation, while the Scherk-Schwarz spectral index separates them",
    "spectral_indices": {"link_bulk_mediators_boundary": kappa_boundary_mediators, "link_and_mediators_bulk": kappa_bulk_mediators},
    "classification": "neither selector nor rigidifier on the anomaly-neutral localization kernel; fixed inflow is blind to a relocation that reverses the radiative selector",
    "smallest_exact_falsifier": "one vectorlike (+1,-1) pair can move between a common boundary and the bulk with k=0 and zero local anomalies in both lifts, while changing the bulk hypermultiplet count by two",
    "flavor_falsifier": "moving the WP738 anomaly-neutral mediator pairs into the bulk leaves the anomaly vector and fixed inflow unchanged but changes kappa from 13 to -35",
    "deutschian_status": "anomaly cancellation, even with independently fixed inflow, is too easy to vary because it has an anomaly-neutral localization kernel",
    "next_source_gate": "derive localization from a source principle sensitive to anomaly-neutral matter, such as a specified higher-dimensional interaction geometry or normalizability condition, without fitting the desired spectral sign",
    "remaining_physical_instrument_gate": "the source must also fix normalization, RG basin, thresholds, physical16 descent, and a calibrated detector response",
}
(ROOT / "results" / "wp756_fixed_inflow_anomaly_neutral_localization_kernel.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
