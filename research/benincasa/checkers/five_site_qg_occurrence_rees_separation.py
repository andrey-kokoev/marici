"""First radial/Rees separation of coincident five-site complement labels."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-site-qg-occurrence-kernel.json"
OUT = ROOT / "research/benincasa/results/five-site-qg-occurrence-rees-separation.json"


def sites(label):
    assert label.startswith("g_")
    return frozenset(int(x) for x in re.findall(r"\d", label))


source = json.loads(SOURCE.read_text())
records = []
types = Counter()
for transition in source["transitions"]:
    # One source entry per occurrence generator; retain it once, not once per orbit.
    labels = transition["source_labels"]
    a, b = sites(labels[0]), sites(labels[1])
    assert a.isdisjoint(b) and a | b == frozenset(range(1, 6))
    if len(a) > len(b):
        a, b = b, a
        oriented_labels = [labels[1], labels[0]]
    else:
        oriented_labels = labels
    assert len(a) in (1, 2)
    coefficient = [2 if i in a else 0 for i in range(1, 6)]
    types[len(a)] += 1
    records.append({
        "term_index": transition["source_term"],
        "labels": oriented_labels,
        "partition_sizes": [len(a), len(b)],
        "common_infinity_normal": True,
        "grade_zero_difference": 0,
        "first_rees_difference_on_E0": coefficient,
        "formula": "2*rho*sum_(i in smaller part) X_i",
    })

assert len(records) == 240
assert sum(types.values()) == 240
packet = {
    "schema": "marici.benincasa.five_site_qg_occurrence_rees_separation.v1",
    "generator_count": len(records),
    "partition_type_census": [{"partition": [size, 5-size], "count": count,
                               "cyclic_orbits": count // 5}
                              for size, count in sorted(types.items())],
    "leading_action_on_infinity_coefficient": "trivial: identical geometric hyperplane and identical branch restriction",
    "first_rees_action": "nonzero generically: qhat_A-qhat_Ac=2*rho*X_A on total energy zero",
    "records": records,
}
assert all(row["count"] % 5 == 0 for row in packet["partition_type_census"])
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"types": packet["partition_type_census"]}))
