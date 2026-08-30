import cmath


def base_increment(z: complex, root: complex) -> complex:
    return (z - root) / (-root)


z_star = 0.0j
p_root = 1.0 + 0.5j
q_root = -0.5 + 1.25j


def c_x_p(z: complex) -> complex:
    return base_increment(z, p_root)


def c_x_q(z: complex) -> complex:
    return base_increment(z, q_root)


def c_xp_q(z: complex) -> complex:
    return c_x_q(z)


def c_xq_p(z: complex) -> complex:
    return c_x_p(z)


for sample in (z_star, 0.2 + 0.3j, -0.7 + 0.1j):
    holonomy = c_xp_q(sample) * c_x_p(sample) / (
        c_xq_p(sample) * c_x_q(sample)
    )
    assert abs(holonomy - 1.0) < 1e-12

phase = cmath.exp(0.37j)


def hostile_xp_q(z: complex) -> complex:
    return phase * c_xp_q(z)


hostile_values = []
for sample in (z_star, 0.2 + 0.3j, -0.7 + 0.1j):
    holonomy = hostile_xp_q(sample) * c_x_p(sample) / (
        c_xq_p(sample) * c_x_q(sample)
    )
    hostile_values.append(holonomy)
    assert abs(holonomy - phase) < 1e-12

assert abs(hostile_values[0] - 1.0) > 0.1
assert max(abs(value - hostile_values[0]) for value in hostile_values) < 1e-12

print("normalized addition square has identity holonomy")
print("hostile square has spectrally constant phase:", hostile_values[0])
print("logarithmic connection cannot detect that constant phase")
print("basepoint normalization rejects it")
