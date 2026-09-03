"""Dependency-free scale audit for truncating inverse Gaussian factors."""

import json
import math
from pathlib import Path


WINDOW = 0.8
CLAIMED_MARGIN = 8.9e-18


def l2_tail_fraction(t: float, window: float = WINDOW) -> float:
    """Exact relative squared-L2 mass outside [-window, window]."""
    assert t > 0 and window > 0
    return math.erfc(2 * math.pi * window / math.sqrt(t))


def solve_threshold(target: float) -> float:
    """Largest t for which the exact tail fraction does not exceed target."""
    lo, hi = 1e-6, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if l2_tail_fraction(mid) <= target:
            lo = mid
        else:
            hi = mid
    return lo


threshold = solve_threshold(CLAIMED_MARGIN)
samples = {
    str(t): l2_tail_fraction(t)
    for t in (0.25, 0.5, 0.75, 1.0, 2.0, 4.0)
}

assert l2_tail_fraction(threshold) <= CLAIMED_MARGIN * (1 + 1e-12)
assert l2_tail_fraction(threshold * (1 + 1e-8)) > CLAIMED_MARGIN
assert all(
    l2_tail_fraction(a) < l2_tail_fraction(b)
    for a, b in zip((0.25, 0.5, 0.75, 1.0, 2.0), (0.5, 0.75, 1.0, 2.0, 4.0))
)

# Deliberate failure of a common exponent error: omitting the square in the
# L2 density predicts erfc(sqrt(2)*pi*L/sqrt(t)), not the exact ratio.
wrong_at_one = math.erfc(math.sqrt(2) * math.pi * WINDOW)
assert abs(wrong_at_one - l2_tail_fraction(1.0)) > 1e-8

result = {
    "schema": "marici.gaussian-window-tail-scale.v1",
    "inverse_factor_modulus": "sqrt(2*pi/t)*exp(-2*pi^2*x^2/t)",
    "relative_squared_l2_tail": "erfc(2*pi*L/sqrt(t))",
    "window_half_width": WINDOW,
    "comparison_margin": CLAIMED_MARGIN,
    "largest_t_with_l2_tail_at_most_margin": threshold,
    "sample_tail_fractions": samples,
    "wrong_unsquared_exponent_rejected": True,
    "weil_form_error_bound_proved": False,
    "interpretation": (
        "Necessary scale diagnostic only: an operator/form continuity bound is still "
        "required to compare truncation error with a localized Weil margin."
    ),
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "gaussian-window-tail-scale.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
