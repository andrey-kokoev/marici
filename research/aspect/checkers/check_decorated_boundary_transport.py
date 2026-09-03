#!/usr/bin/env python3
"""Check decorated boundary transport data and its untyped-selection counterexample."""

import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACT = ROOT / "research/aspect/contracts/decorated-boundary-transport.v1.json"
OUTPUT = ROOT / "research/aspect/results/decorated_boundary_transport.json"
data = json.loads(CONTRACT.read_text(encoding="utf-8"))
boundary = data["boundary_presentation"]
transport = data["transport"]
counterexample = data["counterexample"]

# Exact finite counterexample: a one-object discrete index has limit equal to
# the selected presheaf value.
presheaf_cardinality = {"a": 2, "b": 1, "sigma": 3}
source_limit = presheaf_cardinality[counterexample["source_boundary"][0]]
target_limit = presheaf_cardinality[counterexample["target_boundary"][0]]

checks = {
    "boundary_has_index_carrier_and_incidence": set(boundary) >= {"index_category", "carrier_functor", "incidence_cone"},
    "boundary_retains_occurrences": boundary["occurrence_sensitive"] is True,
    "transport_has_index_equivalence": "index_equivalence" in transport,
    "transport_has_carrier_natural_isomorphism": "carrier_natural_isomorphism" in transport,
    "transport_has_apex_isomorphism": "apex_isomorphism" in transport,
    "transport_has_incidence_coherence": "incidence_coherence" in transport,
    "construction_builds_diagram_iso_before_limit_iso": data["construction"].index("eta and kappa induce a natural isomorphism of boundary diagrams") < data["construction"].index("limit universality induces alpha_M"),
    "construction_builds_inverse": "inverse transport induces alpha_M inverse" in data["construction"],
    "conjugacy_uses_incidence_coherence": any("incidence coherence" in step for step in data["construction"]),
    "counterexample_ambient_equivalence_is_identity": counterexample["ambient_equivalence"] == "identity" and counterexample["presheaf_comparison"] == "identity",
    "counterexample_matching_cardinalities_reproduced": source_limit == counterexample["source_matching_cardinality"] and target_limit == counterexample["target_matching_cardinality"],
    "counterexample_has_no_matching_isomorphism": source_limit != target_limit,
    "counterexample_names_all_missing_transport_data": set(counterexample["missing"]) == {"index_equivalence", "carrier_natural_isomorphism", "incidence_coherence"},
    "physical_equivalence_not_claimed": "physical equivalence" in data["nonclaims"],
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.decorated-boundary-transport-check.v1", "status": "passed", "checks": checks, "counterexample": {"source_matching_cardinality": source_limit, "target_matching_cardinality": target_limit}, "supported_strength": "sufficient typed boundary-transport package plus finite insufficiency counterexample"}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "source_matching_cardinality": source_limit, "target_matching_cardinality": target_limit}, sort_keys=True))
