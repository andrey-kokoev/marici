"""Cyclic transport of the five-site occurrence-to-geometric kernel."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-site-qg-mark-coincidences.json"
OUT = ROOT / "research/benincasa/results/five-site-qg-occurrence-kernel.json"


def shift(label):
    if label.startswith("G_minus_e"):
        i, j = map(int, re.findall(r"\d", label))
        return f"G_minus_e{i % 5 + 1}{j % 5 + 1}"
    sites = sorted(int(x) % 5 + 1 for x in re.findall(r"\d", label))
    return "g_" + "".join(map(str, sites))


source = json.loads(SOURCE.read_text())
terms = {x["term_index"]: x for x in source["term_packets"]}
by_label_set = {
    frozenset(label for group in term["groups"] for label in group["labels"]): index
    for index, term in terms.items()
}
generators = {}
for index, term in terms.items():
    for group in term["groups"]:
        labels = tuple(sorted(group["labels"]))
        if len(labels) == 2:
            generators[(index, labels)] = {"term_index": index, "labels": labels,
                                            "generator": f"[{labels[0]}]-[{labels[1]}]"}
        else:
            assert len(labels) == 1

assert len(generators) == sum(9 - x["geometric_marks"] for x in terms.values()) == 240
transitions = []
for key, generator in sorted(generators.items()):
    index, labels = key
    target_labels_all = frozenset(shift(label) for group in terms[index]["groups"]
                                  for label in group["labels"])
    target_index = by_label_set[target_labels_all]
    mapped = tuple(shift(label) for label in labels)
    target_labels = tuple(sorted(mapped))
    target_key = (target_index, target_labels)
    assert target_key in generators
    sign = 1 if mapped == target_labels else -1
    transitions.append({"source_term": index, "source_labels": labels,
                        "target_term": target_index, "target_labels": target_labels,
                        "sign": sign})

by_source = {(x["source_term"], tuple(x["source_labels"])): x for x in transitions}
seen = set()
orbits = []
for start in sorted(generators):
    if start in seen:
        continue
    current = start
    orbit = []
    product = 1
    while current not in orbit:
        orbit.append(current)
        seen.add(current)
        step = by_source[current]
        product *= step["sign"]
        current = (step["target_term"], tuple(step["target_labels"]))
    assert current == start and len(orbit) == 5 and product == 1
    orbits.append({"generators": [{"term": x[0], "labels": x[1]} for x in orbit],
                   "cyclic_sign_product": product})

assert len(orbits) == 48
packet = {
    "schema": "marici.benincasa.five_site_qg_occurrence_kernel.v1",
    "exact_sequence": "0 -> K_occ -> Q^9 -> Q^m -> 0 termwise",
    "global_labelled_kernel_dimension": len(generators),
    "cyclic_orbit_count": len(orbits),
    "cyclic_module": "Q[C5]^48",
    "all_cyclic_sign_products": 1,
    "orbits": orbits,
    "transitions": transitions,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"kernel_dimension": len(generators), "orbits": len(orbits),
                  "module": packet["cyclic_module"]}))
