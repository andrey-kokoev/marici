import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

C = 23

# Suppose the 23 pole atoms are merely relabeled into WP1052's six event
# roles.  Let d be the integer number carrying detector provenance.  The
# WP1052 cell requires equal detector/monitor support and cross count d/2.
# Its total atom count would then be d+d-d/2=3d/2.
required_detector_count = Fraction(2 * C, 3)
assert required_detector_count == Fraction(46, 3)
assert required_detector_count.denominator != 1

# Equal event-atom weights are also impossible: 23 pole atoms cannot be
# partitioned into six equal-integer atom groups.
assert C % 6 == 5

# The tempting six-branch identification fails even before weighting.  Assign
# each localized SU(6) branch dimension to one WP1052 role and impose equal
# supports, half cross support, and half detected monitor support.
branch_dims = [6, 8, 1, 4, 2, 2]
roles = ["F_det", "F_null", "R_det", "R_null", "X_det", "X_null"]
solutions = []
for perm in set(itertools.permutations(branch_dims)):
    a = dict(zip(roles, perm))
    detector = a["F_det"] + a["F_null"] + a["X_det"] + a["X_null"]
    monitor = a["R_det"] + a["R_null"] + a["X_det"] + a["X_null"]
    cross = a["X_det"] + a["X_null"]
    monitor_detected = a["R_det"] + a["X_det"]
    if detector == monitor and 2 * cross == detector and 2 * monitor_detected == monitor:
        solutions.append(a)
assert solutions == []

result = {
    "schema": "marici.flavor.wp1065.v1",
    "status": "PASS",
    "question": "Can WP1052's physical16 event cell be obtained by relabeling WP1053/WP1056's 23 pole atoms?",
    "diophantine_obstruction": {
        "pole_atoms": C,
        "event_cell_constraints": "detector support = monitor support = d, cross support = d/2",
        "required_total": "d+d-d/2=3d/2",
        "required_detector_count": str(required_detector_count),
        "integer_solution": False,
    },
    "equal_weight_obstruction": {
        "event_atoms": 6,
        "C_mod_6": C % 6,
        "equal_integer_partition": False,
    },
    "branch_identification_hostile": {
        "localized_su6_branch_dimensions": branch_dims,
        "role_assignments_satisfying_WP1052_constraints": len(solutions),
    },
    "classification": "negative pole-event interface gate: the WP1052 event cell is not a relabeling or equal-weight partition of the 23 pole atoms or the six localized SU(6) branches",
    "remaining_gate": "derive channel-dependent event weights, detector/monitor/cross labels, and null outcomes from physical16 production/decay dynamics; do not identify atom counts across frames",
    "claim_boundary": "tests exact relabeling and equal-weight partitions; a future source-derived reweighting map is not excluded",
    "disposition": "productive: the physical16 source-dynamics blocker is sharpened to a required reweighting map rather than a six-atom identification",
}

(ROOT / "results" / "wp1065_pole_event_atom_interface_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1065 PASS:", required_detector_count, C % 6, len(solutions))
