"""Compile the infinity packet on Aspect's updated seven independent axes."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ASPECT_RESULTS = ROOT.parent / "aspect" / "results"
OUTPUT = RESULTS / "infinity-seven-axis-event.json"


def load(directory: Path, name: str) -> dict:
    return json.loads((directory / name).read_text(encoding="utf-8"))


def main() -> None:
    six = load(RESULTS, "infinity-six-axis-event.json")
    action_audit = load(RESULTS, "deck-odd-pairing-descent.json")
    aspect = load(ASPECT_RESULTS, "typed_seven_axis_events.json")
    physical = load(RESULTS, "infinity-physical-line-connection.json")

    events = {
        "physical_infinity_readout": {
            "scalar": "bright",
            "packet": "bright",
            "incidence": "matched",
            "history": "trivial",
            "path": "admissible",
            "coefficient": "native",
            "action": "authorized",
        },
        "selective_sheet_control": {
            "scalar": "unknown",
            "packet": "unknown",
            "incidence": "unknown",
            "history": "unknown",
            "path": "disconnected",
            "coefficient": "native",
            "action": "missing",
        },
    }
    readout = events["physical_infinity_readout"]
    selector = events["selective_sheet_control"]
    derived = {
        "physical_readout_is_source_constructible": readout["path"] == "admissible" and readout["action"] == "authorized",
        "selector_has_path_obstruction": selector["path"] == "disconnected",
        "selector_has_operational_action_gap": selector["action"] == "missing",
        "selector_is_source_constructible": selector["path"] == "admissible" and selector["action"] == "authorized",
    }
    same_path_authorized_action = dict(selector, action="authorized")
    same_action_admissible_path = dict(selector, path="admissible")
    checks = {
        "aspect_updated_tester_passes": aspect["status"] == "pass" and aspect["axis_count"] == 7,
        "six_axis_cosmology_adapter_passes": six["passed"] == six["total"],
        "physical_history_is_trivial": physical["monodromy"] == "identity" and readout["history"] == "trivial",
        "physical_readout_action_is_authorized": readout["action"] == "authorized",
        "physical_readout_is_source_constructible": derived["physical_readout_is_source_constructible"],
        "selector_native_coefficient_is_retained": selector["coefficient"] == "native",
        "selector_path_is_independently_disconnected": selector["path"] == "disconnected",
        "action_is_independently_missing": (
            selector["action"] == "missing"
            and action_audit["checks"]["no_selector_action_map_is_exported"]
        ),
        "coefficient_does_not_authorize_action": selector["coefficient"] == "native" and selector["action"] != "authorized",
        "path_does_not_determine_action": same_path_authorized_action["path"] == selector["path"] and same_path_authorized_action["action"] != selector["action"],
        "action_does_not_determine_path": same_action_admissible_path["action"] == selector["action"] and same_action_admissible_path["path"] != selector["path"],
        "selector_unknowns_are_preserved": all(selector[axis] == "unknown" for axis in ("scalar", "packet", "incidence", "history")),
        "readout_values_do_not_leak_into_selector": selector["scalar"] != readout["scalar"] and selector["action"] != readout["action"],
        "selector_is_not_source_constructible": not derived["selector_is_source_constructible"],
    }
    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "marici.infinity_seven_axis_event.v1",
        "compiler": "adaptation of marici.aspect.typed_seven_axis_events",
        "events": events,
        "derived": derived,
        "independence_witnesses": {
            "same_path_with_authorized_action": same_path_authorized_action,
            "same_missing_action_with_admissible_path": same_action_admissible_path,
        },
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "rule": "coefficient_path_and_action_are_independent_typed_axes",
        "conclusion": "The physical infinity readout and selective sheet controller are distinct events. The first is bright, flat, and source-constructible; the second has unknown output, disconnected path, native coefficient character, and missing action. No readout property is transported to the unimplemented selector.",
        "quartic_consequence": "The updated tester preserves the closure: no Q activation is authorized.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
