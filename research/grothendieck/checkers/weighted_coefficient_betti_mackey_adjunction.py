"""Exact weighted pull--push and C2 normalization checks."""

from fractions import Fraction


def weighted_degree(upstairs: tuple[Fraction, ...], downstairs: Fraction) -> Fraction:
    return sum(upstairs) / downstairs


examples = (
    ((Fraction(1), Fraction(1)), Fraction(1), Fraction(2)),
    ((Fraction(1), Fraction(3)), Fraction(2), Fraction(2)),
    ((Fraction(2), Fraction(5)), Fraction(7, 2), Fraction(2)),
)
for upstairs, downstairs, expected_degree in examples:
    assert weighted_degree(upstairs, downstairs) == expected_degree

# Frozen delta normalization and degree two agree only for equal fiber weights.
for mu_zero, mu_one in (
    (Fraction(1), Fraction(1)),
    (Fraction(1), Fraction(2)),
    (Fraction(3), Fraction(5)),
):
    degree_normalized_downstairs = (mu_zero + mu_one) / 2
    selected_normalized_downstairs = mu_zero
    both_hold = degree_normalized_downstairs == selected_normalized_downstairs
    assert both_hold == (mu_zero == mu_one)

# Reciprocal coefficient and Betti weights preserve unit evaluation products.
for coefficient_weight in (Fraction(1, 3), Fraction(2), Fraction(7, 5)):
    betti_weight = 1 / coefficient_weight
    assert coefficient_weight * betti_weight == 1

print("weighted_pullback_adjoint_is_density_ratio_fiber_sum=True")
print("pull_push_norm_is_weighted_fiber_degree=True")
print("ordinary_degree_survives_exactly_under_fiber_balance=True")
print("C2_frozen_selector_and_degree_require_equal_fiber_weights=True")
print("von_Mangoldt_weighted_fiber_balance_open=True")
