import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

branch_dims = [6,8,1,4,2,2]
assert sum(branch_dims) == 23
row_orbits = [
    {"orbit": "six", "dimensions": [6]},
    {"orbit": "eight", "dimensions": [8]},
    {"orbit": "singlet", "dimensions": [1]},
    {"orbit": "remaining_quartet", "dimensions": [4]},
    {"orbit": "doublet_pair", "dimensions": [2,2]},
]
assert len(row_orbits) == 5
assert sum(len(o["dimensions"]) for o in row_orbits) == 6

kernel_shape = (6,6)
entry_count = kernel_shape[0] * kernel_shape[1]
assert entry_count == 36

# Gauge invariance would require branch x event products to contain a singlet,
# but WP1052's six event roles have no SU4 x SU2 x U1 representation
# assignment. Therefore no zero pattern can yet be evaluated.
event_representation_assignments = 0
evaluable_singlet_constraints = 0
known_coupling_entries = 0
assert event_representation_assignments == 0
assert evaluable_singlet_constraints == 0
assert known_coupling_entries == 0

# The unresolved localized-quartet choice swaps the two candidate kernels; no
# orientation source selects one.
quartet_choice_orbit_size = 2
quartet_choice_selected = False
assert quartet_choice_orbit_size == 2 and not quartet_choice_selected

result = {
    "schema": "marici.flavor.wp1117.v1",
    "status": "PASS",
    "question": "What representation constraints apply to the missing brane-to-physical16 coupling matrix?",
    "branch_dimensions": branch_dims,
    "row_orbits": row_orbits,
    "kernel_shape": list(kernel_shape),
    "entry_count": entry_count,
    "gauge_invariance_rule": "K_eb may be nonzero only when branch b tensor event e contains the source singlet",
    "event_representation_assignments": event_representation_assignments,
    "evaluable_singlet_constraints": evaluable_singlet_constraints,
    "known_coupling_entries": known_coupling_entries,
    "quartet_choice_orbit_size": quartet_choice_orbit_size,
    "quartet_choice_selected": quartet_choice_selected,
    "classification": "conditional gate: representation orbit fiber fixes row grouping but not matrix entries",
    "remaining_gate": "assign source representations to the six physical16 event roles, then impose singlet and gain constraints",
    "hostile_gate": "do not infer matrix zeros or values from dimensions, row orbits, or the unresolved quartet exchange",
    "claim_boundary": "row representation data are necessary constraints, not a coupling matrix",
    "disposition": "representation constraint fiber completed",
}

(ROOT / "results" / "wp1117_brane_coupling_representation_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1117 PASS:", branch_dims, len(row_orbits), entry_count, evaluable_singlet_constraints)
