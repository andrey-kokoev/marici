#!/usr/bin/env python3
"""Exhaustive naturality gate in a connected two-object C2-labelled groupoid."""

import json
from pathlib import Path

OBJECTS = (0, 1)
BITS = (0, 1)
G = (0, 1)
ARROWS = tuple((source, target, label) for source in OBJECTS for target in OBJECTS for label in BITS)


def local_cocycle(c, obj):
    return all((c[g, h, obj] + c[(g + h) % 2, k, obj]) % 2 == (c[h, k, obj] + c[g, (h + k) % 2, obj]) % 2 for g in G for h in G for k in G)


def normalized(c): return all(c[0, g, obj] == 0 and c[g, 0, obj] == 0 for g in G for obj in OBJECTS)

def naturality_failures(c):
    failures = []
    for g in G:
        for h in G:
            for source, target, label in ARROWS:
                left = (label + c[g, h, source]) % 2
                right = (c[g, h, target] + label) % 2
                if left != right: failures.append((g, h, source, target, label))
    return tuple(failures)

def isotropy_failures(c): return tuple(item for item in naturality_failures(c) if item[2] == item[3])
def interobject_failures(c): return tuple(item for item in naturality_failures(c) if item[2] != item[3])

def table(component0, component1):
    result = {(g, h, obj): 0 for g in G for h in G for obj in OBJECTS}
    result[1, 1, 0] = component0
    result[1, 1, 1] = component1
    return result

bad = table(0, 1)
good = table(1, 1)
bad_inter = interobject_failures(bad)
checks = {
    "bad_table_is_normalized": normalized(bad),
    "bad_table_passes_local_cocycle_at_0": local_cocycle(bad, 0),
    "bad_table_passes_local_cocycle_at_1": local_cocycle(bad, 1),
    "bad_table_passes_all_isotropy_naturality": len(isotropy_failures(bad)) == 0,
    "bad_table_fails_interobject_naturality": len(bad_inter) > 0,
    "bad_table_fails_all_four_interobject_arrows_for_pair_11": len(bad_inter) == 4,
    "good_table_is_normalized": normalized(good),
    "good_table_passes_both_local_cocycles": all(local_cocycle(good, obj) for obj in OBJECTS),
    "good_table_passes_full_naturality": len(naturality_failures(good)) == 0,
    "repair_changes_cross_object_relation_not_local_validity": local_cocycle(bad, 1) and local_cocycle(good, 1),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.connected-groupoid-compositor-naturality.v1", "status": "passed", "checks": checks, "arrow_count": len(ARROWS), "bad_interobject_failure_count": len(bad_inter), "claim_boundary": "Connected C2-labelled groupoid with identity functors and central isotropy."}
output = Path(__file__).parents[1] / "results" / "connected_groupoid_compositor_naturality.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "bad_interobject_failures": len(bad_inter)}, sort_keys=True))
