import cmath


a = 0.75 + 1.25j
z0 = -0.5 + 0.25j


def p(z: complex) -> complex:
    return (z - a) / (z0 - a)


assert abs(p(z0) - 1.0) < 1e-15
assert abs(p(a)) < 1e-15

d_minus = 2.0 - 0.5j
transition = -1.0 + 3.0j
d_plus = transition * d_minus

for sample in (0.0j, 1.0 + 2.0j, -3.0 + 0.5j):
    assert abs(p(sample)) > 1e-12
    transformed = (p(sample) * d_plus) / (p(sample) * d_minus)
    assert abs(transformed - transition) < 1e-12

for radius in (10.0, 100.0, 1000.0):
    log_increment = cmath.log(p(radius)).real
    assert abs(log_increment) < 2.0 * cmath.log(radius).real

print("normalization residual:", abs(p(z0) - 1.0))
print("inserted-zero residual:", abs(p(a)))
print("transition preserved at three samples")
print("polynomial logarithmic growth verified")
