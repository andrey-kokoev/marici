import json
from fractions import Fraction
from pathlib import Path


def rank(matrix):
    work = [[Fraction(x) for x in row] for row in matrix]
    if not work:
        return 0
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            scale = work[r][col]
            work[r] = [
                x - scale * y for x, y in zip(work[r], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


q = [[Fraction(1), Fraction(0)]]
e2 = [Fraction(0), Fraction(1)]

downstream_families = [
    [[Fraction(1)]],
    [[Fraction(1)], [Fraction(2)], [Fraction(-3)]],
    [[Fraction(0)], [Fraction(5)]],
]

composites = []
for d in downstream_families:
    composite = [[row[0], Fraction(0)] for row in d]
    assert all(sum(a * b for a, b in zip(row, e2)) == 0 for row in composite)
    assert rank(composite) <= 1
    composites.append(composite)

spectator_rows = [
    [Fraction(7), Fraction(0)],
    [Fraction(-2), Fraction(0)],
    [Fraction(0), Fraction(0)],
]
spectator_extension = q + spectator_rows
assert rank(spectator_extension) == 1

source_reference = [Fraction(0), Fraction(1)]
joint = q + [source_reference]
assert rank(joint) == 2

result = {
    "schema": "marici.gauge-forgetting-downstream-no-go.v1",
    "state_dimension": 2,
    "quotient_rank": rank(q),
    "downstream_ranks": [rank(matrix) for matrix in composites],
    "spectator_extension_rank": rank(spectator_extension),
    "source_sensitive_extension_rank": rank(joint),
    "persistent_kernel_witness": [0, 1],
    "verdict": "postprocessing and spectator ports cannot repair a distinction erased by the source quotient",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "gauge-forgetting-downstream-no-go.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
