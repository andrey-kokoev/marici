#!/usr/bin/env python3
"""Character factorization for the canonical orientation of null infinity."""

import json
from pathlib import Path


# Characters are ordered (P,T).
chi_generator = (+1, -1)  # P: u fixed; T: v=-u.
chi_celestial = (-1, +1)  # P: antipodal degree -1; T: direction fixed.
chi_boundary = tuple(a * b for a, b in zip(chi_generator, chi_celestial))
chi_carrier_polarity = (-1, -1)

assert chi_boundary == (-1, -1)
assert chi_boundary == chi_carrier_polarity
assert tuple(a * b for a, b in zip(chi_boundary, chi_celestial)) == chi_generator

result = {
    "status": "PASS",
    "generator_orientation_character_P_T": chi_generator,
    "celestial_orientation_character_P_T": chi_celestial,
    "null_boundary_orientation_character_P_T": chi_boundary,
    "carrier_polarity_character_P_T": chi_carrier_polarity,
    "character_identity": "chi_boundary = chi_generator * chi_celestial",
    "candidate_comparison": "L_pol -> Or(I)",
    "typing_status": "character_compatible_comparison_not_yet_constructed",
}

out = Path(__file__).resolve().parents[1] / "results" / "null_infinity_orientation_factorization.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
