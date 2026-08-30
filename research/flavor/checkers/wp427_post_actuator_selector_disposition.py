"""Exact reconciliation of the current physical16 selector disposition."""

import json
from pathlib import Path


root = Path(__file__).parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp71 = load("wp71_declared_source_selector_no_go.json")
wp82 = load("wp82_constructor_hostile_ensemble_matrix.json")
wp139 = load("wp139_boundary_instrument_candidate_closeout.json")
wp426 = load("wp426_law_state_intervention_boundary.json")

g71 = wp71["gates"]
rows82 = wp82["rows"]
matrix139 = wp139["candidate_matrix"]

checks = {
    "wp71_exact_dependencies_pass": all(g71.values()),
    "rg_descends_but_has_no_proper_image": g71["derived_rg_operation_has_no_local_proper_image"],
    "instrumented_physical16_algebra_is_nonselective": g71["instrumented_probe_algebra_is_nonselective"],
    "stationarity_fails_complete_frozen_ensemble": g71["stationarity_fails_complete_ensemble"],
    "wp82_no_hostile_candidate_passes_all_gates": all(not row["passes_all"] for row in rows82),
    "wp139_all_precursors_pass": wp139["checks"]["all_precursor_checkers_pass"],
    "wp139_no_boundary_candidate_passes_all_gates": all(not all(row.values()) for row in matrix139.values()),
    "wp139_has_no_executable_instrument": not wp139["physical_instrument_established"],
    "wp426_closes_direct_SM_quartic_actuation": wp426["passed"] and wp426["programme_disposition"].startswith("close direct SM quartic actuation negative"),
    "reopening_contract_remains_complete": g71["minimal_extension_contract_is_complete"],
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP427",
    "title": "Post-actuator flavor-selector disposition",
    "admitted_state_domain": "nondegenerate quark Yukawa pairs modulo full weak-basis equivalence",
    "faithful_quotient_coordinate": "physical16",
    "source_authorized_probe_family": "finite-time Standard Model RG transport plus physical16-generated experimental readouts",
    "contextual_partition": "complete RG transport separates regular physical points but has no proper image; measured ten remains nonfaithful",
    "classification": {
        "RG": "separator, not selector",
        "physical16_readout": "separator, not selector",
        "texture_atlas": "presentation rigidifier",
        "WP128": "conditional selector architecture without source/instrument authority",
        "current_complete_family": "neither an admitted selector nor a universal no-go",
    },
    "smallest_exact_falsifier": "one source-derived boundary/preparation law passing descent, proper physical16 image, ensemble survival, threshold accessibility, and executable open-rival instrument gates",
    "remaining_physical_instrument_gate": "an executable multi-point threshold instrument faithful on a predeclared non-gauge UV rival class",
    "reopening_constructor": "source-selected trajectory or compact support scale normalized relative to a physical clock",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp427_post_actuator_selector_disposition.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
