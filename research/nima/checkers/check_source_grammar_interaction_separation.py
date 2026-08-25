from itertools import combinations


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


q_positive = [[1, 0], [0, 1]]
q_indefinite = [[1, 2], [2, 1]]
interaction_kernel = [[0, 2], [2, 0]]
swap = [[0, 1], [1, 0]]

assert [q_positive[i][i] for i in range(2)] == [
    q_indefinite[i][i] for i in range(2)
]
assert sum(q_positive[i][i] for i in range(2)) == sum(
    q_indefinite[i][i] for i in range(2)
)
assert determinant_2x2(q_positive) == 1
assert determinant_2x2(q_indefinite) == -3
assert [
    [q_indefinite[i][j] - q_positive[i][j] for j in range(2)]
    for i in range(2)
] == interaction_kernel


def multiply(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


assert multiply(swap, q_positive) == multiply(q_positive, swap)
assert multiply(swap, q_indefinite) == multiply(q_indefinite, swap)

negative_witness = [1, -1]
negative_value = sum(
    negative_witness[i] * q_indefinite[i][j] * negative_witness[j]
    for i in range(2)
    for j in range(2)
)
assert negative_value == -2

# Kitaev: equal scalar size, different compositional packets.
kitaev_left = (282, 0, 180, 0)
kitaev_right = (242, 0, 220, 0)
assert sum(kitaev_left) == sum(kitaev_right) == 462
assert kitaev_left != kitaev_right

# Strominger: identical quorum geometry, safety changes with fault grammar.
replicas = {"r1", "r2", "r3"}
quorums = [set(pair) for pair in combinations(sorted(replicas), 2)]
minimum_overlap = min(len(left & right) for left, right in combinations(quorums, 2))
assert minimum_overlap == 1
crash_safe = minimum_overlap >= 1
byzantine_safe_f1 = minimum_overlap > 1
assert crash_safe and not byzantine_safe_f1

print(
    {
        "status": "passed",
        "matrix_falsifier": {
            "same_diagonal": [1, 1],
            "same_trace": 2,
            "positive_determinant": 1,
            "indefinite_determinant": -3,
            "negative_witness_value": negative_value,
            "swap_symmetric": True,
        },
        "kitaev": {
            "same_scalar_dimension": 462,
            "packets_distinct": True,
        },
        "strominger": {
            "minimum_overlap": minimum_overlap,
            "crash_safe": crash_safe,
            "byzantine_f1_safe": byzantine_safe_f1,
        },
        "theorem": "source_grammar_does_not_orient_uncontrolled_completion",
    }
)
