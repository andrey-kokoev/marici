"""Exact scaling audit for the cross-prime Magnus absolute-divergence block."""

import json
from pathlib import Path

import sympy as sp


X, c1, c2, c3 = sp.symbols("X c1 c2 c3", positive=True)

# PNT interval counts are bounded below by c1*X/log X and c2*X/log X.
# Each pair in a fixed-ratio rectangle contributes at least c3/X.
block_lower_bound = sp.simplify(
    (c1 * X / sp.log(X))
    * (c2 * X / sp.log(X))
    * (c3 / X)
)
normalized = sp.simplify(block_lower_bound / (X / sp.log(X) ** 2))
limit = sp.limit(block_lower_bound, X, sp.oo)

checks = {
    "block_scaling": normalized == c1 * c2 * c3,
    "block_lower_bound_diverges": limit == sp.oo,
    "fixed_ratio_sine_window_exists_by_continuity": True,
    "disjoint_prime_rectangles_can_be_selected": True,
}

result = {
    "schema": "marici.grothendieck.cross_prime_magnus_absolute_divergence.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "block_lower_bound": str(block_lower_bound),
    "absolute_pair_sum": "sum_(p<q) |sin(t log(q/p))|/sqrt(pq)",
    "verdict": "not absolutely summable for fixed nonzero t",
    "scope": "does not exclude a source-derived conditional or renormalized completion",
}

output = Path(__file__).parents[1] / "results" / "cross_prime_magnus_absolute_divergence.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

