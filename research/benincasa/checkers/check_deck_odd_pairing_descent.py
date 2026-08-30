"""Check descent of the deck-odd detector/cycle pairing."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORT = ROOT / "results" / "infinity-relative-port-integral-extension.json"
DETECTOR = ROOT / "results" / "comoving-deck-detector-holonomy.json"
GLOBAL_DESCENT = ROOT / "results" / "infinity-integral-dihedral-descent.json"
OUTPUT = ROOT / "results" / "deck-odd-pairing-descent.json"


def main() -> None:
    port = json.loads(PORT.read_text(encoding="utf-8"))
    detector = json.loads(DETECTOR.read_text(encoding="utf-8"))
    global_descent = json.loads(GLOBAL_DESCENT.read_text(encoding="utf-8"))

    detector_holonomy = detector["oriented_lift_holonomy"]
    cycle_holonomy = -1
    tensor_holonomy = detector_holonomy * cycle_holonomy
    direct_sum_invariant_rank = int(detector_holonomy == 1) + int(cycle_holonomy == 1)
    tensor_invariant_rank = int(tensor_holonomy == 1)

    checks = {
        "physical_cycle_is_deck_odd": port["physical_kernel_generator"] == "e_plus-e_minus",
        "detector_lift_is_deck_odd": detector_holonomy == -1,
        "neither_oriented_factor_descends": direct_sum_invariant_rank == 0,
        "tensor_holonomy_is_trivial": tensor_holonomy == 1,
        "tensor_readout_has_rank_one_invariants": tensor_invariant_rank == 1,
        "integral_pairing_is_primitive": abs(detector_holonomy * cycle_holonomy) == 1,
        "extension_order_matches_sign_cancellation": port["obstruction_order"] == 2,
        "source_coefficient_has_same_sign_character": global_descent["coefficient_reflection"].startswith("minus one"),
        "paired_descent_was_already_source_derived": global_descent["paired_coinvariant"] == "Z",
        "no_selector_action_map_is_exported": all(
            key not in port and key not in global_descent
            for key in ("selector_action", "conditionalization_map", "controller_implementation")
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "marici.deck_odd_pairing_descent.v1",
        "detector_local_system": "Z_minus",
        "physical_cycle_local_system": "Z_minus",
        "separate_invariant_rank": direct_sum_invariant_rank,
        "paired_local_system": "Hom(Z_minus,Z_minus)=Z_plus",
        "paired_holonomy": tensor_holonomy,
        "paired_invariant_rank": tensor_invariant_rank,
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "conclusion": "The co-moving detector character is representation-equivalent to the source ordered-residue coefficient line, and their paired descent was already proved in the global dihedral packet. No source map makes that coefficient line act as the selector controller.",
        "authority_boundary": "Character equality and paired descent do not authorize an operational conditionalization map.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
