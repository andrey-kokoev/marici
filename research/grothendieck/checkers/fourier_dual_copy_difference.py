"""Exact cyclic-group checks for Fourier-dual copy/difference correspondence."""

import sympy as sp


def check(n: int) -> None:
    omega = {
        2: -sp.Integer(1),
        3: -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2,
        4: sp.I,
    }[n]
    fourier = sp.Matrix(n, n, lambda k, x: omega ** (k * x) / sp.sqrt(n))

    spectral_copy = sp.zeros(n * n, n)
    for k in range(n):
        spectral_copy[k * n + ((-k) % n), k] = 1

    transported = sp.kronecker_product(fourier.conjugate().T, fourier.conjugate().T) * spectral_copy * fourier

    incidence = sp.zeros(n * n, n)
    for a in range(n):
        for b in range(n):
            incidence[a * n + b, (a - b) % n] = 1
    expected = incidence / sp.sqrt(n)

    assert all(sp.simplify(transported[row, col] - expected[row, col]) == 0 for row in range(n * n) for col in range(n))
    assert incidence.T * incidence == n * sp.eye(n)
    assert sp.simplify(expected.T * expected - sp.eye(n)) == sp.zeros(n)
    print(f"cyclic_group_order={n} fiber_size={n} unnormalized_pull_push={n}*I normalized_isometry=True")


for order in (2, 3, 4):
    check(order)

print("spectral_conjugation_copy_dual_to_source_difference=True")
print("kernel_norm_derived_from_fiber_cardinality=True")
print("physical_relative_chain_pushforward_constructed=False")
