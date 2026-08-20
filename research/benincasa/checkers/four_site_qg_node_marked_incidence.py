"""Incidence of the eight q_G infinity nodes with the 28 source OFPT marked packets."""
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-ofpt-packet.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-node-marked-incidence.json"


def facets(n=4):
    out = {}
    for length in range(1, n):
        for start in range(n):
            sites = {(start + k) % n for k in range(length)}
            q = [0] * (2 * n)
            for i in sites:
                q[i] = 1
            for e in range(n):
                if ((e in sites) != (((e + 1) % n) in sites)):
                    q[n + e] = 1
            out["g_" + "".join(str(i + 1) for i in sorted(sites))] = q
    for e in range(n):
        q = [1] * n + [0] * n
        q[n + e] = 2
        out[f"G_minus_e{e + 1}{(e + 1) % n + 1}"] = q
    out["G"] = [1] * n + [0] * n
    return out


packet = json.loads(SOURCE.read_text())
terms = packet["four_cycle"]["terms"]
common = [f"g_{i}" for i in range(1, 5)]
forms = facets()
points = [(1,) + e for e in itertools.product((-1, 1), repeat=3)]

records = []
profile = Counter()
label_node_hits = Counter()
for term_index, term in enumerate(terms):
    labels = common + term
    node_rows = []
    for point in points:
        vanishing = []
        for label in labels:
            edge = forms[label][4:]
            if sum(a * b for a, b in zip(edge, point)) == 0:
                vanishing.append(label)
                label_node_hits[label] += 1
        node_rows.append({"point": point, "vanishing_labels": vanishing, "depth": len(vanishing)})
    depths = tuple(sorted(row["depth"] for row in node_rows))
    profile[depths] += 1
    records.append({"term_index": term_index, "additional_labels": term, "nodes": node_rows})

positive = (1, 1, 1, 1)
assert all(next(row for row in rec["nodes"] if tuple(row["point"]) == positive)["depth"] == 0 for rec in records)
assert sum(1 for rec in records for row in rec["nodes"] if row["depth"] > 0) > 0

result = {
    "schema": "marici.benincasa.four_site_qg_node_marked_incidence.v1",
    "source_term_count": len(terms),
    "node_count": len(points),
    "marked_hyperplanes_per_term": 7,
    "positive_node": positive,
    "positive_node_marked_depths": [0] * len(terms),
    "positive_node_meets_marked_divisor": False,
    "term_depth_profiles": [{"depths": list(k), "term_count": v} for k, v in sorted(profile.items())],
    "label_node_hit_counts": dict(sorted(label_node_hits.items())),
    "records": records,
    "interpretation": "The physical positive node is disjoint from every source marked divisor at infinity; deck-translated nodes can lie on marked strata.",
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"terms": len(terms), "profiles": len(profile), "positive_depth": 0, "marked_node_occurrences": sum(1 for rec in records for row in rec["nodes"] if row["depth"] > 0)}))
