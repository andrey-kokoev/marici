#!/usr/bin/env python3
"""Finite relational equipment and independent record-module diagnostics."""

import json
from pathlib import Path

X = (0, 1)
IDENTITY = frozenset((x, x) for x in X)
SWAP = frozenset({(0, 1), (1, 0)})
BRANCH = frozenset({(0, 0), (0, 1), (1, 1)})
RELATIONS = (IDENTITY, SWAP, BRANCH)

def compose(left, right):
    return frozenset((x, z) for x, y in right for y2, z in left if y == y2)
def deterministic(relation): return all(sum(1 for source, _ in relation if source == x) == 1 for x in X)
def image(predicate, relation): return frozenset(target for source, target in relation if source in predicate)
def module_closed(predicate, relation): return image(predicate, relation) <= predicate

associativity = all(compose(r, compose(q, p)) == compose(compose(r, q), p) for p in RELATIONS for q in RELATIONS for r in RELATIONS)
identity = all(compose(IDENTITY, relation) == relation == compose(relation, IDENTITY) for relation in RELATIONS)
good_record = frozenset(X)
bad_record = frozenset({0})
checks = {
    "relational_units_hold": identity,
    "relational_associativity_holds": associativity,
    "swap_is_deterministic_transport": deterministic(SWAP),
    "branch_is_nondeterministic_transport": not deterministic(BRANCH),
    "branch_still_composes_lawfully": compose(BRANCH, IDENTITY) == BRANCH,
    "good_record_is_transport_closed": all(module_closed(good_record, relation) for relation in RELATIONS),
    "bad_record_fails_swap_descent": not module_closed(bad_record, SWAP),
    "bad_record_does_not_change_equipment_units": identity,
    "bad_record_does_not_change_equipment_associativity": associativity,
    "record_module_is_independent_extra_gate": identity and associativity and module_closed(good_record, SWAP) and not module_closed(bad_record, SWAP),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.universal-equipment-record-module.v1", "status": "passed", "checks": checks, "relation_count": len(RELATIONS), "good_record": sorted(good_record), "bad_record": sorted(bad_record), "claim_boundary": "Boolean relational equipment on a two-element set; general profunctor/enriched universality remains residual."}
output = Path(__file__).parents[1] / "results" / "universal_equipment_record_module.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks)}, sort_keys=True))
