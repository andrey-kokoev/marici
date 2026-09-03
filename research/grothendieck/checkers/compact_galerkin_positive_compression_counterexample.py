"""Exact counterexample to positivity certification by unsigned norm tails."""

import json
from fractions import Fraction
from pathlib import Path

M = 6
epsilon = Fraction(1, 1000)
diagonal = [Fraction(1, k) for k in range(1, M + 1)]
diagonal += [-epsilon]
diagonal += [Fraction(1, 2000 + k) for k in range(1, 8)]
compression = diagonal[:M]
tail = diagonal[M:]
tail_norm = max(abs(value) for value in tail)

checks = {
    "finite_compression_positive": min(compression) > 0,
    "full_operator_has_negative_entry": min(diagonal) < 0,
    "tail_norm_equals_epsilon": tail_norm == epsilon,
    "incorrect_bound_would_be_positive": min(compression) - tail_norm > 0,
    "correct_extended_compression_bound_nonpositive": min(Fraction(0), min(compression)) - tail_norm < 0,
}
result = {
    "schema": "marici.grothendieck.compact-galerkin-positive-compression-counterexample.v1",
    "cutoff": M,
    "finite_minimum": str(min(compression)),
    "tail_norm": str(tail_norm),
    "full_minimum": str(min(diagonal)),
    **checks,
    "all_verified": all(checks.values()),
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "compact-galerkin-positive-compression-counterexample.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
