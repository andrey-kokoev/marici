"""Audit the four-term Gysin-collapsed filtered PC module."""

from itertools import combinations
from math import comb


def add_term(vector, basis, coefficient):
    vector[basis] = vector.get(basis, 0) + coefficient
    if vector[basis] == 0:
        del vector[basis]


def carrier_basis(degree):
    return {
        0: [("z", 0)],
        1: [("r", i) for i in range(3)],
        2: [("t", i) for i in range(3)],
        3: [("o", 0)],
    }[degree]


def carrier_boundary(basis):
    kind, index = basis
    if kind == "o":
        return {("t", i): 1 for i in range(3)}
    if kind == "t":
        return {("r", index): 1, ("r", (index + 1) % 3): -1}
    if kind == "r":
        return {("z", 0): 1}
    return {}


def carrier_homotopy(basis):
    kind, index = basis
    if kind == "z":
        return {("r", 0): 1}
    if kind == "r" and index == 1:
        return {("t", 0): -1}
    if kind == "r" and index == 2:
        return {("t", 0): -1, ("t", 1): -1}
    if kind == "t" and index == 2:
        return {("o", 0): 1}
    return {}


def cartier_states(filtration):
    return list(combinations(range(3), filtration))


def module_basis(degree):
    return [
        (carrier, state)
        for carrier in carrier_basis(degree)
        for filtration in range(4)
        for state in cartier_states(filtration)
    ]


def chain_boundary(basis):
    carrier, state = basis
    return {
        (target, state): coefficient
        for target, coefficient in carrier_boundary(carrier).items()
    }


def chain_homotopy(basis):
    carrier, state = basis
    return {
        (target, state): coefficient
        for target, coefficient in carrier_homotopy(carrier).items()
    }


def bockstein(basis):
    carrier, state = basis
    result = {}
    for position in range(len(state)):
        target = state[:position] + state[position + 1 :]
        add_term(result, (carrier, target), (-1) ** position)
    return result


def cartier_homotopy(basis):
    carrier, state = basis
    if 0 in state:
        return {}
    return {(carrier, (0,) + state): 1}


def apply(operator, vector):
    result = {}
    for basis, coefficient in vector.items():
        for target, target_coefficient in operator(basis).items():
            add_term(result, target, coefficient * target_coefficient)
    return result


def sum_vectors(left, right):
    result = dict(left)
    for basis, coefficient in right.items():
        add_term(result, basis, coefficient)
    return result


def main():
    bases = {degree: module_basis(degree) for degree in range(4)}
    assert [len(bases[degree]) for degree in range(4)] == [8, 24, 24, 8]

    filtration_profiles = [
        [
            len(carrier_basis(degree)) * comb(3, filtration)
            for filtration in range(4)
        ]
        for degree in range(4)
    ]
    assert filtration_profiles == [
        [1, 3, 3, 1],
        [3, 9, 9, 3],
        [3, 9, 9, 3],
        [1, 3, 3, 1],
    ]

    for degree in range(4):
        for basis in bases[degree]:
            vector = {basis: 1}
            assert apply(chain_boundary, apply(chain_boundary, vector)) == {}
            assert apply(bockstein, apply(bockstein, vector)) == {}
            assert apply(chain_boundary, apply(bockstein, vector)) == apply(
                bockstein, apply(chain_boundary, vector)
            )

            dh_hd = sum_vectors(
                apply(chain_boundary, apply(chain_homotopy, vector)),
                apply(chain_homotopy, apply(chain_boundary, vector)),
            )
            assert dh_hd == vector

            bh_hb = sum_vectors(
                apply(bockstein, apply(cartier_homotopy, vector)),
                apply(cartier_homotopy, apply(bockstein, vector)),
            )
            assert bh_hb == vector

    print("chain_degree_ranks: 8,24,24,8")
    print("filtration_profiles: 1-3-3-1;3-9-9-3;3-9-9-3;1-3-3-1")
    print("carrier_d_squared: 0")
    print("Cartier_B_squared: 0")
    print("carrier_Cartier_commutator: 0")
    print("integral_carrier_contraction: EXPLICIT")
    print("integral_Cartier_filtration_contraction: EXPLICIT")
    print("collapsed_filtered_PC_module: CONSTRUCTED")
    print("occurrence_Cech_realization: NOT_YET_CONSTRUCTED")


if __name__ == "__main__":
    main()
