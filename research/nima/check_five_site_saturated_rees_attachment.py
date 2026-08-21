"""Exact block audit of the deck-saturated total-energy Rees attachment."""

import itertools
import json
from fractions import Fraction as F
from pathlib import Path


# Five edge-soft two-sheet collapses. With q_+=T+2y and q_-=T-2y,
# the logarithmic normal difference at T=0 is -1/y.
edge_controls = [F(2), F(3), F(5), F(7), F(11)]
edge_coefficients = [-F(1, y) for y in edge_controls]
assert all(value != 0 for value in edge_coefficients)

# Ten complementary connected-subgraph collapses. For a boundary pair, the
# four sheet values are q_st=x+s*y+t*z. The projective complementary form is
# T-q_st, so its logarithmic normal coefficient at T=0 is -1/q_st.
connected_controls = [
    (F(101 + 2 * i), F(2 + i), F(3 + i))
    for i in range(10)
]
block_ranks = []
walsh_nonzero_counts = []
for x, y, z in connected_controls:
    sheet_values = []
    for s, t in itertools.product((-1, 1), repeat=2):
        q = x + s * y + t * z
        assert q != 0
        sheet_values.append(-F(1, q))
    # In the sheet basis the attachment is diagonal with four nonzero entries.
    block_ranks.append(sum(value != 0 for value in sheet_values))
    walsh = []
    signs = list(itertools.product((-1, 1), repeat=2))
    for mask in range(4):
        coefficient = F(0)
        for (s, t), value in zip(signs, sheet_values):
            character = (s if mask & 1 else 1) * (t if mask & 2 else 1)
            coefficient += character * value
        walsh.append(coefficient)
    assert all(value != 0 for value in walsh)
    walsh_nonzero_counts.append(4)

assert block_ranks == [4] * 10
generic_rank = len(edge_coefficients) + sum(block_ranks)
assert generic_rank == 45

result = {
    "schema": "marici.cosmology.five_site_saturated_rees_attachment.v1",
    "edge_blocks": 5,
    "edge_block_rank": 1,
    "connected_boundary_blocks": 10,
    "connected_block_rank": 4,
    "generic_total_rank": generic_rank,
    "generic_kernel_dimension": 0,
    "connected_block_walsh_support": walsh_nonzero_counts,
    "only_failure_support": "declared marked divisors q=0",
    "passed": True,
}
out = Path(__file__).with_name("results") / "five-site-saturated-rees-attachment.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
