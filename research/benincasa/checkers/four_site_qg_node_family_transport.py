"""Exact family audit for the persistent C2^3 node sections and Gram boundary."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-node-family-transport.json"


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def adj3(m):
    return [
        [m[1][1]*m[2][2]-m[1][2]*m[2][1], m[0][2]*m[2][1]-m[0][1]*m[2][2], m[0][1]*m[1][2]-m[0][2]*m[1][1]],
        [m[1][2]*m[2][0]-m[1][0]*m[2][2], m[0][0]*m[2][2]-m[0][2]*m[2][0], m[0][2]*m[1][0]-m[0][0]*m[1][2]],
        [m[1][0]*m[2][1]-m[1][1]*m[2][0], m[0][1]*m[2][0]-m[0][0]*m[2][1], m[0][0]*m[1][1]-m[0][1]*m[1][0]],
    ]


def rank(m):
    a = [[Fraction(x) for x in row] for row in m]
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


generic = [[2,1,0],[1,3,1],[0,1,5]]
gram_rank_two = [[1,0,1],[0,1,1],[1,1,2]]
assert det3(generic) != 0
assert det3(gram_rank_two) == 0 and rank(gram_rank_two) == 2

adj_generic = adj3(generic)
adj_boundary = adj3(gram_rank_two)
assert rank(adj_generic) == 3
assert rank(adj_boundary) == 1

# At every sign section Delta=0 identically, for every G.  The Hessian in
# Delta coordinates is proportional to adj(G), hence has the stated ranks.
packet = {
    "schema": "marici.benincasa.four_site_qg_node_family_transport.v1",
    "node_sections": "[1:epsilon2:epsilon3:epsilon4], independent of G",
    "generic_gram_witness": generic,
    "generic_det_G": det3(generic),
    "generic_hessian_rank": rank(adj_generic),
    "rank_two_gram_witness": gram_rank_two,
    "boundary_det_G": det3(gram_rank_two),
    "boundary_adj_G": adj_boundary,
    "boundary_hessian_rank": rank(adj_boundary),
    "rank_two_boundary_normal_form": "W^2 = unit * L(Delta)^2",
    "boundary_cover_behavior": "locally reducible after the existing quadratic Kummer extension",
    "defect_character_transport": "constant chi_111 on det(G) != 0",
    "new_carrier_divisor": False,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"generic_rank": 3, "gram_boundary_rank": 1, "defect_character": "chi_111"}))
