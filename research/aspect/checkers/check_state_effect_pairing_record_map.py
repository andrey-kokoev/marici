#!/usr/bin/env python3
"""Exact independence check for pairing descent and physical record descent."""

import json
from fractions import Fraction as Q
from pathlib import Path

rho = ((Q(1), Q(0)), (Q(0), Q(0)))
E = (((Q(1), Q(0)), (Q(0), Q(0))), ((Q(0), Q(0)), (Q(0), Q(1))))
sigma = {0: 1, 1: 0}

def tr_product(a, b):
    return sum(a[i][j] * b[j][i] for i in range(2) for j in range(2))

def swap_conjugate(a):
    return ((a[1][1], a[1][0]), (a[0][1], a[0][0]))

rho_t = swap_conjugate(rho)
E_t = tuple(swap_conjugate(e) for e in E)
p_source = {i: tr_product(rho, E[i]) for i in range(2)}
p_target = {sigma[i]: tr_product(rho_t, E_t[i]) for i in range(2)}
source_records = {0: "zero", 1: "one"}
good_target_records = {0: "one", 1: "zero"}
bad_target_records = {0: "zero", 1: "one"}
pairing_descends = all(p_target[sigma[i]] == p_source[i] for i in range(2))
good_descends = all(good_target_records[sigma[i]] == source_records[i] for i in range(2))
bad_descends = all(bad_target_records[sigma[i]] == source_records[i] for i in range(2))
checks = {
    "source_probabilities_normalized": sum(p_source.values()) == 1,
    "target_probabilities_normalized": sum(p_target.values()) == 1,
    "probabilities_nonnegative": all(v >= 0 for v in (*p_source.values(), *p_target.values())),
    "state_effect_pairing_descends": pairing_descends,
    "good_record_map_descends": good_descends,
    "bad_record_map_fails_descent": not bad_descends,
    "record_failure_has_witness_label_zero": bad_target_records[sigma[0]] != source_records[0],
    "pairing_data_identical_across_record_models": pairing_descends,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.state-effect-record-map.v1", "status": "passed", "checks": checks, "source_probabilities": {str(k): str(v) for k, v in p_source.items()}, "target_probabilities": {str(k): str(v) for k, v in p_target.items()}, "disposition": "pairing descent does not imply physical record descent"}
out = Path(__file__).parents[1] / "results" / "state_effect_pairing_record_map.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": "passed", "check_count": len(checks), "disposition": result["disposition"]}, sort_keys=True))
