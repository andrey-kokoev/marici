"""Test whether existing branch-node Kato rows can meet deck-odd Cech H2."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-full-cech-h2.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-node-kato-completion.json"


def rank(matrix):
    if not matrix or not matrix[0]:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
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


def matmul(a, b):
    if not a or not b:
        return []
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


source = json.loads(SOURCE.read_text())
packets = []
for term in source["term_packets"]:
    odd = term["deck_minus"]
    c2 = [tuple(tuple(g) for g in triple) for triple in odd["C2_basis"]]
    c2pos = {triple: i for i, triple in enumerate(c2)}
    d2 = [list(row) for row in odd["d2"]]
    kato_rows = []
    for quad in term["quadruples"]:
        if quad["branch_node_count"] == 0:
            continue
        labels = tuple(tuple(g) for g in quad["labels"])
        row = [0] * len(c2)
        for k in range(4):
            face = labels[:k] + labels[k + 1:]
            if face in c2pos:
                row[c2pos[face]] = -1 if k % 2 else 1
        if not any(row):
            continue
        kato_rows.append({"quadruple": quad["labels"], "row": row})
        d2.append(row)
    d1 = odd["d1"]
    composition = matmul(d2, d1)
    closed = all(x == 0 for row in composition for x in row)
    h2 = len(c2) - rank(d1) - rank(d2)
    packets.append({
        "term_index": term["term_index"],
        "ordinary_H2_minus": odd["H2"],
        "branch_kato_rows": kato_rows,
        "completed_rank_d2": rank(d2),
        "completed_H2_minus": h2,
        "d2_d1_zero": closed,
    })

assert all(x["d2_d1_zero"] for x in packets)
packet = {
    "schema": "marici.benincasa.four_site_qg_node_kato_nonincidence.v1",
    "term_count": len(packets),
    "ordinary_global_H2_minus": sum(x["ordinary_H2_minus"] for x in packets),
    "completed_global_H2_minus": sum(x["completed_H2_minus"] for x in packets),
    "all_compositions_zero": True,
    "typing": "A branch-fourfold A1 Kato row can enter this deck-odd H0 complex only through off-branch triple faces. In every source branch quadruple all four faces are ramified, so the typed row is zero.",
    "conclusion": "The existing node Kato complex does not meet the residual rank-eight deck-odd H2. Entry 1181's node acyclicity cannot be transported as authority into this different coefficient row.",
    "term_packets": packets,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"ordinary": packet["ordinary_global_H2_minus"],
                  "kato_completed": packet["completed_global_H2_minus"],
                  "all_d2d1_zero": True,
                  "residual_terms": [{"term": x["term_index"], "H2": x["completed_H2_minus"],
                                      "kato_rows": len(x["branch_kato_rows"])}
                                     for x in packets if x["completed_H2_minus"]]}))
