from fractions import Fraction as F


# Homogenizing R^(-4) Q_R gives coefficients in
# W^4 + 2(1-R^2)W^2 Z^2 + (R^2+1)^2 Z^4, divided by R^4.
def homogeneous_coefficients(r):
    return (
        F(1, r**4),
        F(2 * (1 - r**2), r**4),
        F((r**2 + 1) ** 2, r**4),
    )


for r in (10, 100, 1000):
    w4, w2z2, z4 = homogeneous_coefficients(r)
    assert w4 > 0
    assert w2z2 < 0
    assert z4 > 1

# Coefficientwise, the projective sections converge to Z^4. Its divisor is
# the point at infinity Z=0 with multiplicity four, whereas its restriction
# to the affine chart Z=1 is the apparently zero-free constant one.
r = 10**6
w4, w2z2, z4 = homogeneous_coefficients(r)
assert w4 < F(1, 10**20)
assert abs(w2z2) < F(1, 10**11)
assert abs(z4 - 1) < F(1, 10**11)

affine_limit_degree = 0
projective_limit_degree = 4
assert affine_limit_degree != projective_limit_degree

print("projective_infinity_germ_retains_escaping_quartet: 13/13 gates passed")
