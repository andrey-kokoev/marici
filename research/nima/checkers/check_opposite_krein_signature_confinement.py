def omega(u, v):
    return u[0] * v[1] - u[1] * v[0]


def signature(u):
    value = 1j * omega(u, tuple(x.conjugate() for x in u))
    assert abs(value.imag) < 1e-12
    return value.real


positive = (1 + 0j, 1j)
negative = (1 + 0j, -1j)
seam = (1 + 0j, 0j)

assert signature(positive) > 0
assert signature(negative) < 0
assert abs(omega(positive, negative)) > 1e-12

assert signature(seam) == 0
assert omega(seam, (2 + 0j, 0j)) == 0

scale = 3 - 2j
scaled_positive = tuple(scale * x for x in positive)
assert abs(signature(scaled_positive) - abs(scale) ** 2 * signature(positive)) < 1e-12

print("opposite Krein signatures forbid proportional boundary traces")
print("symplectic cross zero is genuine two-column rank loss")
print("signature-null seam permits alignment")
