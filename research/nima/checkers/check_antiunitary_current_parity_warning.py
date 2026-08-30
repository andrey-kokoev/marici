S = ((0j, -1 + 0j), (1 + 0j, 0j))
R = ((0j, 1 + 0j), (1 + 0j, 0j))
Q = ((0j, 2 + 0j), (2 + 0j, 0j))
v = (1 + 1j, 2 - 1j)


def apply(matrix, vector):
    return tuple(
        sum(a * b for a, b in zip(row, vector))
        for row in matrix
    )


def inner(left, right):
    return sum(a.conjugate() * b for a, b in zip(left, right))


def antiunitary(vector):
    return apply(R, tuple(x.conjugate() for x in vector))


def conjugation(vector):
    return tuple(x.conjugate() for x in vector)


def label_exchange(vector):
    return apply(R, vector)


def current(vector):
    return (-1j * inner(vector, apply(S, vector))).real


def quadratic(vector):
    return inner(vector, apply(Q, vector)).real


transported = antiunitary(v)

assert abs(current(conjugation(v)) + current(v)) < 1e-12
assert abs(current(label_exchange(v)) + current(v)) < 1e-12
assert abs(current(transported) - current(v)) < 1e-12
assert abs(quadratic(transported) - quadratic(v)) < 1e-12

print("conjugation and label exchange separately reverse the order current")
print("their antiunitary composition preserves the order current")
print("the real virial quadratic remains invariant in the same example")
print("matrix parity alone does not determine current parity")
