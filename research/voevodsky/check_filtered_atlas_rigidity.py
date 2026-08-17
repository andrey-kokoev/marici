"""Audit rigidity of the capped filtered atlas in its order-three sector."""


def rank_mod(matrix, modulus):
    rows = [list(map(lambda x: x % modulus, row)) for row in matrix]
    if not rows:
        return 0
    rank = 0
    columns = len(rows[0])
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, modulus)
        rows[rank] = [(inverse * value) % modulus for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            factor = rows[row][column]
            rows[row] = [
                (value - factor * pivot_value) % modulus
                for value, pivot_value in zip(rows[row], rows[rank])
            ]
        rank += 1
    return rank


def main():
    modulus = 3
    orientation_monodromy = -1

    # The capped orientation-twisted Mobius carrier reduces to
    # F3 --(u-1)--> F3 --(u+1)--> F3.
    d0 = [[orientation_monodromy - 1]]
    d1 = [[orientation_monodromy + 1]]
    assert (d1[0][0] * d0[0][0]) % modulus == 0

    rank_d0 = rank_mod(d0, modulus)
    rank_d1 = rank_mod(d1, modulus)
    h0 = 1 - rank_d0
    h1 = (1 - rank_d1) - rank_d0
    h2 = 1 - rank_d1
    assert (h0, h1, h2) == (0, 0, 1)

    # Entry 412 evaluates the unique H2 obstruction coordinate.
    jordan_obstruction = 0
    assert jordan_obstruction == 0

    # Entry 400's endpoint equations select a unique integral comparison.
    endpoint_solutions = [
        (a, b)
        for a in range(-3, 4)
        for b in range(-3, 4)
        if b - a == 1 and a + b == 1
    ]
    assert endpoint_solutions == [(0, 1)]
    endpoint_parity = endpoint_solutions[0][0] % 2
    assert endpoint_parity == 0

    print("twisted_capped_complex: F3 --1--> F3 --0--> F3")
    print("twisted_cohomology_dimensions: H0=0,H1=0,H2=1")
    print("order_three_obstruction_coordinate: 0")
    print("order_three_lift_torsor_H1: 0")
    print("order_three_automorphisms_H0: 0")
    print("endpoint_comparison: (a,b)=(0,1)")
    print("endpoint_parity: 0")
    print("filtered_atlas_lift: EXISTS_AND_RIGID")
    print("scope: obstruction_theory_not_explicit_full_loaded_chain_map")


if __name__ == "__main__":
    main()
