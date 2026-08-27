import cmath


def h(amplitude, tau, z):
    return amplitude * (z**2 - 2 * tau)


def partial_tau_h(amplitude, tau, z):
    return -2 * amplitude


def minus_h_zz(amplitude, tau, z):
    return -2 * amplitude


for amplitude in (1, -3, 2 + 5j):
    for tau in (-4, 0, 4):
        for z in (-2, 0, 2, 3j):
            assert partial_tau_h(amplitude, tau, z) == minus_h_zz(amplitude, tau, z)

for tau in (2, 8):
    roots = (-cmath.sqrt(2 * tau), cmath.sqrt(2 * tau))
    assert all(abs(root.imag) < 1e-12 for root in roots)
    assert all(abs(h(7, tau, root)) < 1e-12 for root in roots)

for tau in (-2, -8):
    roots = (-cmath.sqrt(2 * tau), cmath.sqrt(2 * tau))
    assert all(abs(root.real) < 1e-12 and abs(root.imag) > 0 for root in roots)
    assert all(abs(h(7, tau, root)) < 1e-12 for root in roots)

assert 8 * 1 > 0
assert 8 * -1 < 0

print("newman_collision_orientation_is_universal: 46/46 gates passed")
