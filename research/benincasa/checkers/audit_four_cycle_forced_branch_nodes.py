"""Correct infinity-quartic audit at the five forced C4 incidence points."""
import json
import math
import random
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-triple-points.json"
OUT = ROOT / "research/benincasa/results/four-cycle-forced-branch-nodes.json"


def rref_nullspace(rows, n=4):
    a = [[Fraction(x) for x in row] for row in rows]
    r, pivots = 0, []
    for c in range(n):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        x = [Fraction(0)] * n
        x[f] = 1
        for row, pivot in reversed(list(zip(a, pivots))):
            x[pivot] = -sum(row[c] * x[c] for c in range(pivot + 1, n))
        basis.append(x)
    return basis


def delta(z):
    return [z[1] - z[0], z[2] - z[1], z[3] - z[2]]


def bilinear(h, x, y):
    return sum(x[i] * h[i][j] * y[j] for i in range(3) for j in range(3))


def det3(h):
    return (
        h[0][0] * (h[1][1] * h[2][2] - h[1][2] * h[2][1])
        - h[0][1] * (h[1][0] * h[2][2] - h[1][2] * h[2][0])
        + h[0][2] * (h[1][0] * h[2][1] - h[1][1] * h[2][0])
    )


def symmetric_from_entries(e):
    a, b, c, d, f, g = e
    return [[a, d, f], [d, b, g], [f, g, c]]


def activation_coefficients(d):
    return [d[0] ** 2, d[1] ** 2, d[2] ** 2, 2*d[0]*d[1], 2*d[0]*d[2], 2*d[1]*d[2]]


def witness_h(d0, t1, t2, p, seed):
    rng = random.Random(seed)
    coeff = activation_coefficients(d0)
    solve = next((i for i, x in enumerate(coeff) if x), None)
    for _ in range(400):
        entries = [Fraction(rng.randint(-7, 7) or 1) for _ in range(6)]
        if solve is not None:
            entries[solve] = -sum(coeff[i] * entries[i] for i in range(6) if i != solve) / coeff[solve]
        h = symmetric_from_entries(entries)
        if det3(h) == 0:
            continue
        da = delta([2*p[i]*t1[i] for i in range(4)])
        db = delta([2*p[i]*t2[i] for i in range(4)])
        daa = delta([t1[i]*t1[i] for i in range(4)])
        dab = delta([2*t1[i]*t2[i] for i in range(4)])
        dbb = delta([t2[i]*t2[i] for i in range(4)])
        aa = -(bilinear(h, da, da) + 2*bilinear(h, d0, daa))
        ab = -(2*bilinear(h, da, db) + 2*bilinear(h, d0, dab))
        bb = -(bilinear(h, db, db) + 2*bilinear(h, d0, dbb))
        discriminant = 4*aa*bb - ab*ab
        if discriminant:
            return discriminant
    raise AssertionError("no nondegenerate quadratic witness found")


source = json.loads(SOURCE.read_text())
records = source["incidence_records"]
assert len(records) == 296

point_census = source["projective_y_point_census"]
alternating = (1, -1, 1, -1)
node_witnesses = 0
universal_branch_occurrences = 0

for index, record in enumerate(records):
    p = tuple(Fraction(x) for x in record["projective_y_point"])
    pivot = tuple(Fraction(x) for x in record["pivot_normal"])
    d0 = delta([x*x for x in p])
    if p == alternating:
        assert d0 == [0, 0, 0]
        universal_branch_occurrences += 1
    k = next(i for i, x in enumerate(p) if x)
    gauge = [0, 0, 0, 0]
    gauge[k] = 1
    tangent = rref_nullspace([pivot, gauge])
    assert len(tangent) == 2
    witness_h(d0, tangent[0], tangent[1], p, 1701 + index)
    node_witnesses += 1

assert universal_branch_occurrences == 144
assert node_witnesses == 296

# The degree-four infinity branch is only the quadratic-in-z part.
coordinate_support = {
    "(1, 0, 0, 0)": "adj(G)_11=0",
    "(0, 1, 0, 0)": "(1,-1,0) adj(G) (1,-1,0)^T=0",
    "(0, 0, 1, 0)": "(0,1,-1) adj(G) (0,1,-1)^T=0",
    "(0, 0, 0, 1)": "adj(G)_33=0",
    "(1, -1, 1, -1)": "identically zero because Delta=0",
}

# An A1 surface node w^2=uv has quotient cover C2/{+-1}.  Three marked base
# lines pull back to six distinct central lines generically.  Their complement
# has OS ranks (1,6,5); the deck involution swaps three pairs.
result = {
    "schema": "marici.benincasa.four_cycle_forced_branch_nodes.v1",
    "correct_infinity_branch": "4 B4=-Delta^T adj(G) Delta",
    "discarded_lower_degree_term": "4 det(G) z1 has edge degree two and does not survive infinity",
    "point_census": point_census,
    "branch_support": coordinate_support,
    "universally_singular_alternating_occurrences": universal_branch_occurrences,
    "generic_node_witnesses": node_witnesses,
    "generic_local_surface_type": "A1 double-cover node",
    "normalized_marked_arrangement": "six central lines in C2, paired by the deck involution",
    "local_orlik_solomon_ranks": [1, 6, 5],
    "deck_character_ranks": {"H1_invariant": 3, "H1_anti": 3, "H2_invariant": 2, "H2_anti": 3},
    "generic_coefficient_classification": "mixed Tate with quadratic deck/Kummer character",
    "deeper_support": "vanishing Hessian discriminant of the restricted quartic node",
    "new_carrier_datum": False,
    "supersedes": "Entry 1163 smooth-branch/order-six calculation",
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({
    "records": node_witnesses,
    "universal_alternating": universal_branch_occurrences,
    "local_ranks": result["local_orlik_solomon_ranks"],
}))
