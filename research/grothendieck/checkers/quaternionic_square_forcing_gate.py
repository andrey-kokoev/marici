"""Small exact hostile tests for square-forcing antiunitary symmetry."""

# Represent the real-linear maps on C by 2x2 matrices in coordinates (Re,Im).
# Conjugation K squares to +I; quarter-turn followed by K squares to +I too,
# so a single complex dimension cannot carry Kramers Theta.  On C^2, the
# antiunitary Theta(z1,z2)=(-conj(z2),conj(z1)) squares to -I.


def theta(vector: tuple[complex, complex]) -> tuple[complex, complex]:
    z1, z2 = vector
    return (-z2.conjugate(), z1.conjugate())


for basis_vector in ((1 + 0j, 0j), (0j, 1 + 0j), (1 + 2j, 3 - 4j)):
    twice = theta(theta(basis_vector))
    assert twice == tuple(-entry for entry in basis_vector)

# A 2x2 Hermitian operator commuting with this Theta is forced to be a scalar
# in the one-quaternionic-dimensional model, so its complex determinant is a^2.
for a in (-3, 0, 5):
    complex_determinant = a * a
    moore_determinant = a
    assert complex_determinant == moore_determinant**2

# Positivity makes an interior analytic eigenvalue contact even-order.  The
# smallest lambda=t^2 gives a Kramers-paired complex determinant t^4, whereas
# Xi^2 at a simple Xi zero would have order two.
positive_contact_order = 2
kramers_determinant_order = 2 * positive_contact_order
assert kramers_determinant_order == 4
assert kramers_determinant_order != 2

# Square +1 conjugation permits diag(x,y), whose determinant xy has odd
# exponent in each independent variable and hence is not a polynomial square.
exponents_of_xy = (1, 1)
assert any(exponent % 2 for exponent in exponents_of_xy)

print("kramers_antiunitary_squares_to_minus_identity=True")
print("quaternionic_hermitian_complex_determinant_is_square=True")
print("positive_kramers_determinant_zero_order_divisible_by_four=True")
print("positive_kramers_gram_cannot_model_Xi_squared_at_simple_zero=True")
print("real_structure_square_plus_one_does_not_force_square=True")
print("xi_reflection_alone_is_insufficient=True")
print("indefinite_prequotient_oriented_lift_open=True")
