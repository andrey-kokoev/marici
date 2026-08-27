def q(r, w):
    return (((w - r) ** 2 + 1) * ((w + r) ** 2 + 1)) / r**4


def compact_error_bound(r, radius):
    return 2 * (1 + radius**2) / r**2 + (radius**2 + 1) ** 2 / r**4


for r in (10, 100, 1000):
    roots = (r + 1j, r - 1j, -r + 1j, -r - 1j)
    assert all(abs(q(r, root)) < 1e-20 for root in roots)
    assert q(r, 2) == q(r, -2)
    assert compact_error_bound(r, 3) > 0

assert compact_error_bound(1000, 3) < compact_error_bound(100, 3)
assert compact_error_bound(100, 3) < compact_error_bound(10, 3)
assert compact_error_bound(10**6, 3) < 3e-11

print("symmetric_divisor_escape_at_infinity: 12/12 gates passed")
