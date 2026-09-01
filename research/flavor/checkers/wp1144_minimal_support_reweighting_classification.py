import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

def rank(A):
    rows = [list(row) for row in A]
    value = 0
    for col in range(6):
        pivot = next((i for i in range(value,6) if rows[i][col] != 0), None)
        if pivot is None:
            continue
        rows[value], rows[pivot] = rows[pivot], rows[value]
        pv = rows[value][col]
        rows[value] = [x / pv for x in rows[value]]
        for i in range(6):
            if i != value and rows[i][col] != 0:
                factor = rows[i][col]
                rows[i] = [rows[i][j] - factor * rows[value][j] for j in range(6)]
        value += 1
    return value

# Support one is impossible because no q_j equals u.
support_one = [j for j, value in enumerate(q) if value == u]
assert support_one == []
minimal_target_support = 2

assignments = 0
rank_histogram = {3: 0, 4: 0, 5: 0}
rank_three_example = None
for partners in product(range(6), repeat=6):
    if any(partners[j] == j for j in range(6)):
        continue
    assignments += 1
    rows = []
    valid = True
    for j,k in enumerate(partners):
        if q[j] == q[k]:
            valid = False
            break
        diagonal = (u - q[k]) / (q[j] - q[k])
        if diagonal < 0 or diagonal > 1:
            valid = False
            break
        row = [Fraction(0)] * 6
        row[j] = diagonal
        row[k] = 1 - diagonal
        rows.append(row)
    if not valid:
        continue
    matrix_rank = rank(rows)
    assert matrix_rank >= 3
    rank_histogram[matrix_rank] += 1
    if matrix_rank == 3 and rank_three_example is None:
        rank_three_example = (partners, rows)

assert assignments == 15625
assert sum(rank_histogram.values()) == 729
assert rank_histogram == {3: 6, 4: 162, 5: 561}
assert rank_three_example is not None
partners, rows = rank_three_example
assert rank(rows) == 3
assert all(sum(row) == 1 for row in rows)
assert all(sum(row[j] * q[j] for j in range(6)) == u for row in rows)

result = {
    "schema": "marici.flavor.wp1144.v1",
    "status": "PASS",
    "question": "What is the minimal support and rank of target-compatible local reweighting maps?",
    "dpc": {
        "conjecture": "A two-support local map can satisfy the target, and its rank may be as low as two.",
        "rivals": [
            "support-one diagonal map",
            "support-two rank-two map",
            "support-two rank-three map",
            "higher-rank local map"
        ],
        "risky_consequences": [
            "support one requires q_j=1/6",
            "support two requires exact interpolation",
            "rank is computed for every valid partner assignment",
            "nonnegative stochastic rows"
        ],
        "falsification_attempt": "No support-one row exists. Among 729 support-two maps, ranks are 3, 4, or 5; the minimum rank is 3.",
        "residual": "Six rank-three support-two candidates remain executable algebraic rivals.",
        "disposition": "classify minimal support two and minimal local rank three"
    },
    "support_one_solutions": 0,
    "minimal_target_support": minimal_target_support,
    "partner_assignments_tested": assignments,
    "target_compatible_support_two_maps": 729,
    "rank_histogram": {str(k): v for k,v in rank_histogram.items()},
    "minimal_support_two_rank": 3,
    "rank_three_example": {
        "zero_based_partners": list(partners),
        "rows": [[str(x) for x in row] for row in rows]
    },
    "classification": "classification gate: support two is sufficient for the target but forces rank at least three",
    "remaining_gate": "test the six rank-three support-two candidates against production locality and source provenance",
    "hostile_gate": "do not infer rank-two locality from support-two locality",
    "claim_boundary": "this is exact algebra over q and u, not physical production authority",
    "disposition": "minimal-support leaf resolved; rank-three candidates selected",
}

(ROOT / "results" / "wp1144_minimal_support_reweighting_classification.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1144 PASS:", minimal_target_support, 729, 3)
