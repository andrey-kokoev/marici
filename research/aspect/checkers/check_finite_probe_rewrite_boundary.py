#!/usr/bin/env python3
"""Cross-check the positive witness and independent necessity countermodels."""

import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
RESULTS = ROOT / "research/aspect/results"
positive = json.loads((RESULTS / "finite_natural_isomorphism_fibers.json").read_text(encoding="utf-8"))
nonnatural = json.loads((RESULTS / "nonnatural_probe_rewrite_countermodel.json").read_text(encoding="utf-8"))
noninvertible = json.loads((RESULTS / "natural_noninvertible_probe_map.json").read_text(encoding="utf-8"))

checks = {
    "all_three_inputs_pass": all(item["status"] == "passed" for item in (positive, nonnatural, noninvertible)),
    "positive_has_naturality": positive["checks"]["all_naturality_squares_commute"],
    "positive_has_component_bijections": positive["checks"]["joint_component_is_bijective"] and positive["checks"]["singleton_components_are_bijective"],
    "positive_preserves_all_four_fibers": positive["checks"]["all_four_matching_data_checked"] and positive["checks"]["every_fiber_transport_is_bijective"],
    "positive_preserves_empty_fiber": positive["checks"]["empty_fiber_is_preserved"],
    "nonnatural_case_exhausts_objectwise_bijections": nonnatural["objectwise_bijection_family_count"] == 8 and nonnatural["natural_isomorphism_count"] == 0,
    "nonnatural_case_changes_fiber": nonnatural["checks"]["fiber_cardinality_is_not_preserved"],
    "noninvertible_case_is_natural": noninvertible["checks"]["all_naturality_squares_commute"],
    "noninvertible_case_changes_fiber": noninvertible["checks"]["joint_component_is_not_invertible"] and noninvertible["checks"]["induced_fiber_map_is_not_equivalence"],
    "necessity_failures_are_independent": nonnatural["checks"]["identity_maps_are_objectwise_bijections"] and noninvertible["checks"]["all_naturality_squares_commute"],
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.finite-probe-rewrite-boundary.v1", "status": "passed", "checks": checks, "supported_strength": "finite-local necessity and sufficiency witness", "unproved_generalization": "natural isomorphism induces matching-object isomorphism under transported proper-face diagrams", "claim_boundary": "Cross-result consistency only; not a general categorical proof."}
output = RESULTS / "finite_probe_rewrite_boundary.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "supported_strength": result["supported_strength"]}, sort_keys=True))
