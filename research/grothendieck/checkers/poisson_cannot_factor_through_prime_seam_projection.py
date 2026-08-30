import json
from pathlib import Path

import sympy as sp


# Minimal typed model: the first coordinate is visible at arithmetic seams;
# the second is a continuum variation supported in an unsampled gap.
S = sp.Matrix([[1, 0]])
P = sp.Matrix([[0, 1]])
bump = sp.Matrix([0, 1])
a = sp.symbols("a")

checks = {
    "gap_variation_is_sampling_invisible": S * bump == sp.zeros(1, 1),
    "gap_variation_is_poisson_relevant": P * bump != sp.zeros(1, 1),
    "poisson_does_not_factor_through_sampling": sp.solve(list(P - sp.Matrix([[a]]) * S), [a], dict=True) == [],
    "sampling_kernel_not_in_poisson_kernel": any(P * vector != sp.zeros(1, 1) for vector in S.nullspace()),
}

result = {
    "schema": "marici.grothendieck.poisson-cannot-factor-through-prime-seam-projection.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "A continuum variation can be invisible to prime-seam sampling while remaining visible to the full source correspondence. Therefore global Poisson sewing cannot be reconstructed from the arithmetic projection.",
}

out = Path(__file__).parents[1] / "results" / "poisson_cannot_factor_through_prime_seam_projection.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
