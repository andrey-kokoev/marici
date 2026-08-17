"""Audit the integral total normal form of the filtered atlas."""

from fractions import Fraction
from itertools import combinations


def add_term(vector, basis, coefficient):
    vector[basis] = vector.get(basis, 0) + coefficient
    if vector[basis] == 0:
        del vector[basis]


def tate_basis(degree):
    return {
        0: [("z", 0)],
        1: [("r", i) for i in range(3)],
        2: [("t", i) for i in range(3)],
        3: [("o", 0)],
    }.get(degree, [])


def tate_boundary(basis):
    kind, index = basis
    if kind == "o":
        return {("t", i): 1 for i in range(3)}
    if kind == "t":
        return {("r", index): 1, ("r", (index + 1) % 3): -1}
    if kind == "r":
        return {("z", 0): 1}
    return {}


def cartier_basis(degree):
    return list(combinations(range(3), degree))


def cartier_boundary(basis):
    result = {}
    for position in range(len(basis)):
        face = basis[:position] + basis[position + 1 :]
        add_term(result, face, (-1) ** position)
    return result


def cartier_homotopy(basis):
    if 0 in basis:
        return {}
    return {(0,) + basis: 1}


def total_basis(degree):
    result = []
    for p in range(4):
        q = degree - p
        if 0 <= q <= 3:
            result.extend((p, a, q, b) for a in tate_basis(p) for b in cartier_basis(q))
    return result


def total_boundary(basis):
    p, a, q, b = basis
    result = {}
    for target, coefficient in tate_boundary(a).items():
        add_term(result, (p - 1, target, q, b), coefficient)
    for target, coefficient in cartier_boundary(b).items():
        add_term(result, (p, a, q - 1, target), ((-1) ** p) * coefficient)
    return result


def total_homotopy(basis):
    p, a, q, b = basis
    return {
        (p, a, q + 1, target): ((-1) ** p) * coefficient
        for target, coefficient in cartier_homotopy(b).items()
    }


def apply(operator, vector):
    result = {}
    for basis, coefficient in vector.items():
        for target, target_coefficient in operator(basis).items():
            add_term(result, target, coefficient * target_coefficient)
    return result


def matrix_rank(columns, row_basis):
    rows = [[Fraction(column.get(row, 0)) for column in columns] for row in row_basis]
    rank = 0
    if not rows:
        return 0
    for column in range(len(columns)):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            factor = rows[row][column]
            rows[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(rows[row], rows[rank])
            ]
        rank += 1
    return rank


def main():
    bases = {degree: total_basis(degree) for degree in range(7)}
    dimensions = [len(bases[degree]) for degree in range(7)]
    assert dimensions == [1, 6, 15, 20, 15, 6, 1]

    for degree in range(2, 7):
        for basis in bases[degree]:
            assert apply(total_boundary, total_boundary(basis)) == {}

    # The Cartier unit in the first normal direction supplies an explicit
    # integral contraction of the total complex.
    for degree in range(7):
        for basis in bases[degree]:
            vector = {basis: 1}
            dh = apply(total_boundary, apply(total_homotopy, vector))
            hd = apply(total_homotopy, apply(total_boundary, vector))
            for target, coefficient in hd.items():
                add_term(dh, target, coefficient)
            assert dh == vector

    ranks = [0]
    for degree in range(1, 7):
        columns = [total_boundary(basis) for basis in bases[degree]]
        ranks.append(matrix_rank(columns, bases[degree - 1]))
    assert ranks == [0, 1, 5, 10, 10, 5, 1]

    nonzero_coefficients = {
        abs(coefficient)
        for degree in range(1, 7)
        for basis in bases[degree]
        for coefficient in total_boundary(basis).values()
    }
    assert nonzero_coefficients == {1}

    print("total_degrees: 0..6")
    print("total_ranks: 1,6,15,20,15,6,1")
    print("differential_ranks: 1,5,10,10,5,1")
    print("d_squared: 0")
    print("integral_contraction: EXPLICIT")
    print("matrix_coefficients: 0,+1,-1")
    print("total_normal_form: SPLIT_EXACT_AND_UNIMODULAR")
    print("scope: normalized_finite_filtered_PC_model")
    print("occurrence_Cech_realization_map: NOT_YET_TOTALIZED")


if __name__ == "__main__":
    main()
