"""Solve the integral chain-homotopy problem for two frozen reflections.

Input is only the minimal combined discrepancy complex: six labelled
vertices and the union of the independently frozen cross-sheet and
same-sheet legal edges.  Its triangular 2-cells and relative interior are
derived by clique completion, not inserted as the desired answer.
"""

from itertools import combinations, product
from fractions import Fraction
import json
import math


def zeros(rows, columns):
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matadd(left, right):
    return [[a + b for a, b in zip(x, y)] for x, y in zip(left, right)]


def matsub(left, right):
    return [[a - b for a, b in zip(x, y)] for x, y in zip(left, right)]


def negate(matrix):
    return [[-value for value in row] for row in matrix]


def column(matrix, index):
    return [row[index] for row in matrix]


column_values = column


def set_column(matrix, index, values):
    for row, value in zip(matrix, values):
        row[index] = value


def solve(left, right):
    """One exact solution with free variables zero, plus nullity."""
    rows = len(left)
    columns = len(left[0])
    augmented = [list(map(Fraction, left[i])) + [Fraction(right[i])] for i in range(rows)]
    pivots = []
    pivot_row = 0
    for pivot_column in range(columns):
        found = next((r for r in range(pivot_row, rows) if augmented[r][pivot_column]), None)
        if found is None:
            continue
        augmented[pivot_row], augmented[found] = augmented[found], augmented[pivot_row]
        divisor = augmented[pivot_row][pivot_column]
        augmented[pivot_row] = [value / divisor for value in augmented[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            factor = augmented[r][pivot_column]
            if factor:
                augmented[r] = [a - factor * b for a, b in zip(augmented[r], augmented[pivot_row])]
        pivots.append(pivot_column)
        pivot_row += 1
        if pivot_row == rows:
            break
    for row in augmented:
        if all(value == 0 for value in row[:columns]) and row[columns] != 0:
            raise ValueError("inconsistent linear system")
    solution = [Fraction(0) for _ in range(columns)]
    for r, pivot in enumerate(pivots):
        solution[pivot] = augmented[r][columns]
    return solution, columns - len(pivots)


def nullspace(left):
    rows = len(left)
    columns = len(left[0])
    zero = [Fraction(0)] * rows
    # Obtain RREF once through the same elimination, then seed each free var.
    augmented = [list(map(Fraction, left[i])) + [zero[i]] for i in range(rows)]
    pivots = []
    pivot_row = 0
    for pivot_column in range(columns):
        found = next((r for r in range(pivot_row, rows) if augmented[r][pivot_column]), None)
        if found is None:
            continue
        augmented[pivot_row], augmented[found] = augmented[found], augmented[pivot_row]
        divisor = augmented[pivot_row][pivot_column]
        augmented[pivot_row] = [value / divisor for value in augmented[pivot_row]]
        for r in range(rows):
            if r != pivot_row and augmented[r][pivot_column]:
                factor = augmented[r][pivot_column]
                augmented[r] = [a - factor * b for a, b in zip(augmented[r], augmented[pivot_row])]
        pivots.append(pivot_column)
        pivot_row += 1
    free = [value for value in range(columns) if value not in pivots]
    basis = []
    for free_column in free:
        vector = [Fraction(0)] * columns
        vector[free_column] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = -augmented[r][free_column]
        basis.append(vector)
    return basis


def edge(a, b):
    return (a, b) if a < b else (b, a)


def oriented_edge(a, b):
    return edge(a, b), (1 if a < b else -1)


def source_reflection(i):
    return (1 - i) % 6


def literal_reflection(i):
    return (5 - i) % 6


def rank_over_q(matrix):
    return len(matrix[0]) - solve(matrix, [0] * len(matrix))[1]


def main():
    vertices = tuple(range(6))
    opposite = {edge(i, i + 3) for i in range(3)}
    edges = tuple(
        candidate
        for candidate in combinations(vertices, 2)
        if candidate not in opposite
    )
    edge_index = {value: index for index, value in enumerate(edges)}

    # Clique completion is forced by the legal one-skeleton.
    faces = tuple(
        triple
        for triple in combinations(vertices, 3)
        if all(edge(a, b) in edge_index for a, b in combinations(triple, 2))
    )
    assert len(edges) == 12
    assert len(faces) == 8

    d1 = zeros(6, 12)
    for column, (a, b) in enumerate(edges):
        d1[a][column] = -1
        d1[b][column] = 1

    d2 = zeros(12, 8)
    for column, (a, b, c) in enumerate(faces):
        for (left, right), coefficient in [((b, c), 1), ((a, c), -1), ((a, b), 1)]:
            present, orientation = oriented_edge(left, right)
            d2[edge_index[present]][column] += coefficient * orientation
    assert matmul(d1, d2) == zeros(6, 8)

    # The primitive kernel of d2 is the relative interior boundary.
    kernel = nullspace(d2)
    assert len(kernel) == 1
    top = kernel[0]
    lcm = 1
    for value in top:
        lcm = math.lcm(lcm, value.denominator)
    top = [value * lcm for value in top]
    gcd = 0
    for value in top:
        gcd = math.gcd(gcd, abs(int(value)))
    top = [value / gcd for value in top]
    assert all(abs(int(value)) == 1 for value in top)
    d3 = [[value] for value in top]

    def chain_action(permutation):
        p0 = zeros(6, 6)
        for source in vertices:
            p0[permutation(source)][source] = 1

        p1 = zeros(12, 12)
        for column, (a, b) in enumerate(edges):
            image, sign = oriented_edge(permutation(a), permutation(b))
            p1[edge_index[image]][column] = sign

        p2 = zeros(8, 8)
        face_sets = [set(value) for value in faces]
        for column, face_value in enumerate(faces):
            transformed_boundary = matmul(p1, [[value] for value in column_values(d2, column)])
            image_set = {permutation(value) for value in face_value}
            row = face_sets.index(image_set)
            candidate = [[value] for value in column_values(d2, row)]
            if transformed_boundary == candidate:
                p2[row][column] = 1
            elif transformed_boundary == negate(candidate):
                p2[row][column] = -1
            else:
                raise AssertionError("face orientation transport failed")
        assert matmul(p0, d1) == matmul(d1, p1)
        assert matmul(p1, d2) == matmul(d2, p2)

        image_top = matmul(p2, d3)
        if image_top == d3:
            p3 = 1
        elif image_top == negate(d3):
            p3 = -1
        else:
            raise AssertionError("interior orientation transport failed")
        return p0, p1, p2, p3

    src = chain_action(source_reflection)
    lit = chain_action(literal_reflection)

    # H0 is forced by the legal direct edge from each source-reflected image
    # to the corresponding literal-reflected image.
    h0 = zeros(12, 6)
    for column in vertices:
        a = source_reflection(column)
        b = literal_reflection(column)
        present, sign = oriented_edge(a, b)
        h0[edge_index[present]][column] = sign
    assert matmul(d1, h0) == matsub(lit[0], src[0])

    # Solve d2 H1 = (S_lit-S_src)_1 - H0 d1 over the integers.
    residual1 = matsub(matsub(lit[1], src[1]), matmul(h0, d1))
    h1 = zeros(8, 12)
    free_parameters = 0
    for column in range(12):
        chosen, nullity = solve(d2, column_values(residual1, column))
        free_parameters += nullity
        assert all(value.denominator == 1 for value in chosen)
        set_column(h1, column, chosen)
    assert matadd(matmul(d2, h1), matmul(h0, d1)) == matsub(lit[1], src[1])

    # The 2-cell discrepancy must factor through the primitive relative
    # interior boundary d3.  Solve d3 H2 = residual2.
    residual2 = matsub(matsub(lit[2], src[2]), matmul(h1, d2))
    h2 = zeros(1, 8)
    for column in range(8):
        candidates = [
            int(residual2[row][column] / d3[row][0])
            for row in range(8)
        ]
        assert len(set(candidates)) == 1
        h2[0][column] = candidates[0]
    assert matadd(matmul(d3, h2), matmul(h1, d2)) == matsub(lit[2], src[2])
    assert matmul(h2, d3) == [[Fraction(lit[3] - src[3])]]

    # The sequential zero-parameter gauge is not geometrically privileged.
    # Solve the H1/H2 equations jointly while requiring H2 to be supported
    # only on the two pure parity faces.
    h1_variables = 8 * 12
    variable_count = h1_variables + 8
    joint_left = []
    joint_right = []
    for row in range(12):
        for col in range(12):
            equation = [Fraction(0)] * variable_count
            for face_row in range(8):
                equation[face_row * 12 + col] = d2[row][face_row]
            joint_left.append(equation)
            joint_right.append(residual1[row][col])
    delta2 = matsub(lit[2], src[2])
    for row in range(8):
        for col in range(8):
            equation = [Fraction(0)] * variable_count
            equation[h1_variables + col] = d3[row][0]
            for edge_row in range(12):
                equation[row * 12 + edge_row] += d2[edge_row][col]
            joint_left.append(equation)
            joint_right.append(delta2[row][col])
    equation = [Fraction(0)] * variable_count
    for face_index in range(8):
        equation[h1_variables + face_index] = d3[face_index][0]
    joint_left.append(equation)
    joint_right.append(Fraction(lit[3] - src[3]))

    pure_face_indices = [
        index
        for index, face_value in enumerate(faces)
        if all(vertex % 2 == face_value[0] % 2 for vertex in face_value)
    ]
    mixed_face_indices = [
        index for index in range(8) if index not in pure_face_indices
    ]
    assert len(pure_face_indices) == 2
    for face_index in mixed_face_indices:
        equation = [Fraction(0)] * variable_count
        equation[h1_variables + face_index] = 1
        joint_left.append(equation)
        joint_right.append(Fraction(0))
    pure_solution, pure_nullity = solve(joint_left, joint_right)
    assert all(value.denominator == 1 for value in pure_solution)
    pure_h2 = pure_solution[h1_variables:]
    assert all(pure_h2[index] == 0 for index in mixed_face_indices)
    pure_gauge_h2_vanishes = all(value == 0 for value in pure_h2)
    assert pure_gauge_h2_vanishes

    # Stronger gate: require H1 to use mixed faces only and H2=0.
    mixed_only_left = [row[:] for row in joint_left[:-len(mixed_face_indices)]]
    mixed_only_right = joint_right[:-len(mixed_face_indices)]
    for face_index in pure_face_indices:
        for edge_index_value in range(12):
            equation = [Fraction(0)] * variable_count
            equation[face_index * 12 + edge_index_value] = 1
            mixed_only_left.append(equation)
            mixed_only_right.append(Fraction(0))
    for face_index in range(8):
        equation = [Fraction(0)] * variable_count
        equation[h1_variables + face_index] = 1
        mixed_only_left.append(equation)
        mixed_only_right.append(Fraction(0))
    try:
        mixed_only_solution, mixed_only_nullity = solve(
            mixed_only_left, mixed_only_right
        )
        mixed_only_integral = all(
            value.denominator == 1 for value in mixed_only_solution
        )
        mixed_only_exists = mixed_only_integral
    except ValueError:
        mixed_only_exists = False
        mixed_only_integral = False
        mixed_only_nullity = None

    h0_support = sum(value != 0 for row in h0 for value in row)
    h1_support = sum(value != 0 for row in h1 for value in row)
    h2_support = sum(value != 0 for row in h2 for value in row)
    h2_nonzero_faces = [
        list(faces[index])
        for index, value in enumerate(h2[0])
        if value != 0
    ]
    print(json.dumps({
        "status": "proved_scoped_integral_reflection_discrepancy_nullhomotopy",
        "minimal_input": {
            "vertices": len(vertices),
            "legal_edges": len(edges),
            "derived_clique_faces": len(faces),
            "derived_relative_interiors": 1,
        },
        "chain_ranks": {
            "d1": rank_over_q(d1),
            "d2": rank_over_q(d2),
            "d3": rank_over_q(d3),
        },
        "integral_homotopy": True,
        "h0_nonzero_entries": h0_support,
        "h1_nonzero_entries_in_zero_parameter_gauge": h1_support,
        "h2_nonzero_entries_in_zero_parameter_gauge": h2_support,
        "h2_nonzero_faces_in_zero_parameter_gauge": h2_nonzero_faces,
        "pure_face_supported_gauge_exists": True,
        "h2_nonzero_faces_in_pure_gauge": [
            list(faces[index])
            for index in pure_face_indices
            if pure_h2[index] != 0
        ],
        "h2_pure_gauge_coefficients": [
            int(pure_h2[index]) for index in pure_face_indices
        ],
        "pure_gauge_h2_vanishes": pure_gauge_h2_vanishes,
        "mixed_faces_only_h1_with_zero_h2_exists": mixed_only_exists,
        "mixed_faces_only_solution_integral": mixed_only_integral,
        "mixed_faces_only_affine_parameter_count": mixed_only_nullity,
        "pure_gauge_affine_parameter_count": pure_nullity,
        "h1_affine_parameter_count": free_parameters,
        "primitive_relative_top": all(abs(int(row[0])) == 1 for row in d3),
        "all_chain_homotopy_equations": True,
        "conclusion": (
            "The independently stated reflection discrepancy has an integral "
            "nullhomotopy on the minimal legal completion.  The completion "
            "derives eight triangular cells and one primitive relative "
            "interior; these are consequences, not assumptions, of the "
            "obstruction problem."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
