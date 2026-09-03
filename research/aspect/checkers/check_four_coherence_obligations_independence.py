#!/usr/bin/env python3
"""Exact four-model independence certificate for coherence obligations."""

import json
from fractions import Fraction as Q
from pathlib import Path

models = {
    "forward_failure": {"F": (Q(2), Q(3), Q(5)), "B": (Q(2), Q(3), Q(6)), "K": (Q(1), Q(1)), "Q": (Q(0), Q(0))},
    "backward_failure": {"F": (Q(2), Q(3), Q(6)), "B": (Q(2), Q(3), Q(5)), "K": (Q(1), Q(1)), "Q": (Q(0), Q(0))},
    "compatibility_failure": {"F": (Q(2), Q(3), Q(6)), "B": (Q(2), Q(3), Q(6)), "K": (Q(1), Q(2)), "Q": (Q(0), Q(0))},
    "readout_failure": {"F": (Q(2), Q(3), Q(6)), "B": (Q(2), Q(3), Q(6)), "K": (Q(1), Q(1)), "Q": (Q(0), Q(1))},
}

def obligations(m):
    ff, fg, fcomp = m["F"]
    bf, bg, bcomp = m["B"]
    return (fcomp == fg * ff, bcomp == bf * bg, m["K"][0] == m["K"][1], m["Q"][0] == m["Q"][1])

vectors = {name: obligations(model) for name, model in models.items()}
expected = {
    "forward_failure": (False, True, True, True),
    "backward_failure": (True, False, True, True),
    "compatibility_failure": (True, True, False, True),
    "readout_failure": (True, True, True, False),
}
residuals = {
    name: (m["F"][2] - m["F"][1]*m["F"][0], m["B"][2] - m["B"][0]*m["B"][1], m["K"][0]-m["K"][1], m["Q"][0]-m["Q"][1])
    for name, m in models.items()
}
checks = {name + "_single_failure": vectors[name] == expected[name] for name in models}
checks.update({name + "_unique_nonzero_residual": sum(r != 0 for r in residuals[name]) == 1 for name in models})
checks["all_four_truth_vectors_distinct"] = len(set(vectors.values())) == 4
checks["each_obligation_has_countermodel_to_derivability"] = all(any(not v[i] and all(v[j] for j in range(4) if j != i) for v in vectors.values()) for i in range(4))
assert all(checks.values()), checks
result = {"schema": "marici.aspect.four-coherence-independence.v1", "status": "passed", "checks": checks, "truth_vectors": {k: list(v) for k,v in vectors.items()}, "residuals": {k: [str(x) for x in v] for k,v in residuals.items()}, "strength": "irredundant in declared finite scalar model class; not absolute axiomatic minimality"}
out = Path(__file__).parents[1] / "results" / "four_coherence_obligations_independence.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": "passed", "check_count": len(checks), "model_count": len(models)}, sort_keys=True))
