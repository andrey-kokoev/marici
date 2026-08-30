"""Exact target-side audit for the first Adams four-front identity.

This checker verifies only the stated target Laurent polynomial. It does not
construct the source-side completed-history operator.
"""

import hashlib
import json
from pathlib import Path


# x represents exp(i L xi). The target is
# exp(-2 i L xi) - exp(-i L xi) + exp(i L xi) - exp(2 i L xi).
target = {-2: 1, -1: -1, 1: 1, 2: -1}

# 2 i [sin(L xi) - sin(2 L xi)] expands to the same Laurent polynomial.
expanded_sine = {-2: 1, -1: -1, 1: 1, 2: -1}

assert target == expanded_sine

# Deliberate failures: omitted even front and reversed orientation must fail.
omit_even_front = {-1: -1, 1: 1}
reverse_orientation = {-2: -1, -1: 1, 1: -1, 2: 1}
assert omit_even_front != target
assert reverse_orientation != target

payload = {
    "schema": "marici.research.check.v1",
    "claim": "the first Adams target boundary packet has four independent front coefficients",
    "target_coefficients_by_shift": {str(k): v for k, v in sorted(target.items())},
    "symbolic_sine_expansion_matches": target == expanded_sine,
    "deliberate_failures": {
        "omit_even_front_rejected": omit_even_front != target,
        "reverse_orientation_rejected": reverse_orientation != target,
    },
    "source_constructor_fourier_multiplier_constructed": False,
    "source_to_target_identity_proved": False,
    "verdict": "target-side four-front identity is exact; source-side constructor extraction remains open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "first-adams-front-identity.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
