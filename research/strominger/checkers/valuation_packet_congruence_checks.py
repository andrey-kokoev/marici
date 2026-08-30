#!/usr/bin/env python3
"""Test whether the complete minor-valuation packet is a constructor congruence."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

packet = source["packet"]
LOWER, UPPER = -40, 40


def signature(exponent):
    record = packet(exponent)
    return (record["v3_d1"], record["v3_d2"], record["v3_d3"])


def defect(sig):
    return sig[2] - sig[1] - sig[0]


records = {
    n: {
        "packet": signature(n),
        "defect": defect(signature(n)),
        "successor_packet": signature(n + 1),
        "predecessor_packet": signature(n - 1),
    }
    for n in range(LOWER, UPPER + 1)
}

fibers = {}
for n, record in records.items():
    fibers.setdefault(record["packet"], []).append(n)

split_fibers = []
for sig, grades in fibers.items():
    if len(grades) < 2:
        continue
    successor_classes = {}
    predecessor_classes = {}
    for n in grades:
        successor_classes.setdefault(records[n]["successor_packet"], []).append(n)
        predecessor_classes.setdefault(records[n]["predecessor_packet"], []).append(n)
    if len(successor_classes) > 1 or len(predecessor_classes) > 1:
        witnesses = []
        for left, right in itertools.combinations(grades, 2):
            directions = []
            if records[left]["successor_packet"] != records[right]["successor_packet"]:
                directions.append("+1")
            if records[left]["predecessor_packet"] != records[right]["predecessor_packet"]:
                directions.append("-1")
            if directions:
                witnesses.append({
                    "left": left,
                    "right": right,
                    "same_packet": list(sig),
                    "directions_that_split": directions,
                    "left_successor": list(records[left]["successor_packet"]),
                    "right_successor": list(records[right]["successor_packet"]),
                    "left_predecessor": list(records[left]["predecessor_packet"]),
                    "right_predecessor": list(records[right]["predecessor_packet"]),
                })
        split_fibers.append({
            "packet": list(sig),
            "grades": grades,
            "successor_class_count": len(successor_classes),
            "predecessor_class_count": len(predecessor_classes),
            "witnesses": witnesses,
        })

all_witnesses = [
    witness
    for fiber in split_fibers
    for witness in fiber["witnesses"]
]
all_witnesses.sort(
    key=lambda w: (
        max(abs(w["left"]), abs(w["right"])),
        abs(w["left"] - w["right"]),
        w["left"],
        w["right"],
    )
)
smallest = all_witnesses[0] if all_witnesses else None

defect_fibers = {}
for n, record in records.items():
    defect_fibers.setdefault(record["defect"], []).append(n)
defect_not_faithful = any(
    len({records[n]["packet"] for n in grades}) > 1
    for grades in defect_fibers.values()
)

gates = {
    "bounded_range_contains_repeated_complete_packets":
        any(len(grades) > 1 for grades in fibers.values()),
    "complete_packet_congruence_is_falsified":
        bool(split_fibers),
    "a_smallest_split_witness_is_reported":
        smallest is not None,
    "both_authorized_generator_directions_are_tested":
        all("successor_packet" in r and "predecessor_packet" in r for r in records.values()),
    "scalar_defect_is_strictly_coarser_than_the_packet":
        defect_not_faithful,
}

payload = {
    "schema": "marici.strominger.valuation_packet_congruence_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": (
        "complete_valuation_packet_is_not_a_constructor_congruence"
        if split_fibers
        else "no_bounded_congruence_failure_found"
    ),
    "range": [LOWER, UPPER],
    "distinct_packet_count": len(fibers),
    "repeated_packet_fiber_count": sum(len(v) > 1 for v in fibers.values()),
    "split_fiber_count": len(split_fibers),
    "smallest_witness": smallest,
    "split_fiber_summaries": [
        {
            "packet": fiber["packet"],
            "grades": fiber["grades"],
            "successor_class_count": fiber["successor_class_count"],
            "predecessor_class_count": fiber["predecessor_class_count"],
        }
        for fiber in split_fibers[:8]
    ],
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "Equality of the full minor-valuation packet is not preserved by the "
        "authorized decoration generators in the tested range. A higher "
        "comparison cell must retain constructor-relative information beyond "
        "the local 2+1 packet."
        if split_fibers
        else
        "No higher cell is forced by the tested constructor congruence gate."
    ),
}
print(json.dumps(payload, indent=2))
