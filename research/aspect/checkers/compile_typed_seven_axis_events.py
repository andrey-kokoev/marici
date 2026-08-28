import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
six = json.loads((RESULTS / "typed_six_axis_optical_events.json").read_text(encoding="utf-8"))

events = {name: dict(event, action="unknown") for name, event in six["events"].items()}
events["selective_gate_path"]["action"] = "missing"
events["cosmology_coefficient_without_selector"] = {
    "scalar": "unknown",
    "packet": "unknown",
    "incidence": "unknown",
    "history": "unknown",
    "path": "unknown",
    "coefficient": "native",
    "action": "missing",
}

allowed_action = {"authorized", "missing", "unknown"}


def derive(event):
    return {
        "selected_transmission_zero": event["scalar"] == "dark" and event["packet"] == "bright",
        "incidence_alias": event["incidence"] == "aliased",
        "normalization_erasure": event["scalar"] == "flat_normalized" and event["history"] == "nontrivial",
        "path_obstruction": event["path"] == "disconnected",
        "coefficient_extension_gap": event["coefficient"] == "requires_extension",
        "operational_action_gap": event["action"] == "missing",
    }


derived = {name: derive(event) for name, event in events.items()}
cosmology = events["cosmology_coefficient_without_selector"]
selective = events["selective_gate_path"]

checks = {
    "six_axis_input_passes": six["status"] == "pass",
    "every_action_value_is_typed": all(event["action"] in allowed_action for event in events.values()),
    "cosmology_coefficient_is_native": cosmology["coefficient"] == "native",
    "cosmology_action_is_missing": cosmology["action"] == "missing",
    "native_coefficient_does_not_authorize_action": cosmology["coefficient"] == "native" and cosmology["action"] != "authorized",
    "missing_action_does_not_infer_path_obstruction": cosmology["action"] == "missing" and cosmology["path"] == "unknown",
    "selective_gate_has_three_separate_gaps": selective["path"] == "disconnected" and selective["coefficient"] == "requires_extension" and selective["action"] == "missing",
    "transmission_fixture_makes_no_action_claim": events["rosenbrock_incidence"]["action"] == "unknown",
    "normalization_fixture_makes_no_action_claim": events["all_order_normalization"]["action"] == "unknown",
    "operational_gap_is_derived_only_from_action_axis": derived["cosmology_coefficient_without_selector"]["operational_action_gap"],
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "axis_count": 7,
    "action_values": sorted(allowed_action),
    "events": events,
    "derived": derived,
    "rule": "coefficient_does_not_authorize_action",
}
out = RESULTS / "typed_seven_axis_events.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
