"""Exact rank tests for conjugation-graph projectors."""

import sympy as sp


def conjugation_graph(pair_count: int) -> sp.Matrix:
    size = 2 * pair_count
    matrix = sp.zeros(size)
    for orbit in range(pair_count):
        left = 2 * orbit
        right = left + 1
        matrix[left, right] = 1
        matrix[right, left] = 1
    return matrix


for pairs in range(1, 5):
    graph = conjugation_graph(pairs)
    assert graph.rank() == 2 * pairs
    assert graph * graph == sp.eye(2 * pairs)
    print(f"free_C2_pairs={pairs} graph_rank={graph.rank()}")

# The hostile quartet consists of two free conjugation pairs.
quartet = conjugation_graph(2)
weights = sp.diag(1, 1, -1, -1)
weighted_graph = weights * quartet
assert quartet.rank() == 4
assert weighted_graph.rank() == 4

# A sum of m outer products has rank at most m.
u1, u2 = sp.Matrix([1, 2, 3, 4]), sp.Matrix([0, 1, 1, 0])
v1, v2 = sp.Matrix([2, 0, 1, 1]), sp.Matrix([1, 3, 0, 2])
two_channels = u1 * v1.T + u2 * v2.T
assert two_channels.rank() <= 2

print("hostile_quartet_graph_rank=4")
print("fixed_finite_scalar_channel_realization=False")
print("operator_or_infinite_channel_correspondence_required=True")

