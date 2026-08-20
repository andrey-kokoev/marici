"""Evaluate the four-site residual odd H2 classes on the infinity branch."""
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
COH = ROOT / "research/benincasa/results/four-site-qg-full-cech-h2.json"
MARKS = ROOT / "research/benincasa/results/four-site-qg-seven-mark-weight-page.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-residual-kummer-radicals.json"


def null_vector(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    pivots = []
    r = 0
    for c in range(4):
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
        pivots.append(c)
        r += 1
    assert r == 3
    free = next(c for c in range(4) if c not in pivots)
    v = [Fraction(0)] * 4
    v[free] = 1
    for i, p in enumerate(pivots):
        v[p] = -a[i][free]
    den = math.lcm(*(x.denominator for x in v))
    out = [int(x * den) for x in v]
    g = math.gcd(*[abs(x) for x in out if x])
    out = [x // g for x in out]
    first = next(x for x in out if x)
    return [-x for x in out] if first < 0 else out


def primitive(values):
    g = math.gcd(*[abs(x) for x in values if x])
    values = [x // g for x in values]
    first = next(x for x in values if x)
    return [-x for x in values] if first < 0 else values


coh = json.loads(COH.read_text())
marks = json.loads(MARKS.read_text())
marks_by_term = {x["term_index"]: x for x in marks["term_packets"]}
records = []
for term in coh["term_packets"]:
    if term["deck_minus"]["H2"] != 1:
        continue
    index = term["term_index"]
    rep = term["deck_minus"]["representatives"][0]
    assert len(rep) == 1 and rep[0]["coefficient"] == 1
    triple = [tuple(group) for group in rep[0]["triple"]]
    normal_by_group = {tuple(x["labels"]): x["normal"]
                       for x in marks_by_term[index]["distinct_marks"]}
    point = null_vector([normal_by_group[group] for group in triple])
    z = [x * x for x in point]
    delta = [z[1] - z[0], z[2] - z[1], z[3] - z[2]]
    # K_infinity is a unit times Delta^T adj(G) Delta.  Coordinates are
    # (A11,A22,A33,A12,A13,A23), with A=adj(G_ext).
    coefficients = primitive([
        delta[0] ** 2, delta[1] ** 2, delta[2] ** 2,
        2 * delta[0] * delta[1], 2 * delta[0] * delta[2],
        2 * delta[1] * delta[2],
    ])
    records.append({
        "term_index": index,
        "triple": [list(x) for x in triple],
        "projective_point": point,
        "delta": delta,
        "radicand_coefficients": coefficients,
    })

groups = {}
for record in records:
    groups.setdefault(tuple(record["radicand_coefficients"]), []).append(record["term_index"])
assert len(groups) == 4 and sorted(len(x) for x in groups.values()) == [2, 2, 2, 2]

packet = {
    "schema": "marici.benincasa.four_site_qg_residual_kummer_radicals.v1",
    "cofactor_coordinate_order": ["A11", "A22", "A33", "A12", "A13", "A23"],
    "branch_convention": "K_infinity is a source-fixed nonzero scalar times Delta^T adj(G_ext) Delta; scalar and overall signs do not change the Kummer character.",
    "records": records,
    "radicand_occurrence_groups": [
        {"coefficients": list(coefficients), "term_indices": indices}
        for coefficients, indices in sorted(groups.items())
    ],
    "connection": "On each occurrence line, nabla=d-(1/2)dlog(radicand).",
    "support_classification": "existing branch-incidence divisor at the frozen marked triple point",
    "new_carrier_datum": False,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"groups": packet["radicand_occurrence_groups"]}))
