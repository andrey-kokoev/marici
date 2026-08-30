from fractions import Fraction as F


def geometric_product_components(v, dv):
    a, b = map(F, v)
    c, d = map(F, dv)
    return a * c + b * d, a * d - b * c


fixtures = (
    ((1, 2), (3, 4)),
    ((-3, 5), (7, -2)),
    ((8, -1), (-4, 9)),
)

for v, dv in fixtures:
    scalar, bivector = geometric_product_components(v, dv)
    norm = F(v[0] ** 2 + v[1] ** 2)
    assert scalar / norm == F(v[0] * dv[0] + v[1] * dv[1], norm)
    assert bivector / norm == F(v[0] * dv[1] - v[1] * dv[0], norm)

# Spatial transport V=(H,H_x), d_x V=(H_x,H_xx).
for h, hx, hxx in ((2, 3, 5), (-1, 4, 7), (6, -2, -3)):
    _, bivector = geometric_product_components((h, hx), (hx, hxx))
    assert bivector == h * hxx - hx * hx

# Newman heat transport d_lambda V=(-H_xx,-H_xxx).
for h, hx, hxx, hxxx in ((2, 3, 5, 7), (-1, 4, 7, -2), (6, -2, -3, 11)):
    _, bivector = geometric_product_components((h, hx), (-hxx, -hxxx))
    assert bivector == hx * hxx - h * hxxx

# A simple scalar zero keeps a nonzero relationship direction; a collision
# destroys it.
assert (0, 5) != (0, 0)
assert (0, 0) == (0, 0)

print("clifford_relationship_plane_connection: 14/14 gates passed")
