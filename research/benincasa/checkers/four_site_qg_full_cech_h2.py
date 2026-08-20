"""Compute deck-resolved H^2 after restoring fourfold concurrence cells."""
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAIRS = ROOT / "research/benincasa/results/four-site-qg-pair-curve-types.json"
MARKS = ROOT / "research/benincasa/results/four-site-qg-seven-mark-weight-page.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-full-cech-h2.json"


def rank(matrix):
    if not matrix or not matrix[0]:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
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
        r += 1
    return r


def matmul(a, b):
    if not a or not b:
        return []
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def nullspace(matrix, ncols):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivots = []
    r = 0
    for c in range(ncols):
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
    out = []
    for free in [c for c in range(ncols) if c not in pivots]:
        v = [Fraction(0)] * ncols
        v[free] = 1
        for i, p in enumerate(pivots):
            v[p] = -a[i][free]
        out.append(v)
    return out


def primitive(v):
    den = math.lcm(*(x.denominator for x in v))
    ints = [int(x * den) for x in v]
    g = math.gcd(*[abs(x) for x in ints if x])
    ints = [x // g for x in ints]
    first = next(x for x in ints if x)
    return [-x for x in ints] if first < 0 else ints


def quotient_representatives(d1, d2, nmiddle):
    image = [[Fraction(d1[i][j]) for i in range(nmiddle)]
             for j in range(len(d1[0]))] if d1 and d1[0] else []
    span = []
    for v in image:
        if rank(span + [v]) > rank(span):
            span.append(v)
    reps = []
    for v in nullspace(d2, nmiddle):
        if rank(span + [v]) > rank(span):
            span.append(v)
            reps.append(primitive(v))
    return reps


def boundary(high, low, high_rows, low_cols):
    """Signed simplicial coboundary from low subsets to high subsets."""
    out = [[0] * len(low_cols) for _ in high_rows]
    hp = {x: i for i, x in enumerate(high_rows)}
    lp = {x: i for i, x in enumerate(low_cols)}
    for target in high:
        for k in range(len(target)):
            face = target[:k] + target[k + 1:]
            sign = -1 if k % 2 else 1
            for sheet in ("+", "-", "diag", "ram"):
                source_key = (face, sheet)
                if source_key not in lp:
                    continue
                target_sheet = sheet
                if (target, target_sheet) not in hp:
                    if (target, "ram") in hp:
                        target_sheet = "ram"
                    elif (target, "diag") in hp:
                        target_sheet = "diag"
                    else:
                        continue
                out[hp[(target, target_sheet)]][lp[source_key]] += sign
    return out


pairs_packet = json.loads(PAIRS.read_text())
marks_packet = json.loads(MARKS.read_text())
packets = []
profiles = Counter()

for pp, mp in zip(pairs_packet["term_packets"], marks_packet["term_packets"]):
    assert pp["term_index"] == mp["term_index"]
    mark_keys = sorted({tuple(side) for p in pp["pairs"] for side in p["marks"]})
    mi = {key: i for i, key in enumerate(mark_keys)}
    normal_by_key = {tuple(m["labels"]): m["normal"] for m in mp["distinct_marks"]}
    rows = [normal_by_key[key] for key in mark_keys]
    pair_type = {}
    mark_hits = [set() for _ in mark_keys]
    for p in pp["pairs"]:
        i, j = sorted((mi[tuple(p["marks"][0])], mi[tuple(p["marks"][1])]))
        pair_type[(i, j)] = "split" if p["curve_type"].startswith("split") else "diag"
        hits = set(map(tuple, p["shared_nodes"]))
        mark_hits[i] |= hits
        mark_hits[j] |= hits

    pairs = list(itertools.combinations(range(len(mark_keys)), 2))
    triples = list(itertools.combinations(range(len(mark_keys)), 3))
    quads = [q for q in itertools.combinations(range(len(mark_keys)), 4)
             if rank([rows[i] for i in q]) <= 3]

    def common_hits(subset):
        if not all(mark_hits[i] for i in subset):
            return set()
        return set.intersection(*(mark_hits[i] for i in subset))

    # Plus eigenspace: every nonempty stratum contributes one connected H^0.
    p1 = [(e, "diag") for e in pairs]
    p2 = [(t, "diag") for t in triples]
    p3 = [(q, "diag") for q in quads]
    d1p = boundary(triples, pairs, p2, p1)
    d2p = boundary(quads, triples, p3, p2)

    # Minus eigenspace: split pairs and off-branch higher intersections only.
    m1 = [(e, "+") for e in pairs if pair_type[e] == "split"]
    m2 = [(t, "+") for t in triples if not common_hits(t)]
    m3 = [(q, "+") for q in quads if not common_hits(q)]
    d1m = boundary([x[0] for x in m2], [x[0] for x in m1], m2, m1)
    d2m = boundary([x[0] for x in m3], [x[0] for x in m2], m3, m2)

    assert all(x == 0 for row in matmul(d2p, d1p) for x in row)
    assert all(x == 0 for row in matmul(d2m, d1m) for x in row)
    r1p, r2p = rank(d1p), rank(d2p)
    r1m, r2m = rank(d1m), rank(d2m)
    h2p = len(p2) - r2p - r1p
    h2m = len(m2) - r2m - r1m
    assert h2p >= 0 and h2m >= 0
    profile = (len(mark_keys), len(quads), len(m3), h2p, h2m)
    profiles[profile] += 1
    odd_reps = quotient_representatives(d1m, d2m, len(m2))
    assert len(odd_reps) == h2m
    packets.append({
        "term_index": pp["term_index"],
        "geometric_marks": len(mark_keys),
        "fourfold_concurrences": len(quads),
        "deck_plus": {"C1": len(p1), "C2": len(p2), "C3": len(p3),
                      "rank_d1": r1p, "rank_d2": r2p, "H2": h2p},
        "deck_minus": {"C1": len(m1), "C2": len(m2), "C3": len(m3),
                       "rank_d1": r1m, "rank_d2": r2m, "H2": h2m,
                       "C1_basis": [[list(mark_keys[i]) for i in edge]
                                    for edge, _ in m1],
                       "C2_basis": [[list(mark_keys[i]) for i in triple]
                                    for triple, _ in m2],
                       "C3_basis": [[list(mark_keys[i]) for i in quad]
                                    for quad, _ in m3],
                       "d1": d1m,
                       "d2": d2m,
                       "representatives": [[
                           {"coefficient": coefficient,
                            "triple": [mark_keys[i] for i in m2[position][0]]}
                           for position, coefficient in enumerate(rep) if coefficient]
                           for rep in odd_reps]},
        "quadruples": [{"subset": q, "labels": [mark_keys[i] for i in q],
                         "branch_node_count": len(common_hits(q))} for q in quads],
    })

profile_rows = [{
    "geometric_marks": key[0], "fourfold_concurrences": key[1],
    "off_branch_fourfolds": key[2], "H2_plus": key[3], "H2_minus": key[4],
    "term_count": count,
} for key, count in sorted(profiles.items())]
packet = {
    "schema": "marici.benincasa.four_site_qg_full_cech_h2.v1",
    "profile_census": profile_rows,
    "global_H2": {
        "plus": sum(x["H2_plus"] * x["term_count"] for x in profile_rows),
        "minus": sum(x["H2_minus"] * x["term_count"] for x in profile_rows),
    },
    "checks": {"d2_d1_plus": "zero termwise", "d2_d1_minus": "zero termwise"},
    "term_packets": packets,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"profiles": profile_rows, "global_H2": packet["global_H2"]}))
