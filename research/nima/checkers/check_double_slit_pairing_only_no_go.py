"""Exact countermodel: Gram positivity alone does not constrain a free D readout."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/double-slit-pairing-only-no-go.json"


# A valid normalized positive Gram with gamma=4/5.
gamma = Fraction(4, 5)
gram_determinant = 1 - gamma * gamma

# If distinguishability is attached as an independent readout policy, nothing
# in Gram positivity prohibits choosing D=4/5 as well.
free_distinguishability = Fraction(4, 5)
free_sum = gamma * gamma + free_distinguishability * free_distinguishability

# When D is instead derived from the same record-projector separator, its
# square is the Gram determinant and complementarity closes.
derived_distinguishability_squared = gram_determinant
derived_sum = gamma * gamma + derived_distinguishability_squared

gates = {
    "gram_is_strictly_positive": gram_determinant > 0,
    "free_readout_violates_duality": free_sum > 1,
    "same_object_separator_restores_duality": derived_sum == 1,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.double-slit-pairing-only-no-go.v1",
    "countermodel": {
        "gamma": str(gamma),
        "gram_determinant": str(gram_determinant),
        "independently_attached_D": str(free_distinguishability),
        "V_squared_plus_free_D_squared": str(free_sum),
    },
    "derived_interface": {
        "D_squared": str(derived_distinguishability_squared),
        "V_squared_plus_D_squared": str(derived_sum),
    },
    "gates": gates,
    "conclusion": (
        "Positive coherence constrains overlap but does not constrain an "
        "independently attached distinguishability readout. The separator "
        "must be generated from the same positive record object."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

