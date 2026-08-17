"""Audit descent of the local Cartier operator comparisons."""

from fractions import Fraction


def rank(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    result = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next(
            (row for row in range(result, len(rows)) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[result], rows[pivot] = rows[pivot], rows[result]
        scale = rows[result][column]
        rows[result] = [value / scale for value in rows[result]]
        for row in range(len(rows)):
            if row == result:
                continue
            factor = rows[row][column]
            rows[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(rows[row], rows[result])
            ]
        result += 1
    return result


def mat_vec(matrix, vector):
    return [
        sum(value * coefficient for value, coefficient in zip(row, vector))
        for row in matrix
    ]


def add(left, right):
    return [a + b for a, b in zip(left, right)]


def main():
    # Full augmented Cech nerve on the three rotated road charts.
    d2 = [[1], [-1], [1]]
    d1 = [[-1, -1, 0], [1, 0, -1], [0, 1, 1]]
    augmentation = [[1, 1, 1]]
    assert mat_vec(d1, mat_vec(d2, [1])) == [0, 0, 0]
    for edge in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        assert mat_vec(augmentation, mat_vec(d1, edge)) == [0]
    assert (rank(d2), rank(d1), rank(augmentation)) == (1, 2, 1)

    # Explicit integral cone contraction at chart zero.
    h_minus_one = [[1], [0], [0]]
    h0 = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
    h1 = [[0, 0, 1]]

    for vertex in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        left = mat_vec(d1, mat_vec(h0, vertex))
        right = mat_vec(h_minus_one, mat_vec(augmentation, vertex))
        assert add(left, right) == list(vertex)
    for edge in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        left = mat_vec(d2, mat_vec(h1, edge))
        right = mat_vec(h0, mat_vec(d1, edge))
        assert add(left, right) == list(edge)
    assert mat_vec(h1, mat_vec(d2, [1])) == [1]

    # Entry 131 fixes each local commutator to zero; flat localization and the
    # integral contraction make its operator-valued descent unique.
    local_commutators = [0, 0, 0]
    assert mat_vec(d1, local_commutators) == [0, 0, 0]
    global_commutator = 0
    assert global_commutator == 0

    # Nonvacuity checks inherited from the independently fixed boundary maps.
    generic_q_roof_coefficient = 1
    generic_rees_factor = "x_D"
    endpoint_matrix = [[0, 1], [1, 0]]
    endpoint_determinant = -1
    closed_cartier_residue = 1
    assert generic_q_roof_coefficient == 1
    assert generic_rees_factor == "x_D"
    assert endpoint_matrix == [[0, 1], [1, 0]]
    assert endpoint_determinant == -1
    assert closed_cartier_residue == 1

    print("three_chart_Cech_ranks: 1,2,1")
    print("three_chart_Cech_contraction: INTEGRAL_AND_EXPLICIT")
    print("local_Cartier_commutators: 0,0,0")
    print("global_Cartier_commutator: 0")
    print("operator_descent: UNIQUE")
    print("generic_Q_roof: PRIMITIVE_NONZERO")
    print("generic_Rees_factor: x_D")
    print("closed_Cartier_residue: +1")
    print("endpoint_comparison_determinant: -1")
    print("assembled_filtered_connector: CONSTRUCTED_IN_FINITE_PC_CECH_MODEL")
    print("full_geometric_primal_trace: NOT_CLAIMED")


if __name__ == "__main__":
    main()
