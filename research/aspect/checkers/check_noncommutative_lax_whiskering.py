#!/usr/bin/env python3
"""Ordered versus unwhiskered compositor equations for C3 acting through inner S3 automorphisms."""

import itertools
import json
from pathlib import Path

S3 = tuple(itertools.permutations(range(3)))
ID = (0, 1, 2)
G = (0, 1, 2)

def mul(p, q): return tuple(p[q[i]] for i in range(3))
def inv(p): return tuple(p.index(i) for i in range(3))
def inner(a, x): return mul(mul(a, x), inv(a))
def maps_equal(left, right): return all(left(x) == right(x) for x in S3)

transposition = (1, 0, 2)
cycle = (1, 2, 0)
b = {0: ID, 1: transposition, 2: cycle}
alpha = {g: (lambda x, g=g: inner(b[g], x)) for g in G}
c = {(g, h): mul(mul(b[g], b[h]), inv(b[(g + h) % 3])) for g in G for h in G}

def compatibility_failures(table):
    failures = []
    for g in G:
        for h in G:
            if not maps_equal(lambda x, g=g, h=h: alpha[g](alpha[h](x)), lambda x, g=g, h=h: inner(table[g, h], alpha[(g + h) % 3](x))): failures.append((g, h))
    return tuple(failures)

def ordered_failures(table):
    failures = []
    for g in G:
        for h in G:
            for k in G:
                left = mul(table[g, h], table[(g + h) % 3, k])
                right = mul(alpha[g](table[h, k]), table[g, (h + k) % 3])
                if left != right: failures.append((g, h, k, left, right))
    return tuple(failures)

def unwhiskered_failures(table):
    failures = []
    for g in G:
        for h in G:
            for k in G:
                left = mul(table[g, h], table[(g + h) % 3, k])
                right = mul(table[h, k], table[g, (h + k) % 3])
                if left != right: failures.append((g, h, k))
    return tuple(failures)

mutated = dict(c)
mutated[1, 1] = ID if c[1, 1] != ID else transposition
ordered = ordered_failures(c)
unwhiskered = unwhiskered_failures(c)
mutated_ordered = ordered_failures(mutated)
checks = {
    "gauge_table_is_normalized": all(c[0, g] == ID and c[g, 0] == ID for g in G),
    "chosen_gauge_values_do_not_commute": mul(b[1], b[2]) != mul(b[2], b[1]),
    "action_is_nontrivial": any(alpha[g](x) != x for g in G for x in S3),
    "gauge_table_satisfies_action_compatibility": len(compatibility_failures(c)) == 0,
    "gauge_table_satisfies_all_ordered_triples": len(ordered) == 0,
    "unwhiskered_rival_fails": len(unwhiskered) > 0,
    "whiskering_changes_an_inner_component": any(alpha[g](c[h, k]) != c[h, k] for g in G for h in G for k in G),
    "mutation_preserves_component_membership": all(value in S3 for value in mutated.values()),
    "mutation_breaks_ordered_associativity": len(mutated_ordered) > 0,
    "triple_gate_is_distinct_from_component_existence": all(value in S3 for value in mutated.values()) and bool(mutated_ordered),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.noncommutative-lax-whiskering.v1", "status": "passed", "checks": checks, "ordered_failure_count": len(ordered), "unwhiskered_failure_count": len(unwhiskered), "mutated_ordered_failure_count": len(mutated_ordered), "claim_boundary": "One-object C3/S3 inner-action fixture with invertible comparison cells."}
output = Path(__file__).parents[1] / "results" / "noncommutative_lax_whiskering.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "unwhiskered_failures": len(unwhiskered), "mutated_failures": len(mutated_ordered)}, sort_keys=True))
