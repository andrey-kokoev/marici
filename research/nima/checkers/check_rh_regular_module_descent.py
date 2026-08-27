from fractions import Fraction as F
import json
from pathlib import Path


def eval_poly(coeffs, z):
    return sum(F(c) * z**i for i, c in enumerate(coeffs))


# Hostile M(z)=z, R(z)=1. Pointwise away from zero, L=1/z works, but no
# polynomial or regular factor exists across z=0.
M = (F(0), F(1))
R = (F(1),)
samples = {}
for z in (F(1), F(2), F(3)):
    l_value = eval_poly(R, z) / eval_poly(M, z)
    samples[str(z)] = str(l_value)
    assert l_value * eval_poly(M, z) == eval_poly(R, z)
assert eval_poly(M, F(0)) == 0
assert eval_poly(R, F(0)) == 1

# Successful regular factorization R_good=z^2=(z)M.
R_good = (F(0), F(0), F(1))
L_good = (F(0), F(1))
for z in (F(-2), F(0), F(3)):
    assert eval_poly(R_good, z) == eval_poly(L_good, z) * eval_poly(M, z)

result = {
    "schema": "marici.rh-regular-module-descent.v1",
    "meromorphic_hostile": {
        "M": "z",
        "R": "1",
        "pointwise_factors": samples,
        "formal_factor": "1/z",
        "regular_at_zero": False,
        "hidden_residual_at_zero": "R(0)=1 while M(0)=0",
    },
    "regular_success": {
        "M": "z",
        "R": "z^2",
        "factor": "z",
    },
    "tautological_injection_hostile": {
        "augmented_rows": ["z", "1"],
        "factor": "[0,1]",
        "failure": "carrier_row_inserted_without_source_authority",
    },
    "required_gate": "regular_source_ring_module_membership_with_authorized_rows",
}

out = Path(__file__).parents[1] / "results" / "rh-regular-module-descent.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
