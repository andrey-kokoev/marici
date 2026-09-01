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

def matvec(A):
    return [sum(A[i][j] * q[j] for j in range(6)) for i in range(6)]

# Row-local support means at most the diagonal and one off-diagonal partner.
assignments = 0
target_compatible = 0
low_rank_local = 0
rank_histogram = {str(i): 0 for i in range(1,7)}
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
    assert matvec(rows) == [u] * 6
    target_compatible += 1
    r = rank(rows)
    rank_histogram[str(r)] += 1
    if r <= 2:
        low_rank_local += 1

assert assignments == 5**6
assert target_compatible > 0
assert low_rank_local == 0

# The WP1142 rank-two example uses full six-branch support in every row.
p_plus = [Fraction(5,24), Fraction(1,8), Fraction(5,36), Fraction(7,36), Fraction(1,6), Fraction(1,6)]
p_minus = [Fraction(1,8), Fraction(5,24), Fraction(7,36), Fraction(5,36), Fraction(1,6), Fraction(1,6)]
full_support_rank_two = [p_plus] + [p_minus] * 5
assert rank(full_support_rank_two) == 2
assert min(sum(x != 0 for x in row) for row in full_support_rank_two) == 6

result = {
    "schema": "marici.flavor.wp1143.v1",
    "status": "PASS",
    "question": "Can a rank-two reweighting candidate retain diagonal-plus-one-partner local support?",
    "dpc": {
        "conjecture": "A rank-two target-compatible map can retain row-local production support.",
        "rivals": [
            "rank-one full mixing",
            "rank-two full-support map",
            "diagonal-plus-one-partner local map",
            "higher-rank local map"
        ],
        "risky_consequences": [
            "each local row has support at most two",
            "exact interpolation to u=1/6",
            "rank at most two",
            "nonnegative stochastic entries"
        ],
        "falsification_attempt": "All 15625 off-diagonal partner assignments were tested exactly; target-compatible local maps exist, but none has rank at most two.",
        "residual": "Support three or more, or a sourced production adjacency packet, may still select a map.",
        "disposition": "reject row-local rank-two reweighting"
    },
    "local_assignments_tested": assignments,
    "target_compatible_local_maps": target_compatible,
    "low_rank_local_maps": low_rank_local,
    "rank_histogram": rank_histogram,
    "rank_two_example_min_row_support": 6,
    "classification": "negative gate: rank-two reweighting requires nonlocal full support in the tested local class",
    "remaining_gate": "determine the minimal support compatible with target and rank constraints",
    "hostile_gate": "do not call a rank-two full-support map localized",
    "claim_boundary": "this refutes diagonal-plus-one-partner rank-two candidates only",
    "disposition": "localized rank-two leaf resolved; minimal-support rival selected",
}

(ROOT / "results" / "wp1143_local_rank_two_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1143 PASS:", assignments, target_compatible, low_rank_local)
