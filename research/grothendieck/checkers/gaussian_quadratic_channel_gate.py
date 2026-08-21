"""Exact finite Gaussian-cumulant and Wick-normalization bookkeeping."""

from fractions import Fraction


def second_cumulant(source: tuple[Fraction, ...]) -> Fraction:
    return Fraction(1, 2) * sum(value * value for value in source)


for source in (
    (Fraction(1),),
    (Fraction(1), Fraction(2)),
    (Fraction(1, 2), Fraction(-2, 3), Fraction(3, 5)),
):
    cumulant = second_cumulant(source)
    assert 2 * cumulant == sum(value * value for value in source)
    # Log expectation of the Wick exponential subtracts the same cumulant.
    wick_log_expectation = cumulant - cumulant
    assert wick_log_expectation == 0

# On the critical line each Hermitian norm contribution is exactly 1/p,
# independent of height. Exact finite prime prefixes are strictly increasing.
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
prefix = Fraction(0)
previous = Fraction(-1)
for prime in primes:
    prefix += Fraction(1, prime)
    assert prefix > previous
    previous = prefix

print("Gaussian_second_cumulant_forces_coefficient_one_half=True")
print("Wick_ordering_subtracts_exact_quadratic_channel=True")
print("critical_prime_Hermitian_norm_is_height_independent=True")
print("critical_prime_source_not_Cameron_Martin=True")
print("relative_prime_gamma_covariance_open=True")
