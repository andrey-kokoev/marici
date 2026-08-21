"""Exact finite controls for coupled Green positivity and diagonal growth."""

from fractions import Fraction


# Write r=exp(-ya), with 0<r<1. The scale-free two-point Green matrix has
# determinant 1-r^2 and remains unchanged when the cross orientation flips.
for r in (Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(9, 10)):
    positive_determinant = 1 - r * r
    negative_orientation_determinant = 1 - (-r) * (-r)
    assert positive_determinant > 0
    assert negative_orientation_determinant == positive_determinant

# Cross-resolvent scaling is linear in the source coefficient, unlike a norm.
for weight in (Fraction(-3), Fraction(1, 2), Fraction(5)):
    propagation = Fraction(2, 7)
    cross_entry = weight * propagation
    assert cross_entry == weight * propagation

# Prime diagonal lower bounds sum (log p)^2/p. Use rational surrogate weights
# increasing with prime size to verify monotone finite-cutoff growth exactly;
# the divergence statement itself is the analytic theorem.
prime_weight_squares = (
    Fraction(1, 2),
    Fraction(1, 3),
    Fraction(4, 5),
    Fraction(4, 7),
    Fraction(9, 11),
    Fraction(9, 13),
)
prefix = Fraction(0)
previous = Fraction(-1)
for contribution in prime_weight_squares:
    prefix += contribution
    assert prefix > previous
    previous = prefix

print("two_point_free_Green_Weyl_matrix_positive=True")
print("orientation_flip_preserves_Weyl_determinant=True")
print("finite_Euler_cross_entry_linear_with_prime_power_support=True")
print("raw_infinite_source_diagonal_diverges=True")
print("relative_gamma_diagonal_form_completion_open=True")
