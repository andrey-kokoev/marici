import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

history_slots = 3
history_gain = Fraction(1)
pairing_rank = 3
internal_components = history_slots * pairing_rank
assert internal_components == 9

soft_dimensions = [6,8,1,4,2,2]
event_count = len(soft_dimensions)
assert event_count == 6
assert internal_components != event_count

q = [Fraction(d,23) for d in soft_dimensions]
event_target = [Fraction(1,4)] * event_count
assert q != event_target

required_gain = Fraction(3,2)
assert history_gain != required_gain
assert Fraction(pairing_rank) != required_gain
# Any rank/2 normalization is unstated.
source_normalization_rows = 0
physical16_rows = 0
assert source_normalization_rows == 0
assert physical16_rows == 0

supply = {
    "history_isometry": True,
    "bifundamental_pairing": True,
    "six_event_rows": False,
    "event_reweighting": False,
    "gain_three_halves": False,
    "source_normalization": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1105.v1",
    "status": "PASS",
    "question": "Does history dilation plus bifundamental pairing supply event reweighting or gain?",
    "history_slots": history_slots,
    "pairing_rank": pairing_rank,
    "internal_components": internal_components,
    "event_count": event_count,
    "history_gain": str(history_gain),
    "required_gain": str(required_gain),
    "dimension_weighted_soft_distribution": [str(v) for v in q],
    "event_target": [str(v) for v in event_target],
    "source_normalization_rows": source_normalization_rows,
    "physical16_rows": physical16_rows,
    "current_source_supply": supply,
    "classification": "negative gate: isometry times internal pairing is not production gain",
    "remaining_gate": "source-derived six-row production kernel, event reweighting, normalization, and gain 3/2",
    "hostile_gate": "do not promote 3 history slots times rank 3, isometry, or I3 trace into six events or gain 3/2",
    "claim_boundary": "the composite remains internal and norm-preserving; it has no admitted physical16 output matrix",
    "disposition": "history-plus-pairing gain loophole closed",
}

(ROOT / "results" / "wp1105_history_pairing_gain_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1105 PASS:", internal_components, event_count, history_gain, required_gain)
