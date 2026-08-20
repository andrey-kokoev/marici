"""Classify geometric marked-hyperplane coincidences in the five-cycle packet."""
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUT = ROOT / "research/benincasa/results/five-site-qg-mark-coincidences.json"


def facets(n=5):
    out = {}
    for length in range(1, n):
        for start in range(n):
            sites = {(start + k) % n for k in range(length)}
            edge = [0] * n
            for e in range(n):
                if (e in sites) != ((e + 1) % n in sites):
                    edge[e] = 1
            out["g_" + "".join(str(i + 1) for i in sorted(sites))] = edge
    for e in range(n):
        edge = [0] * n
        edge[e] = 2
        out[f"G_minus_e{e + 1}{(e + 1) % n + 1}"] = edge
    return out


def primitive(v):
    g = math.gcd(*[abs(x) for x in v if x])
    v = tuple(x // g for x in v)
    first = next(x for x in v if x)
    return tuple(-x for x in v) if first < 0 else v


source = json.loads(SOURCE.read_text())["five_cycle"]
forms = facets()
common = [f"g_{i}" for i in range(1, 6)]
packets = []
profiles = Counter()
for index, additional in enumerate(source["terms"]):
    labels = common + additional
    groups = {}
    for label in labels:
        groups.setdefault(primitive(forms[label]), []).append(label)
    multiplicities = tuple(sorted((len(x) for x in groups.values()), reverse=True))
    profiles[(len(groups), multiplicities)] += 1
    packets.append({
        "term_index": index,
        "occurrence_marks": len(labels),
        "geometric_marks": len(groups),
        "multiplicity_profile": multiplicities,
        "groups": [{"normal": normal, "labels": sorted(group)}
                   for normal, group in sorted(groups.items())],
    })

profile_rows = [{"geometric_marks": key[0], "multiplicity_profile": key[1],
                 "term_count": count, "cyclic_orbits": count // 5}
                for key, count in sorted(profiles.items())]
assert all(row["term_count"] % 5 == 0 for row in profile_rows)
packet = {
    "schema": "marici.benincasa.five_site_qg_mark_coincidences.v1",
    "occurrence_marks_per_term": 9,
    "profile_census": profile_rows,
    "term_packets": packets,
    "typing": "Coincident complement labels retain separate occurrences over one geometric infinity hyperplane.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"profiles": profile_rows}))
