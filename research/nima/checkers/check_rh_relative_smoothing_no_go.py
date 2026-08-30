from fractions import Fraction
import json
from pathlib import Path


cutoffs = list(range(1, 13))
smallest_smoothing = [Fraction(1, 2**n) for n in cutoffs]
assert all(x > 0 for x in smallest_smoothing)
assert all(
    smallest_smoothing[i + 1] < smallest_smoothing[i]
    for i in range(len(smallest_smoothing) - 1)
)

# For diagonal K_N with entries 2^-1 through 2^-N, I+K_N is bounded below
# by 1 uniformly.
smallest_identity_relative = [
    min(Fraction(1) + Fraction(1, 2**k) for k in range(1, n + 1))
    for n in cutoffs
]
assert all(x >= 1 for x in smallest_identity_relative)

# A source-relative eigenvalue -1 gives one isolated crossing.
relative_eigenvalues_regular = [Fraction(-1, 2), Fraction(1, 3), Fraction(1, 5)]
relative_eigenvalues_crossing = [Fraction(-1), Fraction(1, 3), Fraction(1, 5)]
det_regular = Fraction(1)
det_crossing = Fraction(1)
for value in relative_eigenvalues_regular:
    det_regular *= 1 + value
for value in relative_eigenvalues_crossing:
    det_crossing *= 1 + value
assert det_regular != 0
assert det_crossing == 0

result = {
    "cutoffs": cutoffs,
    "smoothing_smallest_values": [str(x) for x in smallest_smoothing],
    "every_finite_smoothing_cutoff_injective": True,
    "uniform_smoothing_lower_bound": False,
    "identity_relative_lower_bound": "1",
    "regular_relative_determinant": str(det_regular),
    "crossing_relative_determinant": str(det_crossing),
    "crossing_eigenvalue": "-1",
    "verdict": "theta smoothing must be relative to an isometric or Fredholm principal transport",
}

out = Path(__file__).parents[1] / "results" / "rh-relative-smoothing-no-go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
