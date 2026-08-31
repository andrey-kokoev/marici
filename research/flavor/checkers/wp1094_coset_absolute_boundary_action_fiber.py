import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1070 required coset.
s = [Fraction(1,2), Fraction(1,4), Fraction(0), Fraction(0), Fraction(0), Fraction(3,4), Fraction(0)]
integer_shift = [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
lift0 = s
lift1 = [a + b for a, b in zip(s, integer_shift)]
assert [x % 1 for x in lift0] == [x % 1 for x in lift1]
assert lift0 != lift1

# A flux/channel occupation vector evaluates the two lifts differently.
t = [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
S0 = sum(a*b for a,b in zip(lift0,t))
S1 = sum(a*b for a,b in zip(lift1,t))
assert S0 == 0
assert S1 == 1
assert S1 - S0 == 1

# The anomaly cancellation condition sees only the coset; the boundary-action
# packet must select the absolute lift, counterterm convention, and orientation.
supply = {
    "required_coset_fixed": True,
    "integer_lift_ambiguity": True,
    "same_mod_integral_coset": True,
    "distinct_channel_evaluation": True,
    "absolute_boundary_lift_selected": False,
    "counterterm_normalization_selected": False,
}
assert list(supply.values()).count(False) == 2

result = {
    "schema": "marici.flavor.wp1094.v1",
    "status": "PASS",
    "question": "Does the required anomaly coset determine the absolute UV boundary Chern-Simons action?",
    "required_coset": [str(v) for v in s],
    "lift0": [str(v) for v in lift0],
    "lift1": [str(v) for v in lift1],
    "channel_occupation": [str(v) for v in t],
    "evaluation0": str(S0),
    "evaluation1": str(S1),
    "difference": str(S1-S0),
    "current_source_supply": supply,
    "classification": "negative gate: anomaly cancellation fixes a coset, not an absolute boundary-action lift",
    "remaining_gate": "UV boundary packet selecting the absolute Chern-Simons lift, counterterm convention, endpoint orientation, and physical16 descent",
    "hostile_gate": "do not identify an anomaly coset modulo integers with a unique classical boundary action or normalization",
    "claim_boundary": "integer shifts preserve the WP1070 coset but can change channel-resolved boundary evaluation",
    "disposition": "coset-to-action uniqueness loophole closed",
}

(ROOT / "results" / "wp1094_coset_absolute_boundary_action_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1094 PASS:", S0, S1, S1-S0)
