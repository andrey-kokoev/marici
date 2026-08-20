"""Descent audit for the literal positive-node functional on the node quotient."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-physical-node-functional.json"

points = [(1,) + e for e in itertools.product((-1, 1), repeat=3)]
relation = [e2 * e3 * e4 for _, e2, e3, e4 in points]
positive_index = points.index((1, 1, 1, 1))
positive_functional = [int(i == positive_index) for i in range(8)]
orbit_sum_functional = [1] * 8

pair = lambda f, x: sum(a * b for a, b in zip(f, x))
positive_on_relation = pair(positive_functional, relation)
orbit_sum_on_relation = pair(orbit_sum_functional, relation)

assert positive_on_relation == 1
assert orbit_sum_on_relation == 0

packet = {
    "schema": "marici.benincasa.four_site_qg_physical_node_functional.v1",
    "ordered_points": points,
    "global_relation": relation,
    "positive_node_index": positive_index,
    "literal_positive_functional": positive_functional,
    "literal_positive_functional_on_relation": positive_on_relation,
    "literal_positive_functional_descends": False,
    "deck_orbit_sum_functional": orbit_sum_functional,
    "deck_orbit_sum_on_relation": orbit_sum_on_relation,
    "deck_orbit_sum_descends": True,
    "orbit_sum_source_authorized": False,
    "conclusion": "The global defect does not remove the positive-node hemisphere ambiguity.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"positive_on_relation": positive_on_relation, "orbit_sum_on_relation": orbit_sum_on_relation}))
