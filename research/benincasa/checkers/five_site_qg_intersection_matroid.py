"""Exact geometric matroids and occurrence depths for five-site source terms."""
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-site-qg-mark-coincidences.json"
OUT = ROOT / "research/benincasa/results/five-site-qg-intersection-matroid.json"


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


source = json.loads(SOURCE.read_text())
packets = []
profiles = Counter()
for term in source["term_packets"]:
    groups = term["groups"]
    normals = [g["normal"] for g in groups]
    multiplicities = [len(g["labels"]) for g in groups]
    m = len(groups)
    circuits = []
    for size in range(3, m + 1):
        for subset in itertools.combinations(range(m), size):
            r = rank([normals[i] for i in subset])
            if r == size:
                continue
            if all(rank([normals[i] for i in subset if i != removed]) == size - 1
                   for removed in subset):
                circuits.append(subset)

    flats = {}
    for size in range(1, m + 1):
        for subset in itertools.combinations(range(m), size):
            r = rank([normals[i] for i in subset])
            if r > 4:
                continue  # empty projective intersection in P4
            closure = tuple(i for i in range(m)
                            if rank([normals[j] for j in subset] + [normals[i]]) == r)
            flats[closure] = r

    circuit_census = Counter(len(c) for c in circuits)
    flat_census = Counter((r, len(flat), sum(multiplicities[i] for i in flat))
                          for flat, r in flats.items())
    key = (m, tuple(sorted(circuit_census.items())), tuple(sorted(flat_census.items())))
    profiles[key] += 1
    packets.append({
        "term_index": term["term_index"],
        "geometric_marks": m,
        "circuits": [{"subset": c, "size": len(c),
                      "labels": [groups[i]["labels"] for i in c]} for c in circuits],
        "circuit_size_census": dict(sorted(circuit_census.items())),
        "proper_flats": [{"subset": flat, "rank": r,
                          "geometric_size": len(flat),
                          "occurrence_depth": sum(multiplicities[i] for i in flat),
                          "labels": [groups[i]["labels"] for i in flat]}
                         for flat, r in sorted(flats.items())],
        "flat_census": [{"rank": k[0], "geometric_size": k[1],
                         "occurrence_depth": k[2], "count": v}
                        for k, v in sorted(flat_census.items())],
    })

profile_rows = [{
    "geometric_marks": key[0],
    "circuit_size_census": [{"size": k, "count": v} for k, v in key[1]],
    "flat_census": [{"rank": k[0], "geometric_size": k[1],
                     "occurrence_depth": k[2], "count": v}
                    for k, v in key[2]],
    "term_count": count,
    "cyclic_orbits": count // 5,
} for key, count in sorted(profiles.items())]
assert all(row["term_count"] % 5 == 0 for row in profile_rows)
packet = {
    "schema": "marici.benincasa.five_site_qg_intersection_matroid.v1",
    "ambient_projective_space": "P4",
    "profile_count": len(profile_rows),
    "profile_census": profile_rows,
    "term_packets": packets,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"profile_count": len(profile_rows),
                  "profiles": [{"marks": x["geometric_marks"],
                                "circuits": x["circuit_size_census"],
                                "terms": x["term_count"]} for x in profile_rows]}))
