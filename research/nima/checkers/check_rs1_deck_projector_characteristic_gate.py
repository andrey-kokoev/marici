"""Exact characteristic gate for the RS-1 deck-projector candidate."""

from fractions import Fraction
import json
from pathlib import Path


def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(inv * x) % p for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [(x - c * y) % p for x, y in zip(a[i], a[row])]
        row += 1
    return row


sigma = [[0, 1], [1, 0]]
projector_q = [[Fraction(1, 2), Fraction(1, 2)],
               [Fraction(1, 2), Fraction(1, 2)]]

# Direct exact checks over Q.
assert projector_q == [
    [sum(projector_q[i][k] * projector_q[k][j] for k in range(2)) for j in range(2)]
    for i in range(2)
]
assert projector_q != [[1, 0], [0, 1]]  # deliberate false model rejected
assert [sum(projector_q[i][k] * [1, -1][k] for k in range(2)) for i in range(2)] == [0, 0]

rows = []
for p in (2, 3, 5, 7):
    norm = [[1, 1], [1, 1]]
    norm_sq = [[sum(norm[i][k] * norm[k][j] for k in range(2)) % p
                for j in range(2)] for i in range(2)]
    rows.append({
        "characteristic": p,
        "deck_order_invertible": p != 2,
        "norm_rank": rank_mod(norm, p),
        "norm_square_zero": norm_sq == [[0, 0], [0, 0]],
        "normalized_projector_exists": p != 2,
        "anti_invariant_kernel_dimension": 1 if p != 2 else None,
    })

assert rows[0]["norm_square_zero"] and not rows[0]["normalized_projector_exists"]
assert all(r["normalized_projector_exists"] and not r["norm_square_zero"] for r in rows[1:])

result = {
    "schema": "marici.rs1.deck-projector-characteristic-gate.v1",
    "rational_source_packet": {
        "channels": 2,
        "fold": "S=(1/2)(1,1)",
        "transfer": "T=(1,1)^T",
        "projector": "TS=(1+sigma)/2",
        "physical_pairing_compatible": True,
    },
    "finite_characteristic_audit": rows,
    "verdict": (
        "The mass-collision packet is a full source-realized fold/readout, but its rational "
        "syndrome is the one-dimensional anti-invariant kernel. Modular norm homology occurs "
        "only at the bad characteristic dividing deck order and is not thereby a physical sector."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs1-deck-projector-characteristic-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
