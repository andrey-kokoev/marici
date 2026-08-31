import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Grant all upstream repairs through WP1041, including the selected dimensionless threshold ratio.
x = Fraction(1, 1)  # p2/M2
threshold_shape = Fraction(1, 1) / (1 + x)  # R(p2)/R(0)
assert threshold_shape == Fraction(1, 2)

# The physical16 portal row still contains the source-detector gain/interface coefficient.
g1 = Fraction(1, 1)
g2 = Fraction(2, 1)
portal1 = g1 * threshold_shape
portal2 = g2 * threshold_shape
assert portal1 == Fraction(1, 2)
assert portal2 == Fraction(1, 1)
assert portal2 - portal1 == Fraction(1, 2)

# Normalized one-port fractions cannot see the common gain.
normalized1 = portal1 / portal1
normalized2 = portal2 / portal2
assert normalized1 == normalized2 == 1

result = {
    "schema": "marici.flavor.wp1042.v1",
    "status": "PASS",
    "question": "Would a source-locked threshold ratio by itself give a physical16 portal prediction?",
    "granted_upstream_repairs": [
        "integer labels k=2,C=23 selected",
        "typed degenerate one-pole operator selected",
        "calibrated momentum port supplied",
        "dimensionless ratio p2/M2=1 selected"
    ],
    "threshold_shape": {"p2_over_M2": "1", "R_over_R0": str(threshold_shape)},
    "hostile_interface_gains": {
        "gain_1": {"g": str(g1), "physical16_portal_row": str(portal1)},
        "gain_2": {"g": str(g2), "physical16_portal_row": str(portal2)}
    },
    "normalized_fraction_collision": {
        "gain_1_fraction": str(normalized1),
        "gain_2_fraction": str(normalized2)
    },
    "first_nonfaithful_arrow": "threshold shape to calibrated physical16 portal row without a source-detector gain law",
    "classification": "source-locked threshold ratio would be a shape selector, not an absolute physical16 normalization selector",
    "remaining_gate": "derive the source-to-Yukawa or source-to-detector coupling gain in the same frame as the threshold ratio, with an absolute or interference-calibrated physical16 instrument",
    "claim_boundary": "one-row multiplicative interface after granting all WP1038-WP1041 repairs; does not exclude a Ward identity or interference monitor fixing gain",
    "disposition": "negative for ratio-only completion of the integer-pole branch"
}

(ROOT / "results" / "wp1042_ratio_to_physical16_gain_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1042 PASS:", threshold_shape, portal1, portal2)
