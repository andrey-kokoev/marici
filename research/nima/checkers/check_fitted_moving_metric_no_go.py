from math import exp


def diagonal_product(*matrices):
    size = len(matrices[0])
    return tuple(
        tuple(
            (
                0.0
                if i != j
                else __import__("math").prod(matrix[i][i] for matrix in matrices)
            )
            for j in range(size)
        )
        for i in range(size)
    )


for t in [0.0, 0.5, 1.0, 2.0]:
    phi = ((exp(t), 0.0), (0.0, exp(-t)))
    q = ((exp(-2 * t), 0.0), (0.0, exp(2 * t)))
    transported = diagonal_product(phi, q, phi)
    assert abs(transported[0][0] - 1.0) < 1e-12
    assert abs(transported[1][1] - 1.0) < 1e-12
    assert q[0][0] > 0 and q[1][1] > 0

assert exp(2.0) > 1
assert exp(-2.0) < 1

print("hyperbolic flow expands and contracts in the fixed metric")
print("a fitted moving positive metric makes it exactly isometric")
print("moving-metric existence alone has no confinement content")
