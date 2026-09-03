#!/usr/bin/env python3
"""Typed endpoint checks for object-changing noncommutative lax whiskering."""

import itertools
import json
from pathlib import Path

S3 = tuple(itertools.permutations(range(3)))
OBJECTS = (0, 1)
ID = (0, 1, 2)
r = (1, 2, 0)

def mul(p, q): return tuple(p[q[i]] for i in range(3))
def inv(p): return tuple(p.index(i) for i in range(3))
def alpha(p): return mul(mul(r, p), inv(r))
def swap(x): return 1 - x

def arrow(source, target, label): return (source, target, label)
def compose(after, before):
    if before[1] != after[0]: return None
    return arrow(before[0], after[1], mul(after[2], before[2]))
def apply_swap(morphism): return arrow(swap(morphism[0]), swap(morphism[1]), alpha(morphism[2]))
def mu(x): return arrow(x, swap(x), r)

# Naturality: S(u) o mu_x = mu_y o u for every u:x->y.
naturality_failures = []
for x in OBJECTS:
    for y in OBJECTS:
        for p in S3:
            u = arrow(x, y, p)
            left = compose(apply_swap(u), mu(x))
            right = compose(mu(y), u)
            if left != right: naturality_failures.append((x, y, p))

path_records = []
for x in OBJECTS:
    left_whiskered = apply_swap(mu(x))       # S(mu_x): Sx -> x
    right_whiskered = mu(swap(x))            # mu_{Sx}: Sx -> x
    final = mu(x)                             # x -> Sx
    left_path = compose(final, left_whiskered)
    right_path = compose(final, right_whiskered)
    path_records.append((x, left_whiskered, right_whiskered, left_path, right_path))

# Same label as S(mu_x), but illegal copied endpoints x -> Sx.
fake_failures = []
label_only_matches = []
for x in OBJECTS:
    correct = apply_swap(mu(x))
    fake = arrow(x, swap(x), correct[2])
    typed = compose(mu(x), fake)
    fake_failures.append(typed is None)
    label_only_matches.append(mul(mu(x)[2], fake[2]) == mul(mu(x)[2], correct[2]))

checks = {
    "attachment_groupoid_has_24_arrows": len(OBJECTS) * len(OBJECTS) * len(S3) == 24,
    "swap_changes_every_object": all(swap(x) != x for x in OBJECTS),
    "label_action_is_nontrivial": any(alpha(p) != p for p in S3),
    "compositor_naturality_holds_for_all_arrows": len(naturality_failures) == 0,
    "left_and_right_whiskered_components_are_typed": all(record[1][:2] == record[2][:2] == (swap(record[0]), record[0]) for record in path_records),
    "both_associativity_paths_are_composable": all(record[3] is not None and record[4] is not None for record in path_records),
    "typed_associativity_paths_agree": all(record[3] == record[4] for record in path_records),
    "fake_whiskering_preserves_label_projection": all(label_only_matches),
    "fake_whiskering_breaks_typed_composition": all(fake_failures),
    "label_equality_is_not_typing_evidence": all(label_only_matches) and all(fake_failures),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.object-changing-noncommutative-laxity.v1", "status": "passed", "checks": checks, "naturality_arrow_count": 24, "typed_path_records": path_records, "claim_boundary": "Two-object S3-labelled groupoid with an inner-action swap functor and invertible cells."}
output = Path(__file__).parents[1] / "results" / "object_changing_noncommutative_laxity.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "naturality_failures": len(naturality_failures)}, sort_keys=True))
