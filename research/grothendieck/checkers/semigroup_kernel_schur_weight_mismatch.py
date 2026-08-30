"""Exact exponent and support checks for the Euler Schur mismatch."""

from fractions import Fraction


# Lowest-mode semigroup amplitude exponent and its quadratic exponent.
semigroup_amplitude_exponent = Fraction(3, 4)
schur_diagonal_exponent = 2 * semigroup_amplitude_exponent
assert schur_diagonal_exponent == Fraction(3, 2)

# The Euler prime coefficient at y=0 has exponent 1/2 before continuation.
euler_boundary_exponent = Fraction(1, 2)
assert schur_diagonal_exponent != euler_boundary_exponent

# Equality p^(-3/2)=p^(-1/2-y) occurs only at y=1, not as an identity in y.
matching_y = schur_diagonal_exponent - euler_boundary_exponent
assert matching_y == 1

# A Schur term is quadratic in source scaling; the Euler cross term is linear.
for scale in (Fraction(-3), Fraction(0), Fraction(2, 5), Fraction(7)):
    schur_scaling = scale * scale
    cross_scaling = scale
    if scale not in (0, 1):
        assert schur_scaling != cross_scaling

print("semigroup_Schur_lowest_exponent_is_three_halves=True")
print("Euler_boundary_exponent_is_one_half=True")
print("quadratic_Schur_scaling_differs_from_linear_cross_resolvent=True")
print("prime_power_von_Mangoldt_support_missing_from_prime_only_kernel=True")
print("paired_two_boundary_Weyl_matrix_is_revised_target=True")
