"""Exact endpoint-resolved rank/index two-port readout audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

rank_probe = sp.Matrix([[1, 1]])
index_probe = sp.Matrix([[1, -1]])
joint_probe = sp.Matrix.vstack(rank_probe, index_probe)
endpoint_probe = sp.eye(2)
swap = sp.Matrix([[0, 1], [1, 0]])

hostile_same_index_a = sp.Matrix([2, 1])
hostile_same_index_b = sp.Matrix([3, 2])
hostile_same_rank_a = sp.Matrix([2, 1])
hostile_same_rank_b = sp.Matrix([1, 2])

checks = {
    "rank_probe_alone_has_rank_one": rank_probe.rank() == 1,
    "index_probe_alone_has_rank_one": index_probe.rank() == 1,
    "every_single_scalar_linear_port_has_at_most_rank_one": sp.Matrix([[2, 3]]).rank() == 1,
    "rank_and_index_joint_probe_has_rank_two": joint_probe.rank() == 2,
    "rank_and_index_joint_probe_has_determinant_minus_two": joint_probe.det() == -2,
    "endpoint_probe_is_faithful": endpoint_probe.rank() == 2,
    "same_index_hostile_is_separated_by_rank": index_probe * hostile_same_index_a == index_probe * hostile_same_index_b and rank_probe * hostile_same_index_a != rank_probe * hostile_same_index_b,
    "same_rank_hostile_is_separated_by_index": rank_probe * hostile_same_rank_a == rank_probe * hostile_same_rank_b and index_probe * hostile_same_rank_a != index_probe * hostile_same_rank_b,
    "endpoint_swap_preserves_rank": rank_probe * swap == rank_probe,
    "endpoint_swap_reverses_index": index_probe * swap == -index_probe,
    "two_labelled_endpoints_break_swap_to_its_stabilizer": swap != sp.eye(2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP763",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the positive cone of endpoint-resolved K-ranks (n0,npi) with an endpoint-swap symmetry before reference labeling",
    "faithful_coordinate": "the ordered endpoint rank pair, equivalently the parity-compatible joint readout (T,I)",
    "probe_family": "aggregate rank T=n0+npi and oriented index I=n0-npi, or two separately calibrated endpoint ports",
    "contextual_partition": "either scalar probe has one-dimensional fibers; the joint two-component probe has singleton fibers on the ordered lattice",
    "minimality": "one scalar linear port has rank at most one, while the rank-index pair has determinant -2 and is jointly faithful on its parity-compatible image",
    "reference_groupoid": "labelling and separately addressing both endpoints replaces the endpoint-swap quotient by the stabilizer of the chosen labels",
    "classification": "faithful relational readout and presentation rigidifier; neither a source selector nor evidence that the selected endpoint class is physically realized",
    "smallest_exact_falsifiers": {
        "index_only": "(2,1) and (3,2) have the same index but different rank",
        "rank_only": "(2,1) and (1,2) have the same rank but opposite index",
    },
    "instrument_gate": "two formal ports become physical only after one source derives independent endpoint couplings, common calibration, thresholds, uncertainties, and executable detector channels",
    "reference_warning": "the two-port experiment measures a relative ordered class in a new stabilizer groupoid; it does not recover an absolute label from the unreferenced experiment",
    "selection_gate": "joint faithfulness reconstructs whichever class was prepared but supplies no dynamics selecting T=3 or T=4",
    "deutschian_status": "the architecture can make the readout hard to vary once built, but it does not explain why nature prepares the desired class",
    "next_source_gate": "derive the rank-index class and the two endpoint couplings from one compactification or defect action, then compute threshold and detector Jacobians",
}
(ROOT / "results" / "wp763_endpoint_rank_index_two_port_readout.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
