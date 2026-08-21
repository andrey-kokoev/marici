"""Exact Euler-box checks for the incidence-derived Hilbert metric."""

import sympy as sp


def chain_zeta(length: int) -> sp.Matrix:
    return sp.Matrix(length, length, lambda row, col: 1 if col <= row else 0)


def kron_all(matrices: list[sp.Matrix]) -> sp.Matrix:
    result = matrices[0]
    for matrix in matrices[1:]:
        result = sp.kronecker_product(result, matrix)
    return result


for lengths in ([2], [3], [2, 3], [2, 2, 2]):
    chains = [chain_zeta(length) for length in lengths]
    differences = [chain.inv() for chain in chains]
    zeta = kron_all(chains)
    inverse = kron_all(differences)
    metric_factors = [difference.T * difference for difference in differences]
    metric = kron_all(metric_factors)

    assert inverse == zeta.inv()
    assert metric == inverse.T * inverse
    assert zeta.T * metric * zeta == sp.eye(zeta.rows)
    assert all(metric[:index, :index].det() > 0 for index in range(1, metric.rows + 1))
    print(f"chain_lengths={lengths} dimension={zeta.rows} incidence_unitary_in_metric=True")

single_difference = chain_zeta(4).inv()
single_metric = single_difference.T * single_difference
assert single_metric == sp.Matrix([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 1]])

print("one_prime_metric=tridiagonal_discrete_Dirichlet")
print("Euler_tensor_factorization=True")
print("naive_counting_adjoint_repaired=True")
print("infinite_tensor_limit_open=True")
print("physical_relative_chain_pushforward_constructed=False")
