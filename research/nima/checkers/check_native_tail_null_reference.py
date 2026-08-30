def omega(u, v):
    return u[0] * v[1] - u[1] * v[0]


def signature(u):
    value = 1j * omega(u, tuple(x.conjugate() for x in u))
    assert abs(value.imag) < 1e-12
    return value.real


X = 2 + 3j
moving = (X, 1 + 0j)
endpoint = (0j, 1 + 0j)

assert omega(moving, endpoint) == X
assert signature(endpoint) == 0
assert signature(moving) == -2 * X.imag

zero_moving = (0j, 1 + 0j)
assert omega(zero_moving, endpoint) == 0

print("native tail readout is a genuine symplectic determinant")
print("fixed endpoint reference line is Krein-null")
print("moving-line signature is exactly scalar imaginary-part orientation")
