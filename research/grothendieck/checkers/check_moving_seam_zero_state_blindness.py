"""Exact moving-seam common/relative channel audit."""

from fractions import Fraction
import json


# A finite exact trajectory with r=2 and zero completed total.
cuts = [Fraction(0), Fraction(1), Fraction(2), Fraction(3)]
r = Fraction(2)
T = [Fraction(6) - r * L for L in cuts]
B = [-Fraction(6) + r * L for L in cuts]
C = [t + b for t, b in zip(T, B)]
D = [t - b for t, b in zip(T, B)]

checks = {
    "zero_total_at_every_cut": all(x == 0 for x in C),
    "nonzero_zero_state_trajectory": any(t != 0 or b != 0 for t, b in zip(T, B)),
    "anti_diagonal_at_every_cut": all(b == -t for t, b in zip(T, B)),
    "relative_channel_detects_trajectory": any(x != 0 for x in D),
    "common_quadratic_energy_is_zero": all(x * x == 0 for x in C),
    "faithful_seam_energy_is_positive_somewhere": any(t * t + b * b > 0 for t, b in zip(T, B)),
    "flow_is_oppositely_oriented": all(
        T[i + 1] - T[i] == -(B[i + 1] - B[i])
        for i in range(len(cuts) - 1)
    ),
}

result = {
    "schema": "marici.grothendieck.moving-seam-zero-state-blindness.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "trajectory": [
        {"L": str(L), "T": str(t), "B": str(b), "C": str(c), "D": str(d)}
        for L, t, b, c, d in zip(cuts, T, B, C, D)
    ],
}

print(json.dumps(result, indent=2, sort_keys=True))
