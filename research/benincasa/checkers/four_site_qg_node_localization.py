"""Reduced localization map for seven marked nodes inside the rank-seven lattice."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-node-localization.json"


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x/q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x-q*y for x,y in zip(a[i],a[r])]
        r += 1
    return r


points = [(1,) + e for e in itertools.product((-1, 1), repeat=3)]
positive = points.index((1, 1, 1, 1))
supported = [i for i in range(8) if i != positive]
relation = [p[1] * p[2] * p[3] for p in points]

# Quotient Q^8/<relation> using the seven nonpositive coordinates as basis.
# relation has coefficient +1 at the positive node, so e_positive is the
# signed combination below and the supported map is the 7x7 identity.
assert relation[positive] == 1
positive_in_supported_basis = [-relation[i] for i in supported]
support_matrix = [[int(i == j) for j in range(7)] for i in range(7)]
support_rank = rank(support_matrix)
assert support_rank == 7

packet = {
    "schema": "marici.benincasa.four_site_qg_node_localization.v1",
    "ordered_points": points,
    "positive_index": positive,
    "supported_indices": supported,
    "global_relation": relation,
    "global_lattice_rank": 7,
    "supported_map_matrix_in_nonpositive_basis": support_matrix,
    "supported_image_rank": support_rank,
    "positive_class_in_supported_basis": positive_in_supported_basis,
    "ordinary_open_quotient_rank": 0,
    "reduced_mapping_cone_homology_rank": 0,
    "qualification": "This is the reduced node grade; higher incidence-depth Cech/Kato terms are retained as the next question.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"support_rank": support_rank, "global_rank": 7, "open_rank": 0, "cone_rank": 0}))
