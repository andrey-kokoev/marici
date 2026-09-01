import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Model the seven interaction/CS channels as e1..e7 and the loop-independent
# contact port as e8.  Benincasa's provenance audit states that the contact
# port is disjoint from the rank-seven interaction quotient.
interaction_rank = 7
contact = [Fraction(0)] * 7 + [Fraction(1)]
assert len(contact) == 8
with_contact_rank = 8
assert with_contact_rank == interaction_rank + 1

# WP1094's integer-lift witness changes channel 4.
required_lift_shift = [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
occupation = required_lift_shift
assert len(required_lift_shift) == 7

# A contact counterterm has zero component on every CS channel, so it cannot
# implement the lift or change its channel-resolved evaluation.
contact_on_cs = contact[:7]
assert all(v == 0 for v in contact_on_cs)
delta_evaluation = sum(a*b for a,b in zip(contact_on_cs, occupation))
assert delta_evaluation == 0
assert sum(a*b for a,b in zip(required_lift_shift, occupation)) == 1

supply = {
    "contact_port_disjoint_from_rank7": True,
    "contact_counterterm_can_shift_contact_readout": True,
    "absolute_cs_lift_selected": False,
    "channel_evaluation_changed": False,
    "counterterm_basis_or_renormalization_condition": False,
    "physical16_descent": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1098.v1",
    "status": "PASS",
    "question": "Can a local contact counterterm supply the absolute UV boundary Chern-Simons lift?",
    "interaction_rank": interaction_rank,
    "with_contact_rank": with_contact_rank,
    "required_lift_shift": [str(v) for v in required_lift_shift],
    "contact_on_cs_channels": [str(v) for v in contact_on_cs],
    "contact_delta_on_lift_occupation": str(delta_evaluation),
    "current_source_supply": supply,
    "classification": "negative gate: contact-port shifts are disjoint from the seven-channel boundary lift",
    "remaining_gate": "UV boundary packet selecting the absolute CS lift, counterterm convention, endpoint orientation, and physical16 descent",
    "hostile_gate": "do not promote a loop-independent contact shift or rank-disjointness theorem into a seven-channel Chern-Simons lift",
    "claim_boundary": "the counterterm may alter contact readout, but its projection to the required CS channel shift is zero in the admitted provenance model",
    "disposition": "contact-counterterm boundary-lift loophole closed",
}

(ROOT / "results" / "wp1098_contact_counterterm_boundary_lift_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1098 PASS:", interaction_rank, with_contact_rank, delta_evaluation)
