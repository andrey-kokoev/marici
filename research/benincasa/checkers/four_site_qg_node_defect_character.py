"""Exact quadratic defect and C2^3-character audit for the eight C4 nodes."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-node-defect-character.json"


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


points = [(1,) + e for e in itertools.product((-1, 1), repeat=3)]
quadrics = [(i, j) for i in range(4) for j in range(i, 4)]
evaluation = [[p[i] * p[j] for i, j in quadrics] for p in points]
evaluation_rank = rank(evaluation)
assert evaluation_rank == 7

# Walsh characters chi_S(e)=product_{i in S} e_i on the regular C2^3 orbit.
characters = {}
for mask in range(8):
    values = [
        (e[0] if mask & 1 else 1)
        * (e[1] if mask & 2 else 1)
        * (e[2] if mask & 4 else 1)
        for _, *e in points
    ]
    # chi occurs in the quadratic evaluation image iff adjoining it does not raise rank.
    present = rank([row + [value] for row, value in zip(evaluation, values)]) == evaluation_rank
    characters[f"chi_{mask:03b}"] = {"values": values, "present_in_quadrics": present}

missing = [name for name, data in characters.items() if not data["present_in_quadrics"]]
assert missing == ["chi_111"]
relation = characters["chi_111"]["values"]
for col in zip(*evaluation):
    assert sum(c * x for c, x in zip(relation, col)) == 0

packet = {
    "schema": "marici.benincasa.four_site_qg_node_defect_character.v1",
    "points": points,
    "quadratic_monomials": [f"y{i+1}y{j+1}" for i, j in quadrics],
    "evaluation_rank": evaluation_rank,
    "node_count": 8,
    "defect": 1,
    "characters": characters,
    "missing_character": "chi_111 = epsilon2 epsilon3 epsilon4",
    "signed_relation_coefficients": relation,
    "independent_vanishing_cycle_rank": 7,
    "smooth_b3_benchmark": 20,
    "small_resolution_b2_expected": 2,
    "small_resolution_b3_expected": 6,
    "qualification": "Betti-number consequences use the standard conifold-transition sequence; physical activation is not inferred.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"rank": evaluation_rank, "defect": 1, "missing": missing, "vanishing_rank": 7}))
