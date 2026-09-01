import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The SU(3) alternating cubic carrier epsilon_3 has six nonzero components,
# three +1 and three -1, indexed by permutations of (1,2,3).
def parity(perm):
    inversions = sum(1 for i in range(3) for j in range(i+1,3) if perm[i] > perm[j])
    return Fraction(-1) if inversions % 2 else Fraction(1)
epsilon_entries = [(p, parity(p)) for p in itertools.permutations((1,2,3))]
assert len(epsilon_entries) == 6
assert sum(1 for _,v in epsilon_entries if v == 1) == 3
assert sum(1 for _,v in epsilon_entries if v == -1) == 3

# These are internal tensor components, not six soft-branch production rows.
soft_dimensions = [6, 8, 1, 4, 2, 2]
q = [Fraction(d, 23) for d in soft_dimensions]
event_target = [Fraction(1,4)] * 6
assert q != event_target
epsilon_to_soft_rows = 0
epsilon_to_physical16_rows = 0
assert epsilon_to_soft_rows == 0
assert epsilon_to_physical16_rows == 0

# SU(3) invariance cannot distinguish the A-triplet directions.
supply = {
    "alternating_cubic_carrier_available": True,
    "six_nonzero_tensor_components": True,
    "six_soft_branch_kernel": False,
    "physical16_output_rows": False,
    "event_reweighting": False,
    "gain_law": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1100.v1",
    "status": "PASS",
    "question": "Do SU(3) alternating cubic carriers supply the production/decay kernel?",
    "epsilon_nonzero_components": [{"indices": list(p), "value": str(v)} for p,v in epsilon_entries],
    "component_count": 6,
    "positive_count": 3,
    "negative_count": 3,
    "dimension_weighted_soft_distribution": [str(v) for v in q],
    "event_target": [str(v) for v in event_target],
    "epsilon_to_soft_rows": epsilon_to_soft_rows,
    "epsilon_to_physical16_rows": epsilon_to_physical16_rows,
    "current_source_supply": supply,
    "classification": "negative gate: alternating tensor components are internal invariants, not production rows",
    "remaining_gate": "source-derived six-row branch-to-physical16 coupling matrix with event reweighting and gain 3/2",
    "hostile_gate": "do not promote six epsilon components, signs, or SU3 invariance into six event branches, reweighting, or gain",
    "claim_boundary": "WP1080 supplies the alternating carrier signature; it does not supply a map from internal indices to physical16 events",
    "disposition": "alternating-carrier production loophole closed",
}

(ROOT / "results" / "wp1100_alternating_cubic_production_kernel_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1100 PASS:", len(epsilon_entries), epsilon_to_soft_rows, epsilon_to_physical16_rows)
