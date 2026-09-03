#!/usr/bin/env python3
"""Full-category versus maximal-groupoid naturality in a finite attachment category."""

import json
from pathlib import Path

OBJECTS = (0, 1)
BITS = (0, 1)
G = (0, 1)
# Arrow: source, target, C2 label. There are no arrows 1 -> 0.
ARROWS = tuple((s, t, a) for s, t in ((0, 0), (1, 1), (0, 1)) for a in BITS)
CORE = tuple(arrow for arrow in ARROWS if arrow[0] == arrow[1])
NONINVERTIBLE = tuple(arrow for arrow in ARROWS if arrow[0] != arrow[1])


def table(component0, component1):
    c = {(g, h, obj): 0 for g in G for h in G for obj in OBJECTS}
    c[1, 1, 0] = component0
    c[1, 1, 1] = component1
    return c

def normalized(c): return all(c[0, g, x] == 0 and c[g, 0, x] == 0 for g in G for x in OBJECTS)
def local_cocycle(c, x): return all((c[g, h, x] + c[(g + h) % 2, k, x]) % 2 == (c[h, k, x] + c[g, (h + k) % 2, x]) % 2 for g in G for h in G for k in G)
def failures(c, arrows):
    result = []
    for g in G:
        for h in G:
            for source, target, label in arrows:
                if (label + c[g, h, source]) % 2 != (c[g, h, target] + label) % 2:
                    result.append((g, h, source, target, label))
    return tuple(result)

bad = table(0, 1)
good = table(1, 1)
bad_noninvertible = failures(bad, NONINVERTIBLE)
checks = {
    "fixture_has_four_core_arrows": len(CORE) == 4,
    "fixture_has_two_noninvertible_arrows": len(NONINVERTIBLE) == 2,
    "bad_table_is_normalized": normalized(bad),
    "bad_table_passes_both_local_cocycles": all(local_cocycle(bad, x) for x in OBJECTS),
    "bad_table_passes_maximal_groupoid_naturality": len(failures(bad, CORE)) == 0,
    "bad_table_fails_both_noninvertible_arrows": len(bad_noninvertible) == 2,
    "bad_table_fails_full_category_naturality": len(failures(bad, ARROWS)) == 2,
    "good_table_passes_local_cocycles": all(local_cocycle(good, x) for x in OBJECTS),
    "good_table_passes_full_category_naturality": len(failures(good, ARROWS)) == 0,
    "repair_preserves_local_validity": all(local_cocycle(bad, x) and local_cocycle(good, x) for x in OBJECTS),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.noninvertible-attachment-naturality.v1", "status": "passed", "checks": checks, "core_arrow_count": len(CORE), "noninvertible_arrow_count": len(NONINVERTIBLE), "bad_noninvertible_failure_count": len(bad_noninvertible), "claim_boundary": "Finite C2-labelled category with identity transport functors and invertible compositor components."}
output = Path(__file__).parents[1] / "results" / "noninvertible_attachment_naturality.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "noninvertible_failures": len(bad_noninvertible)}, sort_keys=True))
