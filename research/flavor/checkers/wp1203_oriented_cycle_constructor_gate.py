import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(854)
wp854=json.loads((ROOT/"results"/"wp854_oriented_unitary_cycle_boundary_compression_constructor.json").read_text())
assert wp854["summary"]["all_passed"] is True
assert wp854["source_operation"] == "remove the directed return port e3->e0 from a lossless four-cycle"
assert wp854["derived_open_transport"] == "C=(I-P0)U=U(I-P3)"
assert wp854["relative_sign"] == "J=P0-P3; reversed cycle and port give -J"
assert wp854["classification"] == "conditional source-generated relational selector and normalizer"
singular=next(t for t in wp854["tests"] if t["name"]=="surviving_nonzero_singular_values_are_unit")["evidence"]
assert singular == "{1: 3, 0: 1}"
# Boundary compression derives WP852's partial-isometry data and an oriented
# boundary current, but the flavor cycle and its readout remain interfaces.
partial_isometry_derived=True
oriented_current_derived=True
unit_normalization_derived=True
flavor_cycle_realization=False
boundary_readout=False
threshold_intertwining=False
assert partial_isometry_derived and oriented_current_derived and unit_normalization_derived
assert not (flavor_cycle_realization or boundary_readout or threshold_intertwining)
result={
    "schema":"marici.flavor.wp1203.v1",
    "status":"PASS",
    "question":"Can an oriented cycle construct the path partial isometry?",
    "dpc":{
        "conjecture":"Removing a marked return port from a lossless cycle derives the required partial-isometry source relation.",
        "rivals":["declared path relation","oriented boundary compression","microscopic flavor cycle realization","calibrated boundary readout"],
        "risky_consequences":["C=(I-P0)U=U(I-P3)","J=P0-P3 reverses with the cycle and port","three surviving singular values are unit","the uncompressed cycle has no boundary current"],
        "falsification_attempt":"The constructor derives the normalization and orientation, but only after changing the groupoid to the stabilizer of marked source and sink.",
        "residual":"A microscopic flavor cycle, map from J to normalized contrast, threshold intertwiner, and calibrated physical16 readout remain required.",
        "disposition":"construct the oriented-cycle normalizer; reject completed physical realization"
    },
    "source_operation":wp854["source_operation"],
    "derived_open_transport":wp854["derived_open_transport"],
    "relative_sign":wp854["relative_sign"],
    "dimensionless_magnitude":wp854["dimensionless_magnitude"],
    "groupoid_change":wp854["groupoid_change"],
    "partial_isometry_derived":partial_isometry_derived,
    "oriented_current_derived":oriented_current_derived,
    "unit_normalization_derived":unit_normalization_derived,
    "flavor_cycle_realization":flavor_cycle_realization,
    "boundary_readout":boundary_readout,
    "threshold_intertwining":threshold_intertwining,
    "classification":"conditional relational constructor: boundary compression derives the partial isometry and oriented current",
    "remaining_gate":"realize the flavor cycle and construct a calibrated boundary-current readout",
    "hostile_gate":"do not treat marked-boundary compression as an existing flavor instrument",
    "claim_boundary":"the selector is conditional on the oriented cycle and marked source/sink; no flavor realization is claimed",
    "disposition":"oriented-cycle-constructor leaf resolved; boundary-current readout rival selected"
}
(ROOT/"results"/"wp1203_oriented_cycle_constructor_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1203 PASS: C=(I-P0)U and J=P0-P3")
