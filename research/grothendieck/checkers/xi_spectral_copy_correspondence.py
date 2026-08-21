"""Exact matrix checks for the conjugation-twisted copy correspondence."""

import sympy as sp


def copy_matrix(pair_count: int) -> sp.Matrix:
    n = 2 * pair_count
    matrix = sp.zeros(n * n, n)
    for orbit in range(pair_count):
        left = 2 * orbit
        right = left + 1
        matrix[left * n + right, left] = 1
        matrix[right * n + left, right] = 1
    return matrix


for pairs in range(1, 4):
    n = 2 * pairs
    copy = copy_matrix(pairs)
    graph_projection = copy * copy.T
    assert copy.T * copy == sp.eye(n)
    assert graph_projection**2 == graph_projection
    assert graph_projection.rank() == n
    print(f"free_C2_pairs={pairs} copy_isometry=True graph_projection_rank={n}")

# J alone does not choose a copy basis: a non-permutation real rotation
# changes the diagonal/copy projector.
root_two = sp.sqrt(2)
rotation = sp.Matrix([[1, 1], [-1, 1]]) / root_two
plain_copy = sp.zeros(4, 2)
plain_copy[0, 0] = 1
plain_copy[3, 1] = 1
rotated_copy = sp.kronecker_product(rotation, rotation) * plain_copy * rotation.T
assert sp.simplify(rotated_copy * rotated_copy.T - plain_copy * plain_copy.T) != sp.zeros(4)

print("copy_adjoint_copy=I")
print("copy_copy_adjoint=P_graph")
print("real_structure_alone_selects_copy_basis=False")
print("atomic_Frobenius_structure_required=True")
print("physical_relative_chain_pushforward_constructed=False")

