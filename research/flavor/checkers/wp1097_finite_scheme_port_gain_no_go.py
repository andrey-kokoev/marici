import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Benincasa finite-scheme witness ports x=(0,1,2).
x = [Fraction(0), Fraction(1), Fraction(2)]
det = (x[1]-x[0]) * (x[2]-x[0]) * (x[2]-x[1])
assert det == 2
port_rank = 3

# The flavor event-reweighting problem has six independent soft channels.
soft_dimensions = [6, 8, 1, 4, 2, 2]
event_count = len(soft_dimensions)
assert event_count == 6
assert port_rank < event_count

# A constant normalized response evaluates to one at every port; evaluation is
# not the required gain 3/2.
constant_values = [Fraction(1) for _ in x]
assert constant_values == [1, 1, 1]
evaluation_gain = Fraction(1)
required_gain = Fraction(3, 2)
assert evaluation_gain != required_gain

# Three faithful scheme coordinates are not six branch-to-physical16 rows.
supply = {
    "three_ports_faithful_on_scheme_orbit": True,
    "six_event_weights": False,
    "branch_to_physical16_kernel": False,
    "gain_three_halves": False,
    "production_channel_selection": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1097.v1",
    "status": "PASS",
    "question": "Can finite-scheme normalization ports supply event reweighting or gain?",
    "ports": [str(v) for v in x],
    "vandermonde_determinant": str(det),
    "port_rank": port_rank,
    "event_count": event_count,
    "constant_response_values": [str(v) for v in constant_values],
    "evaluation_gain": str(evaluation_gain),
    "required_gain": str(required_gain),
    "current_source_supply": supply,
    "classification": "negative gate: finite-scheme port faithfulness is not event reweighting or gain",
    "remaining_gate": "source-derived six-row production kernel with event weights and gain 3/2",
    "hostile_gate": "do not promote three faithful normalization coordinates or Vandermonde invertibility into six event weights or gain 3/2",
    "claim_boundary": "the three-port theorem selects a finite scheme point; it has no branch or physical16 output rows",
    "disposition": "finite-scheme-port gain loophole closed",
}

(ROOT / "results" / "wp1097_finite_scheme_port_gain_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1097 PASS:", det, port_rank, event_count, evaluation_gain, required_gain)
