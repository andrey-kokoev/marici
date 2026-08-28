#!/usr/bin/env python3
"""Exact Boolean deletion/Mobius profile of the five-mark rank-26 geometry."""
from __future__ import annotations

import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-boolean-deletion-mobius-profile.json"

marks = ("g1", "g2", "g3", "g23", "g31")
quartic_intersections = {"g1": 2, "g2": 2, "g3": 2, "g23": 4, "g31": 4}
parallel = {frozenset(("g1", "g23")), frozenset(("g2", "g31"))}


def subsets():
    for r in range(len(marks) + 1):
        yield from itertools.combinations(marks, r)


def rank_value(subset: tuple[str, ...]) -> int:
    # chi(A2 minus K)=9. Removing a marked affine line contributes n_K-1,
    # and every nonparallel line-line crossing contributes one.
    pairs = itertools.combinations(subset, 2)
    crossing_count = sum(frozenset(pair) not in parallel for pair in pairs)
    return 9 + sum(quartic_intersections[m] - 1 for m in subset) + crossing_count


rank_function = {frozenset(s): rank_value(s) for s in subsets()}
mobius = {}
for s in sorted(rank_function, key=lambda x: (len(x), sorted(x))):
    mobius[s] = rank_function[s] - sum(mobius[t] for t in mobius if t < s)

nonzero = [
    {"subset": sorted(s), "coefficient": value}
    for s, value in mobius.items()
    if value
]
checks = {
    "absolute_rank_is_nine": mobius[frozenset()] == 9,
    "singleton_total_is_nine": sum(v for s, v in mobius.items() if len(s) == 1) == 9,
    "crossing_pair_total_is_eight": sum(v for s, v in mobius.items() if len(s) == 2) == 8,
    "parallel_pairs_contribute_zero": all(mobius[p] == 0 for p in parallel),
    "all_triple_and_higher_coefficients_vanish": all(v == 0 for s, v in mobius.items() if len(s) >= 3),
    "full_rank_is_twenty_six": rank_function[frozenset(marks)] == 26,
    "mobius_sum_recovers_full_rank": sum(mobius.values()) == 26,
}

packet = {
    "schema": "marici.rank26-boolean-deletion-mobius-profile.v1",
    "marks": list(marks),
    "parallel_pairs": [sorted(p) for p in sorted(parallel, key=lambda x: sorted(x))],
    "quartic_intersection_counts": quartic_intersections,
    "full_rank": rank_function[frozenset(marks)],
    "mobius_grade_totals": {
        "absolute": 9,
        "single_mark": 9,
        "pair_crossing": 8,
        "triple_and_higher": 0,
    },
    "nonzero_mobius_coefficients": nonzero,
    "checks": checks,
    "passed": all(checks.values()),
    "scope": "This is the deletion-filtration Euler/Mobius profile. It does not assert a canonical splitting of the rank-26 coefficient object.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
