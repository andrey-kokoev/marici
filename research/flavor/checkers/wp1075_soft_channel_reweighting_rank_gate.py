import json
from fractions import Fraction
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

branch_dims = [6, 8, 1, 4, 2, 2]
q = [Fraction(x, 23) for x in branch_dims]
r = [Fraction(1, 4) for _ in range(6)]
assert sum(q) == 1
assert sum(r) == Fraction(3, 2)

# Dimension-weighted identity propagation preserves q, not the WP1052 event weights.
assert q != r
assert sorted(q) != r

# No permutation/bijection can map q to the uniform six-role target r.
permutation_works = any([q[i] for i in perm] == r for perm in permutations(range(6)))
assert not permutation_works

# A common-gain diagonal channel would need branch-dependent gains, so it is
# not a diagonal common-gain law.
required_diagonal_gains = [r[i] / q[i] for i in range(6)]
assert required_diagonal_gains == [
    Fraction(23, 24),
    Fraction(23, 32),
    Fraction(23, 4),
    Fraction(23, 16),
    Fraction(23, 8),
    Fraction(23, 8),
]
assert len(set(required_diagonal_gains)) == 5

# Complete uniform mixing U=(1/6)J maps any normalized source distribution to
# 1/6 on each role.  A common gain g=3/2 then gives WP1052's six weights 1/4.
uniform = [Fraction(1, 6) for _ in q]
mixed = [sum(Fraction(1, 6) * qj for qj in q) for _ in range(6)]
assert mixed == uniform
gain = Fraction(3, 2)
assert [gain * x for x in mixed] == r

# The same uniform map also erases a hostile source concentrated on one
# branch, so its existence cannot be inferred from the target rows alone.
hostile_q = [1, 0, 0, 0, 0, 0]
hostile_mixed = [sum(Fraction(1, 6) * qj for qj in hostile_q) for _ in range(6)]
assert hostile_mixed == uniform

result = {
    "schema": "marici.flavor.wp1075.v1",
    "status": "PASS",
    "question": "What reweighting structure is required to map the six soft branch weights to WP1052's six event-role weights?",
    "source_branch_distribution": [str(x) for x in q],
    "target_event_role_weights": [str(x) for x in r],
    "negative_results": {
        "identity_preserves_dimension_weights": True,
        "permutation_maps_to_target": permutation_works,
        "common_gain_diagonal_exists": False,
        "required_diagonal_gains": [str(x) for x in required_diagonal_gains],
    },
    "minimal_rank_one_solution": {
        "mixing_matrix": "U=(1/6)J_6",
        "mixed_weights": [str(x) for x in mixed],
        "common_gain": str(gain),
        "output": [str(x) for x in [gain * x for x in mixed]],
        "rank": 1,
    },
    "target_fitting_hostile": "U also maps a source concentrated on one branch to the same uniform event weights, so U cannot be inferred from WP1052 rows alone",
    "classification": "soft-channel reweighting rank gate: dimension identity, bijection, and common-gain diagonal maps fail; a rank-one complete-mixing matrix with gain 3/2 can reproduce the event weights but requires source dynamics",
    "remaining_gate": "derive the production/decay coupling matrix, its mixing rank, and the gain 3/2 from the localized source rather than from the target event cell",
    "claim_boundary": "linear exact-weight analysis only; it does not assert that complete mixing is physical",
    "disposition": "productive: C1 now has an exact matrix law and hostiles rather than an unspecified coupling map",
}

(ROOT / "results" / "wp1075_soft_channel_reweighting_rank_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1075 PASS:", required_diagonal_gains, gain)
