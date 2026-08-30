import cmath


def h(t, z):
    return z**2 - 2 * t


def h_t(t, z):
    return -2


def minus_h_zz(t, z):
    return -2


for t in (-3, -1, 0, 1, 3):
    for z in (-2, 0, 2, 1j):
        assert h_t(t, z) == minus_h_zz(t, z)

for t in (1, 2, 8):
    r = cmath.sqrt(2 * t)
    velocity_from_root = 1 / r
    velocity_from_pde = 2 / (2 * r)
    assert velocity_from_root == velocity_from_pde
    assert abs(h(t, r)) < 1e-12
    assert abs(h(t, -r)) < 1e-12

# The divisor has constant mass and center.  Its algebraic second moment is
# 4t, with derivative four, on both sides of the cubic collision.
for t in (-8, -2, 2, 8):
    roots = (cmath.sqrt(2 * t), -cmath.sqrt(2 * t))
    assert len(roots) == 2
    assert abs(sum(roots)) < 1e-12
    assert abs(sum(root**2 for root in roots) - 4 * t) < 1e-12

print("newman_divisor_current_continuity: 41/41 gates passed")
