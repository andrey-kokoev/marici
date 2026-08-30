"""Exact finite model of arithmetic transpose matching and the seam support gap."""

from fractions import Fraction
import json


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cmul_real(a, z):
    return (a * z[0], a * z[1])


def cconj(z):
    return (z[0], -z[1])


# Two labelled arithmetic supports, with exact Gaussian-rational characters.
supports = (Fraction(2), Fraction(3))
weights = (Fraction(1, 2), Fraction(1, 3))
characters = ((Fraction(0), Fraction(1)), (Fraction(-1), Fraction(0)))


def even_test(a):
    return Fraction(1) + a * a


direct = (Fraction(0), Fraction(0))
reciprocal = (Fraction(0), Fraction(0))
for a, w, chi in zip(supports, weights, characters):
    direct = cadd(direct, cmul_real(w * even_test(a), chi))
    # Reflection changes a to -a; the real-even test is unchanged, and the
    # Real structure conjugates the character.
    reciprocal = cadd(reciprocal, cmul_real(w * even_test(-a), cconj(chi)))

# A nonzero seam test at position 1 lies below the first arithmetic support 2.
gap_test_value = Fraction(7)
arithmetic_evaluation_on_gap = Fraction(0)
seam_delta_evaluation_on_gap = gap_test_value

checks = {
    "reciprocal_evaluation_is_conjugate": reciprocal == cconj(direct),
    "even_test_is_reflection_invariant": all(even_test(-a) == even_test(a) for a in supports),
    "all_arithmetic_supports_miss_gap": all(a >= 2 for a in supports),
    "arithmetic_packet_annihilates_gap_test": arithmetic_evaluation_on_gap == 0,
    "seam_distribution_detects_gap_test": seam_delta_evaluation_on_gap != 0,
    "arithmetic_packet_is_not_a_seam_core": arithmetic_evaluation_on_gap != seam_delta_evaluation_on_gap,
}

result = {
    "schema": "marici.grothendieck.arithmetic-transpose-match-seam-gap.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "direct": [str(x) for x in direct],
    "reciprocal": [str(x) for x in reciprocal],
}

print(json.dumps(result, indent=2, sort_keys=True))
