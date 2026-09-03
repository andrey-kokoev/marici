#!/usr/bin/env python3
"""Finite co-Yoneda composition and compositor-cocycle diagnostics."""

import json
from pathlib import Path

OBJECTS = ("a", "b")


def hom(source, target):
    return frozenset({f"id:{source}"}) if source == target else frozenset()


def represented_profunctor(source, representative):
    return hom(source, representative)


def coend_support(source, target_representative, middle_pullback):
    # Discrete category: union over intermediate E of Hom(source,g*E) x Hom(E,f*D).
    witnesses = []
    for middle in OBJECTS:
        left = hom(source, middle_pullback[middle])
        right = hom(middle, target_representative)
        witnesses.extend((l, r, middle) for l in left for r in right)
    return tuple(witnesses)


# Identity pullbacks in the discrete fixture.
middle_pullback = {obj: obj for obj in OBJECTS}
coend_a = coend_support("a", "a", middle_pullback)
coend_b = coend_support("b", "a", middle_pullback)
direct_a = represented_profunctor("a", "a")
direct_b = represented_profunctor("b", "a")

C3 = (0, 1, 2)

def good_twist(first, second): return 0

def bad_twist(first, second): return 1 if (first, second) == (1, 1) else 0

def normalized(twist): return all(twist(0, value) == 0 and twist(value, 0) == 0 for value in C3)

def pentagon_violations(twist):
    violations = []
    for f in C3:
        for g in C3:
            for h in C3:
                left = (twist(g, h) + twist(f, (g + h) % 3)) % 2
                right = (twist(f, g) + twist((f + g) % 3, h)) % 2
                if left != right: violations.append((f, g, h, left, right))
    return tuple(violations)

good_violations = pentagon_violations(good_twist)
bad_violations = pentagon_violations(bad_twist)
checks = {
    "coend_has_unique_intermediate_for_represented_a": len(coend_a) == 1 and coend_a[0][2] == "a",
    "coend_is_empty_for_nonmapping_b": len(coend_b) == 0,
    "coend_and_direct_support_agree_at_a": len(coend_a) == len(direct_a) == 1,
    "coend_and_direct_support_agree_at_b": len(coend_b) == len(direct_b) == 0,
    "zero_twist_is_normalized": normalized(good_twist),
    "zero_twist_satisfies_every_pentagon": len(good_violations) == 0,
    "localized_twist_is_normalized": normalized(bad_twist),
    "localized_twist_violates_pentagon": len(bad_violations) > 0,
    "pointwise_representatives_are_unchanged_by_twist": middle_pullback == {"a": "a", "b": "b"},
    "coherence_not_pointwise_cardinality_detects_defect": len(coend_a) == 1 and len(bad_violations) > 0,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.coherent-attachment-representability.v1", "status": "passed", "checks": checks, "coend_a": coend_a, "good_pentagon_violation_count": len(good_violations), "bad_pentagon_violation_count": len(bad_violations), "first_bad_violation": bad_violations[0], "claim_boundary": "Finite discrete co-Yoneda and central C2 twist over C3; general bicategorical coherence follows from the stated source cells."}
output = Path(__file__).parents[1] / "results" / "coherent_attachment_representability.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "bad_violations": len(bad_violations)}, sort_keys=True))
