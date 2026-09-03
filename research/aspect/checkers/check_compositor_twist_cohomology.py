#!/usr/bin/env python3
"""Exhaustive normalized H^2 diagnostics for cyclic groups with trivial C2 coefficients."""

import itertools
import json
from pathlib import Path


def normalized_two_cochains(n):
    free_pairs = [(f, g) for f in range(1, n) for g in range(1, n)]
    for values in itertools.product((0, 1), repeat=len(free_pairs)):
        table = {(f, g): 0 for f in range(n) for g in range(n)}
        table.update(dict(zip(free_pairs, values)))
        yield tuple(table[(f, g)] for f in range(n) for g in range(n))


def value(cochain, n, f, g): return cochain[f * n + g]


def is_cocycle(cochain, n):
    return all((value(cochain, n, g, h) + value(cochain, n, f, (g + h) % n) - value(cochain, n, f, g) - value(cochain, n, (f + g) % n, h)) % 2 == 0 for f in range(n) for g in range(n) for h in range(n))


def normalized_coboundaries(n):
    results = set()
    for tail in itertools.product((0, 1), repeat=n - 1):
        b = (0,) + tail
        results.add(tuple((b[g] + b[f] - b[(f + g) % n]) % 2 for f in range(n) for g in range(n)))
    return results


def add(left, right): return tuple((a + b) % 2 for a, b in zip(left, right))


def classify(n):
    cocycles = set(c for c in normalized_two_cochains(n) if is_cocycle(c, n))
    coboundaries = normalized_coboundaries(n)
    unseen = set(cocycles)
    classes = []
    while unseen:
        representative = min(unseen)
        orbit = {add(representative, boundary) for boundary in coboundaries}
        assert orbit <= cocycles
        classes.append(orbit)
        unseen -= orbit
    return cocycles, coboundaries, classes


z2, b2, h2 = classify(2)
z3, b3, h3 = classify(3)
nontrivial_c2 = tuple(1 if (f, g) == (1, 1) else 0 for f in range(2) for g in range(2))
checks = {
    "c2_has_two_normalized_cocycles": len(z2) == 2,
    "c2_has_one_normalized_coboundary": len(b2) == 1,
    "h2_c2_c2_has_two_classes": len(h2) == 2,
    "nontrivial_c2_twist_is_coherent": nontrivial_c2 in z2,
    "nontrivial_c2_twist_is_not_coboundary": nontrivial_c2 not in b2,
    "c3_has_four_normalized_cocycles": len(z3) == 4,
    "c3_has_four_normalized_coboundaries": len(b3) == 4,
    "h2_c3_c2_is_trivial": len(h3) == 1,
    "all_c3_cocycles_are_gauge_removable": z3 == b3,
    "same_coefficients_different_composition_group_changes_obstruction": len(h2) != len(h3),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.compositor-twist-cohomology.v1", "status": "passed", "checks": checks, "C2_with_C2": {"cocycles": len(z2), "coboundaries": len(b2), "classes": len(h2)}, "C3_with_C2": {"cocycles": len(z3), "coboundaries": len(b3), "classes": len(h3)}, "claim_boundary": "Normalized finite cyclic groups with trivial central C2 coefficients."}
output = Path(__file__).parents[1] / "results" / "compositor_twist_cohomology.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "h2_c2": len(h2), "h2_c3": len(h3)}, sort_keys=True))
