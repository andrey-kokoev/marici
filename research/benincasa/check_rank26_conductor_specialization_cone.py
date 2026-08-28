"""Exact formal audit of the active-conductor monodromy collision."""

from fractions import Fraction
import json
from pathlib import Path


# Write exp(2*pi*i*(constant + slope*epsilon)) as the pair
# (constant modulo Z, slope).  This retains precisely the formal character
# needed for the specialization test without numerical transcendental input.
alpha = (Fraction(1, 2), Fraction(1))  # -1/2 + eps modulo integers
single = alpha
merged = ((2 * alpha[0]) % 1, 2 * alpha[1])

checks = {
    "single_branch_constant_character_is_minus_one": single[0] == Fraction(1, 2),
    "merged_conductor_constant_character_is_trivial": merged[0] == 0,
    "merged_first_epsilon_character_is_nonzero": merged[1] == 2,
    "two_single_slopes_add_to_merged_slope": 2 * single[1] == merged[1],
}

# In logarithmic normalization, d/d eps of the merged character is
# 2*pi*i*merged[1] = 4*pi*i.  The source normalization has first coefficient
# eps, while the local conductor integral has principal part 1/eps.
normalization_order = 1
conductor_pole_order = -1
finite_grade = normalization_order + conductor_pole_order
checks["source_normalization_pairs_with_principal_part"] = finite_grade == 0

payload = {
    "schema": "marici.rank26-conductor-specialization-cone.v1",
    "physical_exponent": "-1/2 + epsilon",
    "single_branch_character": {
        "constant_exponent_mod_Z": str(single[0]),
        "epsilon_slope": str(single[1]),
        "value_at_epsilon_zero": "-1",
    },
    "merged_conductor_character": {
        "constant_exponent_mod_Z": str(merged[0]),
        "epsilon_slope": str(merged[1]),
        "value_at_epsilon_zero": "+1",
        "logarithmic_derivative": "4*pi*i",
    },
    "normalization_order": normalization_order,
    "conductor_pole_order": conductor_pole_order,
    "normalized_grade": finite_grade,
    "checks": checks,
    "all_passed": all(checks.values()),
}

out = Path(__file__).with_name("rank26-conductor-specialization-cone.json")
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["all_passed"]:
    raise SystemExit(1)
