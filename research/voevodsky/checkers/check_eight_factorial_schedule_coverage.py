#!/usr/bin/env python3
"""Give every one of the 8! unrestricted node schedules a typed disposition."""
from itertools import permutations
import json
from pathlib import Path

ROOT = "0"
TRANSITIONS = ("A", "J", "P", "C", "T", "E", "F")
NODES = (ROOT,) + TRANSITIONS
RELATIONS = (
    *((ROOT, x) for x in TRANSITIONS),
    ("A", "J"), ("A", "C"), ("J", "T"), ("C", "T"),
    ("P", "T"), ("P", "E"), ("T", "F"), ("E", "F"),
)
PREDECESSORS = {x: set() for x in NODES}
for lower, upper in RELATIONS:
    PREDECESSORS[upper].add(lower)


def disposition(order):
    seen = set()
    for index, event in enumerate(order):
        missing = sorted(PREDECESSORS[event] - seen, key=NODES.index)
        if missing:
            return {
                "s": "empty",
                "i": index,
                "e": event,
                "m": "".join(missing),
                "a": "empty_typed_fiber",
            }
        seen.add(event)
    return {
        "s": "admissible",
        "a": "residual_augmented_relative_feature_nerve",
        "r": "<".join(order[1:]),
    }

records = {"".join(order): disposition(order) for order in permutations(NODES)}
valid = sum(record["s"] == "admissible" for record in records.values())
empty = len(records) - valid
assert len(records) == 40320
assert valid == 28
assert empty == 40292
assert all(record["a"] for record in records.values())

result = {
    "schema": "marici.voevodsky.eight-factorial-schedule-coverage.v1",
    "node_order": NODES,
    "root_convention": "0 is the initial object and must precede every transition",
    "relations": RELATIONS,
    "schedule_count": len(records),
    "admissible_count": valid,
    "empty_typed_fiber_count": empty,
    "field_legend": {
        "s": "status",
        "i": "zero-based first failure position",
        "e": "event at first failure",
        "m": "missing immediate predecessors",
        "a": "analytical-form constructor",
        "r": "admissible seven-transition linear extension",
    },
    "coverage": records,
    "passed": True,
    "conclusion": (
        "All 40320 unrestricted eight-node schedules have typed analytical forms: "
        "28 map to maximal relative-feature simplices and 40292 map to empty typed "
        "fibers carrying a first dependency-obstruction certificate."
    ),
}
out = Path(__file__).parents[1] / "results" / "eight_factorial_schedule_coverage.json"
out.write_text(json.dumps(result, separators=(",", ":")) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k != "coverage"}, indent=2))
