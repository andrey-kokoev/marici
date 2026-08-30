import json
from pathlib import Path


ASPECT = Path(__file__).resolve().parents[1]
MARICI = ASPECT.parents[1]
RESULTS = ASPECT / "results"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


seven = load(RESULTS / "typed_seven_axis_events.json")
dual = load(RESULTS / "primitive_product_dual_return_gain.json")
infinity = load(MARICI / "research" / "benincasa" / "results" / "infinity-seven-axis-event.json")

registry = {
    "scalar": {"bright", "dark", "flat_normalized", "unknown"},
    "packet": {"zero", "bright", "unknown"},
    "incidence": {"matched", "aliased", "unknown"},
    "history": {"trivial", "nontrivial", "unknown"},
    "path": {"admissible", "disconnected", "unknown"},
    "coefficient": {"native", "requires_extension", "unknown"},
    "action": {"authorized", "missing", "unknown"},
    "duality_exchange": {"intertwined", "broken", "unknown"},
    "action:optical_emulator": {"authorized", "missing", "unknown"},
    "action:physical_dual_source": {"authorized", "missing", "unknown"},
}


def validate(event):
    return all(key in registry and value in registry[key] for key, value in event.items())


events = dict(seven["events"])
events["infinity_physical_readout_external"] = infinity["events"]["physical_infinity_readout"]
events["infinity_selective_control_external"] = infinity["events"]["selective_sheet_control"]
events["primitive_product_hostile"] = {
    "scalar": "dark",
    "packet": "bright",
    "incidence": "unknown",
    "history": "unknown",
    "path": "unknown",
    "coefficient": "native",
    "action": "unknown",
    "duality_exchange": "broken",
    "action:optical_emulator": "authorized",
    "action:physical_dual_source": "missing",
}

flavor = events["primitive_product_hostile"]
infinity_readout = events["infinity_physical_readout_external"]
infinity_selector = events["infinity_selective_control_external"]
path_witness = infinity["independence_witnesses"]["same_missing_action_with_admissible_path"]
action_witness = infinity["independence_witnesses"]["same_path_with_authorized_action"]

checks = {
    "seven_axis_core_input_passes": seven["status"] == "pass",
    "dual_pair_input_passes": dual["status"] == "pass",
    "external_infinity_checks_all_pass": infinity["passed"] == infinity["total"] == 14,
    "every_event_validates_against_registry": all(validate(event) for event in events.values()),
    "registry_is_extensible_beyond_seven_keys": len(registry) > seven["axis_count"],
    "flavor_product_dark_packet_bright": flavor["scalar"] == "dark" and flavor["packet"] == "bright",
    "flavor_exchange_is_broken": flavor["duality_exchange"] == "broken",
    "emulator_action_does_not_authorize_physical_source": flavor["action:optical_emulator"] == "authorized" and flavor["action:physical_dual_source"] == "missing",
    "infinity_readout_is_independently_constructible": infinity_readout["scalar"] == "bright" and infinity_readout["path"] == "admissible" and infinity_readout["action"] == "authorized",
    "infinity_selector_path_and_action_fail_separately": infinity_selector["path"] == "disconnected" and infinity_selector["action"] == "missing",
    "path_counterfactual_preserves_missing_action": path_witness["path"] == "admissible" and path_witness["action"] == "missing",
    "action_counterfactual_preserves_disconnected_path": action_witness["action"] == "authorized" and action_witness["path"] == "disconnected",
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "core_profile": list(seven["events"]["rosenbrock_incidence"].keys()),
    "registered_capabilities": {key: sorted(values) for key, values in registry.items()},
    "events": events,
    "rule": "capabilities_are_namespaced_and_unknown_preserving",
}
out = RESULTS / "namespaced_capability_registry.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
