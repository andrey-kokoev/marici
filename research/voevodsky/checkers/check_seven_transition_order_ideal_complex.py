#!/usr/bin/env python3
"""Enumerate the order-ideal complex of the seven semilocal transitions."""

from itertools import combinations, permutations
import json
from pathlib import Path

ELEMENTS = ("A", "J", "P", "C", "T", "E", "F")
RELATIONS = (
    ("A", "J"),
    ("A", "C"),
    ("J", "T"),
    ("C", "T"),
    ("P", "T"),
    ("P", "E"),
    ("T", "F"),
    ("E", "F"),
)


def is_ideal(candidate: frozenset[str]) -> bool:
    return all(upper not in candidate or lower in candidate for lower, upper in RELATIONS)


def chain_counts(vertices: list[frozenset[str]]) -> list[int]:
    vertices = sorted(vertices, key=lambda item: (len(item), tuple(sorted(item))))
    ending: list[list[int]] = []
    for index, vertex in enumerate(vertices):
        counts = [0] * (len(vertices) + 1)
        counts[1] = 1
        for earlier, lower in enumerate(vertices[:index]):
            if lower < vertex:
                for length, number in enumerate(ending[earlier]):
                    if number:
                        counts[length + 1] += number
        ending.append(counts)
    totals = [sum(counts[length] for counts in ending) for length in range(1, len(vertices) + 1)]
    while totals and totals[-1] == 0:
        totals.pop()
    return totals


ideals = [
    frozenset(ELEMENTS[index] for index in range(len(ELEMENTS)) if mask & (1 << index))
    for mask in range(1 << len(ELEMENTS))
]
ideals = [ideal for ideal in ideals if is_ideal(ideal)]

linear_extensions = [
    order
    for order in permutations(ELEMENTS)
    if all(order.index(lower) < order.index(upper) for lower, upper in RELATIONS)
]

proper = [ideal for ideal in ideals if ideal and len(ideal) < len(ELEMENTS)]
full_counts = chain_counts(ideals)
proper_counts = chain_counts(proper)

result = {
    "claim": "The distributive lattice of order ideals has 18 states and 28 maximal chains; the proper-part order complex has f-vector (16,79,179,208,121,28).",
    "status": "proved_by_exhaustive_enumeration",
    "elements": ELEMENTS,
    "relations": RELATIONS,
    "order_ideals": [
        "".join(element for element in ELEMENTS if element in ideal)
        for ideal in sorted(ideals, key=lambda item: (len(item), tuple(sorted(item))))
    ],
    "order_ideal_count": len(ideals),
    "linear_extension_count": len(linear_extensions),
    "linear_extensions": ["<".join(order) for order in linear_extensions],
    "full_order_complex_f_vector": full_counts,
    "proper_part_order_complex_f_vector": proper_counts,
    "interpretation": {
        "full": "Includes empty and complete ideals; it is a doubly coned complex.",
        "proper": "Removes the initial and terminal ideals; maximal simplices correspond to the 28 admissible operation orders.",
    },
}

assert len(ideals) == 18
assert len(linear_extensions) == 28
assert full_counts == [18, 112, 353, 645, 716, 478, 177, 28]
assert proper_counts == [16, 79, 179, 208, 121, 28]

output = Path(__file__).parents[1] / "results" / "seven_transition_order_ideal_complex.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
