"""Exact symbolic audit of the pure Gaussian readout map."""

import json
from fractions import Fraction
from pathlib import Path


def inverse(p: Fraction, s: Fraction) -> tuple[Fraction, Fraction]:
    occupation = (p * p + s * s) / (2 * s + 1)
    return occupation, s - occupation


# Exact rational audit over a bounded grid in the physical half-plane.
tested = 0
for p_num in range(-8, 9):
    for s_num in range(-3, 13):
        p = Fraction(p_num, 4)
        s = Fraction(s_num, 4)
        if s <= Fraction(-1, 2):
            continue
        nu, y = inverse(p, s)
        assert p * p + y * y == nu * (nu + 1)
        assert nu >= 0
        assert s == nu + y
        tested += 1

# Thermal points have distinct pure preimages whenever n>0.
thermal_tests = 0
for n_num in range(1, 17):
    n = Fraction(n_num, 4)
    pure_nu, pure_y = inverse(Fraction(0), n)
    assert pure_nu == n * n / (2 * n + 1)
    assert pure_y == n * (n + 1) / (2 * n + 1)
    assert pure_y * pure_y == pure_nu * (pure_nu + 1)
    assert pure_nu != n
    thermal_tests += 1

packet = {
    "schema": "marici.pure-squeezed-readout-injectivity.v1",
    "purity_equation": "P^2 + (S-nu)^2 = nu(nu+1)",
    "reduced_identity": "P^2+S^2=(2S+1)nu",
    "inverse_nu": "(P^2+S^2)/(2S+1)",
    "inverse_Y": "S-(P^2+S^2)/(2S+1)",
    "exact_rational_samples": tested,
    "thermal_point_pure_preimage": {
        "nu": "n^2/(2n+1)",
        "Y": "n(n+1)/(2n+1)",
        "exact_rational_samples": thermal_tests,
    },
    "conclusion": {
        "pure_locus": "bijective onto S > -1/2 (vacuum phase identified)",
        "full_positive_gaussian_space": "not injective",
        "thermal_vs_pure": "same readout for n > 0, distinct covariance states",
    },
}

out = Path(__file__).parent / "results" / "pure-squeezed-readout-injectivity.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
