import json
from fractions import Fraction
from pathlib import Path


# Rational invertible scalar witnesses avoid numerical exponentials. A
# contraction factor c and its reciprocal cannot both be at most one unless
# c=1.
factors = [Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2), Fraction(2)]
rows = []
for factor in factors:
    inverse = 1 / factor
    forward_contractive = factor <= 1
    inverse_contractive = inverse <= 1
    both = forward_contractive and inverse_contractive
    assert both == (factor == 1)
    rows.append({
        "factor": str(factor),
        "inverse_factor": str(inverse),
        "forward_contractive": forward_contractive,
        "inverse_contractive": inverse_contractive,
        "both_contractive": both,
    })

# Norm-chain witness: if both operator bounds hold, lower and upper bounds on
# ||T x|| coincide with ||x||.
two_sided_implication = {
    "lower_bound_from_inverse": "||x|| <= ||T x||",
    "upper_bound_from_forward": "||T x|| <= ||x||",
    "conclusion": "||T x|| = ||x||",
}

result = {
    "scalar_witnesses": rows,
    "two_sided_implication": two_sided_implication,
    "strict_two_sided_contraction_exists": False,
    "verdict": "reciprocal inverse flows cannot both be outward-contractive in one fixed norm",
}

output = Path(__file__).parents[1] / "results" / "rh-two-sided-contraction-no-go.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

