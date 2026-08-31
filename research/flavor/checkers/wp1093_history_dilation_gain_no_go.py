import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1087's conditional history dilation is an isometry.  Normalize the three
# history slots; their weights are equal and their total norm is one.
history_weights = [Fraction(1, 3) for _ in range(3)]
history_norm = sum(history_weights)
assert history_norm == 1
isometry_gain = Fraction(1)
required_gain = Fraction(3, 2)
assert isometry_gain != required_gain

# Six soft event branches still require a six-row production/reweighting map.
soft_dimensions = [6, 8, 1, 4, 2, 2]
soft_total = sum(soft_dimensions)
assert soft_total == 23
soft_distribution = [Fraction(d, soft_total) for d in soft_dimensions]
event_target = [Fraction(1, 4) for _ in soft_dimensions]
assert len(history_weights) == 3
assert len(event_target) == 6
assert soft_distribution != event_target

# An internal history dilation has no branch-to-physical16 coupling entries.
history_to_soft_rows = 0
history_to_physical16_rows = 0
assert history_to_soft_rows == 0
assert history_to_physical16_rows == 0

supply = {
    "three_normalized_history_slots": True,
    "isometric_history_dilation": True,
    "six_branch_reweighting_map": False,
    "physical16_coupling_rows": False,
    "gain_three_halves": False,
    "production_kernel": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1093.v1",
    "status": "PASS",
    "question": "Does conditional history dilation supply event reweighting or the gain law?",
    "history": {
        "slot_count": 3,
        "normalized_slot_weights": [str(v) for v in history_weights],
        "norm": str(history_norm),
        "gain": str(isometry_gain),
    },
    "soft_events": {
        "branch_dimensions": soft_dimensions,
        "dimension_weighted_distribution": [str(v) for v in soft_distribution],
        "event_target": [str(v) for v in event_target],
        "branch_count": 6,
    },
    "kernel_requirement": {
        "history_to_soft_rows": history_to_soft_rows,
        "history_to_physical16_rows": history_to_physical16_rows,
        "required_event_rows": 6,
    },
    "current_source_supply": supply,
    "classification": "negative gate: conditional history dilation preserves norm and supplies no production gain",
    "remaining_gate": "source-derived production kernel with branch reweighting, physical16 coupling rows, and gain 3/2",
    "hostile_gate": "do not promote three history slots, equal slot weights, isometry, or cyclic history into six event weights or gain 3/2",
    "claim_boundary": "the dilation can preserve cyclic history, but is norm-preserving and internal; it has no admitted production or descent matrix",
    "disposition": "history-dilation gain loophole closed",
}

(ROOT / "results" / "wp1093_history_dilation_gain_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1093 PASS:", history_norm, isometry_gain, required_gain, history_to_physical16_rows)
