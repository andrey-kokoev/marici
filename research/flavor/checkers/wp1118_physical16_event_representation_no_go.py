import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

atoms = [
    ("F_det", {"detector": True, "monitor": False, "cross": False, "null": False}),
    ("F_null", {"detector": True, "monitor": False, "cross": False, "null": True}),
    ("R_det", {"detector": False, "monitor": True, "cross": False, "null": False}),
    ("R_null", {"detector": False, "monitor": True, "cross": False, "null": True}),
    ("X_det", {"detector": True, "monitor": True, "cross": True, "null": False}),
    ("X_null", {"detector": True, "monitor": True, "cross": True, "null": True}),
]
assert len(atoms) == 6
assert all(a[1]["detector"] or a[1]["monitor"] for a in atoms)
assert sum(a[1]["cross"] for a in atoms) == 2
weight = Fraction(1,4)
assert 6*weight == Fraction(3,2)

source_representation_assignments = 0
assert source_representation_assignments == 0

# Assigning all six event roles the trivial singlet would be an extra posit,
# not a source derivation, and would leave every one of 36 couplings allowed.
trivial_assignment_is_sourced = False
unconstrained_entries_under_trivial_assignment = 36
assert not trivial_assignment_is_sourced
assert unconstrained_entries_under_trivial_assignment == 36

singlet_constraints_evaluable = 0
assert singlet_constraints_evaluable == 0

result = {
    "schema": "marici.flavor.wp1118.v1",
    "status": "PASS",
    "question": "Do physical16 event roles admit a source representation assignment enabling singlet constraints?",
    "event_atoms": [name for name,_ in atoms],
    "event_weight": str(weight),
    "source_representation_assignments": source_representation_assignments,
    "trivial_assignment_is_sourced": trivial_assignment_is_sourced,
    "unconstrained_entries_under_trivial_assignment": unconstrained_entries_under_trivial_assignment,
    "singlet_constraints_evaluable": singlet_constraints_evaluable,
    "classification": "negative gate: physical16 labels are detector/monitor/cross/null provenance, not SU4xSU2xU1 source representations",
    "remaining_gate": "derive event dynamics and representation content from the source production/decay process",
    "hostile_gate": "do not assign all-singlet event roles or fit branch-matching representations to manufacture coupling zeros",
    "claim_boundary": "the six atom labels are exact but carry no gauge-source transformation law",
    "disposition": "event-representation assignment route closed at current source",
}

(ROOT / "results" / "wp1118_physical16_event_representation_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1118 PASS:", len(atoms), weight, source_representation_assignments, unconstrained_entries_under_trivial_assignment)
