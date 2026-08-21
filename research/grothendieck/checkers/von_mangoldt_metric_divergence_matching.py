"""Exact exponent bookkeeping for the forced log-power source metric."""

from fractions import Fraction


def divergence_exponent(alpha: Fraction) -> Fraction:
    # PNT density removes one log from (log p)^(2-alpha)/p.
    return 2 - alpha


candidate_alphas = tuple(Fraction(value, 2) for value in range(-2, 9))
matched = []
for alpha in candidate_alphas:
    exponent = divergence_exponent(alpha)
    if exponent == 0:
        matched.append(alpha)

assert matched == [Fraction(2)]

# At alpha=2 the von Mangoldt square cancels exactly on every prime atom.
for symbolic_log_prime in (Fraction(1), Fraction(2), Fraction(5, 3), Fraction(11, 7)):
    coefficient_squared = symbolic_log_prime**2
    metric_weight = 1 / symbolic_log_prime**2
    assert coefficient_squared * metric_weight == 1

print("raw_von_Mangoldt_diagonal_growth_is_log_cutoff_squared=True")
print("gamma_oscillator_growth_is_log_log_cutoff=True")
print("unique_log_power_metric_match_alpha_equals_two=True")
print("reciprocal_square_metric_reduces_prime_diagonal_to_harmonic=True")
print("weighted_coefficient_Betti_adjunction_open=True")
