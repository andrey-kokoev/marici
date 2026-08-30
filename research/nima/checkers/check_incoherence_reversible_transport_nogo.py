"""Finite controls for the reversible-transport local-minimum no-go."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "incoherence_reversible_transport_nogo.json"


def monotone(assignments, arrows):
    return all(assignments[source] <= assignments[target] for source, target in arrows)


def census(size, value_count):
    # A bidirected cycle is a finite connected groupoid generating graph.
    arrows = []
    for index in range(size):
        neighbor = (index + 1) % size
        arrows.extend(((index, neighbor), (neighbor, index)))
    admitted = [
        values
        for values in itertools.product(range(value_count), repeat=size)
        if monotone(values, arrows)
    ]
    return {
        "objects": size,
        "value_count": value_count,
        "all_assignments": value_count**size,
        "monotone_assignments": len(admitted),
        "constant_assignments": sum(len(set(values)) == 1 for values in admitted),
        "all_monotone_assignments_are_constant": all(
            len(set(values)) == 1 for values in admitted
        ),
    }


def main():
    controls = [census(size, 3) for size in range(2, 8)]
    packet = {
        "schema": "marici.incoherence-reversible-transport-nogo.v1",
        "controls": controls,
        "theorem": (
            "a preorder-monotone obstruction record is equivalent at the endpoints "
            "of every invertible arrow and constant on every connected groupoid orbit"
        ),
        "consequence": (
            "experienced-world selection by local minima requires a source-directed "
            "noninvertible arrow class"
        ),
        "passed": all(item["all_monotone_assignments_are_constant"] for item in controls),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
