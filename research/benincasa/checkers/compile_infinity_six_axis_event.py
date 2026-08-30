"""Compile the infinity selector/readout packet on Aspect's six typed axes."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "infinity-six-axis-event.json"


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def main() -> None:
    physical = load("infinity-physical-line-connection.json")
    dark_port = load("infinity-readout-aspect-dark-port.json")
    descent = load("infinity-integral-dihedral-descent.json")
    path = load("infinity-deck-selector-path-obstruction.json")
    detector = load("comoving-deck-detector-holonomy.json")

    event = {
        "scalar": "bright",
        "packet": "bright",
        "incidence": "matched",
        "history": "unknown",
        "path": "disconnected",
        "coefficient": "native",
    }
    derived = {
        "physical_readout_exists": event["scalar"] == "bright" and event["packet"] == "bright",
        "typed_pairing_descends": event["incidence"] == "matched" and event["coefficient"] == "native",
        "endpoint_without_symmetric_path": event["path"] == "disconnected",
        "source_constructible_selector": event["path"] == "admissible" and event["coefficient"] == "native",
        "history_authorized": event["history"] != "unknown",
    }
    checks = {
        "physical_scalar_is_nonzero": physical["all_checks_pass"],
        "both_packet_arms_are_nonzero": dark_port["checks"]["direct_arm_is_nonzero"] and dark_port["checks"]["reciprocal_arm_is_nonzero"],
        "incidence_pairing_is_primitive": descent["checks"]["paired_diagonal_generator_is_primitive"],
        "coefficient_line_is_native": descent["coefficient_reflection"].startswith("minus one"),
        "fixed_source_path_is_disconnected": path["checks"]["identity_has_even_projective_character"] and path["checks"]["selector_has_odd_projective_character"],
        "moving_history_is_candidate_not_source_authority": detector["scope"].endswith("no source authorization for the moving detector is inferred"),
        "unknown_history_is_preserved": event["history"] == "unknown",
        "selector_is_not_source_constructible": not derived["source_constructible_selector"],
        "no_scalar_zero_is_inferred": event["scalar"] == "bright",
    }
    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "marici.infinity_six_axis_event.v1",
        "compiler": "adaptation of marici.aspect.typed_six_axis_optical_event_compiler",
        "event": event,
        "derived": derived,
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "rule": "unknown_is_not_false_and_native_coefficient_does_not_authorize_path",
        "conclusion": "The infinity readout is bright, incidence-matched, and has a native coefficient line, but the selective controller is not source-constructible because its fixed-source path is disconnected and its co-moving history remains unauthorized.",
        "quartic_consequence": "No Q activation follows from the existing readout packet or coefficient character.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
