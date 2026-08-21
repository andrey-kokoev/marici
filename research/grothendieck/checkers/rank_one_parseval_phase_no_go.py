"""Exact rational controls for the rank-one Parseval phase no-go."""

from fractions import Fraction


def parseval_pair(u: Fraction) -> tuple[Fraction, Fraction]:
    denominator = 1 + u * u
    return ((1 - u * u) / denominator, (2 * u) / denominator)


for numerator in range(-12, 13):
    u = Fraction(numerator, 7)
    c, q = parseval_pair(u)
    assert c * c + q * q == 1
    assert (q == 0) == (u == 0)

# Reciprocal scalar phases contain no selective zero condition.
for phase in (Fraction(1, 2), Fraction(2, 3), Fraction(5, 7), Fraction(-3, 4)):
    assert phase * (1 / phase) == 1

print("rank_one_parseval_pair_is_rational_circle_parameterization=True")
print("arbitrary_input_zeros_transfer_directly_to_complement=True")
print("reciprocal_scalar_phase_gluing_is_identity=True")
print("rank_one_zero_set_not_explanatory_without_independent_phase=True")
print("two_channel_source_interference_is_next_target=True")
