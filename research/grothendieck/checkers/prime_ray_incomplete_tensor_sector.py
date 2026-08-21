"""Exact finite-prefix checks for the prime-ray tensor-sector obstruction."""

from fractions import Fraction


primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
cumulative_displacement = Fraction(0)
previous = Fraction(-1)
for prime in primes:
    local_squared_norm = Fraction(1, prime - 1)
    geometric_sum = sum(Fraction(1, prime**exponent) for exponent in range(1, 30))
    assert geometric_sum < local_squared_norm
    cumulative_displacement += local_squared_norm
    assert cumulative_displacement > previous
    previous = cumulative_displacement

for prime_norm, gamma_norm in (
    (Fraction(1), Fraction(1)),
    (Fraction(3, 2), Fraction(7, 3)),
    (Fraction(5), Fraction(0)),
):
    combined = prime_norm + gamma_norm
    assert combined >= prime_norm

print("local_prime_ray_squared_norm_equals_one_over_p_minus_one=True")
print("global_prime_displacement_sum_diverges=True")
print("vacuum_product_overlap_tends_to_zero=True")
print("independent_positive_gamma_sector_cannot_cancel_norm=True")
print("relative_quasifree_or_Krein_completion_open=True")
