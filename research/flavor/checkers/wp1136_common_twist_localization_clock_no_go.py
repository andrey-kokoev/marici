import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1060 conditional common-twist parent clock: massless bulk fields, common
# half twist, unit radius, level zero.
q = Fraction(1,2)
n = 0
M15 = (n+q)**2
M6bar = (n+q)**2
assert M15 == Fraction(1,4)
assert M6bar == Fraction(1,4)
assert M15/M6bar == 1

# Descent to the localized cell is a separate theorem. WP1058 leaves five
# independent invariant mass blocks after exchange; the parent clock has one
# common value. No source map shows localization preserves the common twist
# clock on all residual sectors.
parent_mass_blocks = 1
localized_mass_blocks_after_exchange = 5
localization_preserving_clock_maps = 0
mass_descent_certificates = 0
assert parent_mass_blocks == 1
assert localized_mass_blocks_after_exchange == 5
assert localization_preserving_clock_maps == 0
assert mass_descent_certificates == 0

# Even if descent existed, absolute radius remains uncalibrated; R=2 changes
# the common value without changing equality.
R2_value = Fraction(1,16)
assert R2_value != Fraction(1,4)

result = {
    "schema": "marici.flavor.wp1136.v1",
    "status": "PASS",
    "question": "Can the common-twist tower align the localized mass clock?",
    "dpc": {
        "conjecture": "The massless common-twist tower aligns parent masses and descends to the common clock on all localized sectors.",
        "rivals": [
            "common-twist parent alignment with localization descent",
            "parent-only alignment",
            "radius-calibrated descent",
            "no localized alignment"
        ],
        "risky_consequences": [
            "M15^2=M6bar^2=(n+q)^2",
            "a localization-preserving clock map",
            "all five residual mass blocks inherit the common value",
            "an absolute radius calibration"
        ],
        "falsification_attempt": "Parent alignment is exact at M^2=1/4, but the localized cell has five invariant mass blocks and zero descent certificates; radius remains uncalibrated.",
        "residual": "A future localization theorem could preserve the tower clock and calibrate radius.",
        "disposition": "reject common-twist tower as localized mass-clock authority"
    },
    "twist_q": str(q),
    "kk_level": n,
    "parent_masses": {"15": str(M15), "bar6": str(M6bar)},
    "parent_ratio": "1",
    "parent_mass_blocks": parent_mass_blocks,
    "localized_mass_blocks_after_exchange": localized_mass_blocks_after_exchange,
    "localization_preserving_clock_maps": localization_preserving_clock_maps,
    "mass_descent_certificates": mass_descent_certificates,
    "radius2_common_value": str(R2_value),
    "classification": "negative gate: common parent tower does not descend to the localized mass clock",
    "remaining_gate": "derive localization-preserving clock descent and absolute radius calibration",
    "hostile_gate": "do not treat common twist, parent equality, or radius-changing equality as localized clock authority",
    "claim_boundary": "this rejects current descent, not the conditional WP1060 parent alignment",
    "disposition": "common-twist localized alignment rejected",
}

(ROOT / "results" / "wp1136_common_twist_localization_clock_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1136 PASS:", M15, localized_mass_blocks_after_exchange, localization_preserving_clock_maps)
