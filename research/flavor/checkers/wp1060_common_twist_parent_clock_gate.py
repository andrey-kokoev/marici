import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP753's admitted tower has massless bulk fields with one common twist
# charge.  On the WP1059 parent packet this makes the inter-parent clock exact
# at every KK level, but leaves the radius as the absolute scale.
def kk_mass_sq(n, q, R=1):
    return Fraction(n * n + 2 * n * q + q * q, R * R)

q_common = Fraction(1, 2)
level = 0
m15 = kk_mass_sq(level, q_common)
mbar6 = kk_mass_sq(level, q_common)
assert m15 == mbar6 == Fraction(1, 4)
assert m15 / mbar6 == 1

# Normalize the common pole clock to one.  This is a unit choice, not a source
# derivation of the absolute radius.
unit_normalization = Fraction(1, 1) / m15
assert m15 * unit_normalization == 1
assert mbar6 * unit_normalization == 1

# Exact hostiles against overclaiming the common-twist theorem.
different_twists = (
    kk_mass_sq(0, Fraction(1, 2)),
    kk_mass_sq(0, Fraction(3, 2)),
)
assert different_twists == (Fraction(1, 4), Fraction(9, 4))
assert different_twists[0] / different_twists[1] == Fraction(1, 9)

parent_bulk_mass_hostile = (
    kk_mass_sq(0, Fraction(1, 2)),
    kk_mass_sq(0, Fraction(1, 2)) + 1,
)
assert parent_bulk_mass_hostile == (Fraction(1, 4), Fraction(5, 4))
assert parent_bulk_mass_hostile[0] / parent_bulk_mass_hostile[1] == Fraction(1, 5)

radius_two_common_clock = kk_mass_sq(0, q_common, R=2)
assert radius_two_common_clock == Fraction(1, 16)
assert radius_two_common_clock / m15 == Fraction(1, 4)

# The WP1059 bulk-weighted mean is common under the shared tower.
bulk_weighted_mean = Fraction(15 * m15 + 8 * mbar6, 23)
assert bulk_weighted_mean == Fraction(1, 4)
assert bulk_weighted_mean * unit_normalization == 1

result = {
    "schema": "marici.flavor.wp1060.v1",
    "status": "PASS",
    "question": "Does WP753's massless common-twist tower close WP1059's inter-parent clock gap?",
    "common_twist_cell": {
        "level": level,
        "twist": str(q_common),
        "m15_sq": str(m15),
        "mbar6_sq": str(mbar6),
        "ratio": "1",
        "bulk_weighted_mean": str(bulk_weighted_mean),
        "unit_normalized_clock": "1",
    },
    "hostiles": {
        "different_twist_charges": {
            "m15_sq": str(different_twists[0]),
            "mbar6_sq": str(different_twists[1]),
            "ratio_15_over_bar6": str(different_twists[0] / different_twists[1]),
        },
        "parent_bulk_mass_added": {
            "m15_sq": str(parent_bulk_mass_hostile[0]),
            "mbar6_sq": str(parent_bulk_mass_hostile[1]),
            "ratio_15_over_bar6": str(parent_bulk_mass_hostile[0] / parent_bulk_mass_hostile[1]),
        },
        "radius_two_common_clock": {
            "mass_sq": str(radius_two_common_clock),
            "ratio_to_reference": str(radius_two_common_clock / m15),
            "note": "common, but not the absolute unit clock",
        },
    },
    "classification": "conditional common-twist clock constructor: one massless twist charge makes the 15 and bar6 parent clocks equal at every KK level; it does not derive the common twist, masslessness, or absolute radius",
    "remaining_gate": "derive the common twist/masslessness from the anomaly-complete localization, stabilize the radius or compactification clock, and calibrate p^2/M^2 in the same frame",
    "claim_boundary": "uses WP753's admitted massless one-common-twist tower; bulk masses and multiple twist charges are outside that theorem",
    "disposition": "productive: the inter-parent clock gap is conditionally closed, leaving absolute scale and momentum calibration as the next typed blockers",
}

(ROOT / "results" / "wp1060_common_twist_parent_clock_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1060 PASS:", m15, mbar6, bulk_weighted_mean, radius_two_common_clock)
