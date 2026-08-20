"""Regular-sequence audit for five-site first-Rees occurrence symbols."""
import json
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-site-qg-mark-coincidences.json"
OUT = ROOT / "research/benincasa/results/five-site-qg-occurrence-koszul.json"


def rank(rows):
    if not rows:
        return 0
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


def sites(label):
    return frozenset(int(x) for x in re.findall(r"\d", label))


source = json.loads(SOURCE.read_text())
packets = []
profiles = Counter()
total_energy = [1, 1, 1, 1, 1]
for term in source["term_packets"]:
    symbols = []
    types = []
    for group in term["groups"]:
        if len(group["labels"]) == 1:
            continue
        assert len(group["labels"]) == 2
        a, b = map(sites, group["labels"])
        assert a.isdisjoint(b) and a | b == frozenset(range(1, 6))
        if len(a) > len(b):
            a = b
        symbols.append([1 if i in a else 0 for i in range(1, 6)])
        types.append(f"{len(a)}|{5-len(a)}")
    k = len(symbols)
    assert k == 9 - term["geometric_marks"]
    quotient_rank = rank([total_energy] + symbols) - 1
    assert quotient_rank == k
    # Independent linear forms in the polynomial E_T=0 base are a regular sequence.
    dimensions = [1] if k == 0 else ([1, 1] if k == 1 else [1, 2, 1])
    profiles[(k, tuple(sorted(types)))] += 1
    packets.append({
        "term_index": term["term_index"],
        "symbol_count": k,
        "partition_types": sorted(types),
        "symbol_vectors_mod_scale": symbols,
        "rank_mod_total_energy": quotient_rank,
        "koszul_module_ranks": dimensions,
        "positive_koszul_homology": 0,
        "H0_support_codimension": k,
    })

profile_rows = [{"symbol_count": key[0], "partition_types": key[1],
                 "term_count": count, "cyclic_orbits": count // 5,
                 "support_codimension": key[0]}
                for key, count in sorted(profiles.items())]
assert all(row["term_count"] % 5 == 0 for row in profile_rows)
packet = {
    "schema": "marici.benincasa.five_site_qg_occurrence_koszul.v1",
    "base_ring": "Q[X1,...,X5]/(E_T)",
    "profile_census": profile_rows,
    "all_symbol_sequences_regular": True,
    "generic_positive_homology": 0,
    "support": "only the declared labelled site-soft or partial-site-soft linear loci",
    "term_packets": packets,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"profiles": profile_rows, "all_regular": True}))
