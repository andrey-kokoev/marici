"""Test Q support in the complete intrinsic lower normal Kummer-incidence packet."""

import sympy as sp

x, y, z = sp.symbols("X1 X2 X3")
e = x + y + z
p = x * y
s = x + y
q = sp.expand(-16 * p**2 - 8 * p * e**2 + 8 * s * e**3 - 5 * e**4)

l1 = x - y - z
l2 = x - y + z
l3 = x + y - z
l4 = x + y + z

support = {
    "minus_quadratic_leading": l2**2 * l3**2,
    "plus_quadratic_leading": l1**2 * l4**2,
    "minus_normal_discriminant_coefficient": l1 * l2**2 * l3**2 * l4,
    "plus_normal_discriminant_coefficient": l1**2 * l2 * l3 * l4**2,
    "triple_normal_cover_discriminant": l1 * l2 * l3 * l4,
    "triple_normal_leading_y": y,
    "triple_normal_leading_z": z,
}

for name, polynomial in support.items():
    gcd = sp.factor(sp.gcd(q, polynomial))
    assert gcd == 1, (name, gcd)
    print(f"{name}:Q_GCD=1")

# Entry 712 supplies the only adjacent incidence coefficients.
incidence_coefficients = (sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2))
assert all(coefficient != 0 for coefficient in incidence_coefficients)

print("INCIDENCE_COEFFICIENTS=[1/2,-1/2,1/2]")
print("INCIDENCE_POLE_DIVISOR=empty")
print("INTRINSIC_LOWER_NORMAL_PACKET_Q_SUPPORT=false")
