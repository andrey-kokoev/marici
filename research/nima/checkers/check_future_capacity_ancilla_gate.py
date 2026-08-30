"""Independent-ancilla inflation gate for prospective entropy."""

import json
from pathlib import Path
import sympy as sp


def H(ps):
    return sp.simplify(-sum(p*sp.log(p) for p in ps if p != 0))


# Present variable X is fair; system future Y copies X exactly.
p_x = [sp.Rational(1, 2), sp.Rational(1, 2)]
p_y = p_x
p_xy = [sp.Rational(1, 2), 0, 0, sp.Rational(1, 2)]
I_xy = sp.simplify(H(p_x) + H(p_y) - H(p_xy))

# Add an independent fair spectator Z.  It doubles raw future alternatives
# and raises H(Y,Z), but carries no information about X.
p_z = [sp.Rational(1, 2), sp.Rational(1, 2)]
p_yz = [py*pz for py in p_y for pz in p_z]
p_xyz = [pxy*pz for pxy in p_xy for pz in p_z]
I_xyz = sp.simplify(H(p_x) + H(p_yz) - H(p_xyz))

entropy_inflation = sp.simplify(H(p_yz) - H(p_y))
assert entropy_inflation == sp.log(2)
assert sp.simplify(I_xyz - I_xy) == 0

result = {
    "status": "PASS",
    "raw_future_entropy_before": str(H(p_y)),
    "raw_future_entropy_after_independent_spectator": str(H(p_yz)),
    "inflation": str(entropy_inflation),
    "connected_information_before": str(I_xy),
    "connected_information_after": str(I_xyz),
    "connected_change": str(sp.simplify(I_xyz-I_xy)),
    "conclusion": (
        "Total prospective entropy suffers spectator-noise inflation. A viable "
        "future-capacity law must quotient independent factors or use a "
        "causally connected quantity such as mutual information/channel capacity."
    ),
}
out = Path(__file__).parents[1] / "results" / "future_capacity_ancilla_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
