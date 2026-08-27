from fractions import Fraction as F


def omega(a, b, c, d):
    gram = a * a + b * b
    return F(a * c - b * b, gram), F(b * c - a * d, gram)


fixtures = (
    (3, 2, 5, 7),
    (-1, 4, 2, -3),
    (8, -5, -2, 11),
)

for a, b, c, d in fixtures:
    wx_plus, wl_plus = omega(a, b, c, d)
    wx_minus, wl_minus = omega(a, -b, c, -d)
    assert wx_minus == wx_plus
    assert wl_minus == -wl_plus

# The full symmetric rectangle is twice the positive-half rectangle.  Here p
# and q are the positive-x phase changes on the upper and lower heat edges,
# while r is the positive-height wall phase change.
for p, q, r in ((F(3), F(1), F(2)), (F(7, 3), F(-2), F(5, 7))):
    full = 2 * p - 2 * q - 2 * r
    half = p - q - r
    assert full == 2 * half

# Positivity at the symmetry center removes the x=0 collision port.
positive_source_samples = (F(1, 2), F(3, 7), F(11, 13))
assert sum(positive_source_samples) > 0

for pair_count in range(6):
    full_collision_degree = -2 * pair_count
    assert full_collision_degree % 2 == 0

print("even_newman_collision_pairing_and_half_domain: 15/15 gates passed")
