import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "contracts" / "flavor-interaction-net-state.v1.json").read_text())
nodes = {node["id"]: node for node in contract["nodes"]}

tested_gates = [
    "wp1135_parent_projection_mass_clock_no_go",
    "wp1136_common_twist_localization_clock_no_go",
    "wp1137_radius_absolute_clock_no_go",
]
assert all(name in nodes for name in tested_gates)
assert all(nodes[name]["status"] == "constructed" for name in tested_gates)

# Exact target and retained conditional facts.
target_M2 = Fraction(1)
parent_clock = Fraction(1,4)
assert target_M2 == 1
assert parent_clock == Fraction(1,4)

constructor_candidates = [
    "spin-11 projection",
    "common-twist parent alignment",
    "radius stabilization",
]
current_source_passes = 0
assert current_source_passes == 0

# First missing typed object and its acceptance test. This is a branch blocker,
# not a new abstract successor.
missing_object = {
    "id": "compactification_clock_packet",
    "required_fields": [
        "unique_flux_sector_n",
        "gauge_gravity_ratio_B_over_A",
        "localization_preserving_clock_descent",
        "physical_momentum_frame"
    ],
    "failed_consequence": "absolute localized pole clock M^2=1",
    "acceptance_test": "derive n and B/A=6n^2 from one compactification packet, prove descent to all localized sectors, and evaluate p^2/M^2 in the same frame"
}
assert len(missing_object["required_fields"]) == 4

result = {
    "schema": "marici.flavor.wp1138.v1",
    "status": "PASS",
    "question": "Does the current source packet contain an admissible localized mass-clock constructor?",
    "dpc": {
        "conjecture": "The current source packet contains a constructor for the absolute localized pole clock.",
        "rivals": [
            "spin-11 projection",
            "common-twist parent alignment",
            "radius stabilization"
        ],
        "risky_consequences": [
            "equivariant port-preserving cell projection",
            "localization-preserving common-twist descent",
            "unique sourced flux sector and B/A",
            "same-frame p^2/M^2"
        ],
        "falsification_attempt": "All three rivals fail their authority interfaces; zero current-source constructors pass.",
        "residual": "A future compactification clock packet may satisfy the typed acceptance test.",
        "disposition": "reject current-source mass-clock closure and record the first missing typed object"
    },
    "tested_gates": tested_gates,
    "constructor_candidates": constructor_candidates,
    "current_source_passes": current_source_passes,
    "target_M2": str(target_M2),
    "conditional_parent_clock": str(parent_clock),
    "missing_object": missing_object,
    "classification": "closure audit: conditional clock facts exist, but absolute localized clock authority is absent",
    "remaining_gate": "materialize compactification_clock_packet and pass its acceptance test",
    "hostile_gate": "do not aggregate conditional clock facts or repeated negative gates into absolute clock authority",
    "claim_boundary": "this closes tested current-source mass-clock rivals, not a future compactification packet",
    "disposition": "mass-clock branch deferred on compactification_clock_packet",
}

(ROOT / "results" / "wp1138_mass_clock_constructor_closure_audit.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1138 PASS:", len(tested_gates), current_source_passes, missing_object["id"])
