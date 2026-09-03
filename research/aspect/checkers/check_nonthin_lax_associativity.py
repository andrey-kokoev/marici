#!/usr/bin/env python3
"""Parallel-path equality for lax compositors in a nonthin one-object category."""

import json
from pathlib import Path

G = (0, 1, 2)
A = (0, 1)

def compose(left, right): return max(left, right)
def normalized(table): return all(table[0, g] == 0 and table[g, 0] == 0 for g in G)
def natural(component): return all(compose(arrow, component) == compose(component, arrow) for arrow in A)
def associativity_failures(table):
    failures = []
    for g in G:
        for h in G:
            for k in G:
                left = compose(table[g, h], table[(g + h) % 3, k])
                right = compose(table[h, k], table[g, (h + k) % 3])
                if left != right: failures.append((g, h, k, left, right))
    return tuple(failures)

def make_table(nonzero_pairs): return {(g, h): 1 if (g, h) in nonzero_pairs else 0 for g in G for h in G}

bad = make_table({(1, 1)})
good = make_table(set())
bad_failures = associativity_failures(bad)
good_failures = associativity_failures(good)
checks = {
    "endomorphism_monoid_has_parallel_arrows": len(A) == 2,
    "nonidentity_cell_is_noninvertible": all(compose(1, candidate) != 0 or compose(candidate, 1) != 0 for candidate in A),
    "bad_table_is_normalized": normalized(bad),
    "every_bad_component_exists": all(value in A for value in bad.values()),
    "every_bad_component_is_natural": all(natural(value) for value in bad.values()),
    "bad_table_contains_noninvertible_component": 1 in bad.values(),
    "bad_table_violates_associativity": len(bad_failures) > 0,
    "bad_table_has_four_explicit_failures": len(bad_failures) == 4,
    "good_table_is_normalized_and_natural": normalized(good) and all(natural(value) for value in good.values()),
    "good_table_satisfies_every_associativity_equation": len(good_failures) == 0,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.nonthin-lax-associativity.v1", "status": "passed", "checks": checks, "triple_count": 27, "bad_failure_count": len(bad_failures), "first_bad_failure": bad_failures[0], "claim_boundary": "One-object commutative idempotent endomorphism monoid with identity functors."}
output = Path(__file__).parents[1] / "results" / "nonthin_lax_associativity.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "bad_failures": len(bad_failures)}, sort_keys=True))
