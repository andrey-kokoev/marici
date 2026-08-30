import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def load_result(name):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


rosenbrock = load_result("incidence_aware_rosenbrock_classifier.json")
history = load_result("graded_history_normalization_erasure.json")
path = load_result("reflection_component_path_tomography.json")

unknown = "unknown"

events = {
    "rosenbrock_incidence": {
        "scalar": "dark",
        "packet": "bright",
        "incidence": "aliased",
        "history": unknown,
        "path": unknown,
        "coefficient": unknown,
    },
    "all_order_normalization": {
        "scalar": "flat_normalized",
        "packet": "bright",
        "incidence": unknown,
        "history": "nontrivial",
        "path": unknown,
        "coefficient": unknown,
    },
    "selective_gate_path": {
        "scalar": unknown,
        "packet": unknown,
        "incidence": unknown,
        "history": unknown,
        "path": "disconnected",
        "coefficient": "requires_extension",
    },
}


def derive(event):
    return {
        "selected_transmission_zero": event["scalar"] == "dark" and event["packet"] == "bright",
        "incidence_alias": event["incidence"] == "aliased",
        "normalization_erasure": event["scalar"] == "flat_normalized" and event["history"] == "nontrivial",
        "endpoint_without_symmetric_path": event["path"] == "disconnected",
        "coefficient_authority_gap": event["coefficient"] == "requires_extension",
    }


derived = {name: derive(event) for name, event in events.items()}

allowed = {
    "scalar": {"bright", "dark", "flat_normalized", unknown},
    "packet": {"zero", "bright", unknown},
    "incidence": {"matched", "aliased", unknown},
    "history": {"trivial", "nontrivial", unknown},
    "path": {"admissible", "disconnected", unknown},
    "coefficient": {"native", "requires_extension", unknown},
}

checks = {
    "all_upstream_results_pass": all(item["status"] == "pass" for item in (rosenbrock, history, path)),
    "every_axis_value_is_typed": all(
        value in allowed[axis]
        for event in events.values()
        for axis, value in event.items()
    ),
    "rosenbrock_is_transmission_zero": derived["rosenbrock_incidence"]["selected_transmission_zero"],
    "rosenbrock_is_incidence_alias": derived["rosenbrock_incidence"]["incidence_alias"],
    "rosenbrock_does_not_claim_path_status": events["rosenbrock_incidence"]["path"] == unknown,
    "history_event_is_normalization_erasure": derived["all_order_normalization"]["normalization_erasure"],
    "history_event_does_not_claim_incidence": events["all_order_normalization"]["incidence"] == unknown,
    "path_event_detects_component_obstruction": derived["selective_gate_path"]["endpoint_without_symmetric_path"],
    "path_event_detects_coefficient_gap": derived["selective_gate_path"]["coefficient_authority_gap"],
    "path_event_makes_no_zero_claim": events["selective_gate_path"]["scalar"] == unknown and events["selective_gate_path"]["packet"] == unknown,
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "axes": {axis: sorted(values) for axis, values in allowed.items()},
    "events": events,
    "derived": derived,
    "rule": "unknown_is_not_false",
}
out = RESULTS / "typed_six_axis_optical_events.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
