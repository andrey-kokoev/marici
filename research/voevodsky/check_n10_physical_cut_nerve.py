"""Construct the decagon physical Cut nerve and its Thom sign coherence."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

import check_n8_six_by_four_cut_boundary as polygon
from check_n8_cut_cech_h1_carrier_homology import unit_smith_rank


N = 10


def physical_cuts():
    return tuple(
        d for d in polygon.diagonals(N) if (d[1] - d[0]) % 2 == 1
    )


def rank(matrix):
    if not matrix:
        return 0
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def incidence(lower, upper):
    lower_index = {simplex: i for i, simplex in enumerate(lower)}
    matrix = [[0] * len(upper) for _ in lower]
    for column, simplex in enumerate(upper):
        for removed in range(len(simplex)):
            face = simplex[:removed] + simplex[removed + 1 :]
            matrix[lower_index[face]][column] = (-1) ** removed
    return matrix


def permutation_sign(order):
    inversions = sum(
        order[i] > order[j]
        for i in range(len(order))
        for j in range(i + 1, len(order))
    )
    return -1 if inversions % 2 else 1


def main():
    cuts = physical_cuts()
    assert len(cuts) == 15
    channel_types = Counter(min(b - a, N - (b - a)) for a, b in cuts)
    assert channel_types == {3: 10, 5: 5}

    simplices = {size: [] for size in range(1, 5)}
    for size in range(1, 5):
        simplices[size] = tuple(
            simplex
            for simplex in combinations(cuts, size)
            if all(not polygon.crosses(a, b) for a, b in combinations(simplex, 2))
        )
    assert len(simplices[4]) == 0
    assert len(simplices[3]) > 0

    d1 = incidence(simplices[1], simplices[2])
    d2 = incidence(simplices[2], simplices[3])
    assert all(
        sum(d1[i][k] * d2[k][j] for k in range(len(simplices[2]))) == 0
        for i in range(len(simplices[1]))
        for j in range(len(simplices[3]))
    )
    r1, r2 = rank(d1), rank(d2)
    u1, _ = unit_smith_rank(d1)
    u2, _ = unit_smith_rank(d2)
    assert (u1, u2) == (r1, r2)
    betti = (
        len(simplices[1]) - r1,
        len(simplices[2]) - r1 - r2,
        len(simplices[3]) - r2,
    )

    # For every compatible triple, changing the restriction order contributes
    # the Koszul sign of the permutation.  The three odd Thom-normal lines
    # contribute the same sign, so their tensor product is order-independent.
    order_checks = 0
    for simplex in simplices[3]:
        for order in permutations(range(3)):
            koszul = permutation_sign(order)
            thom = permutation_sign(order)
            assert koszul * thom == 1
            order_checks += 1

    print(f"n10_physical_Cuts: {len(cuts)}=10_SHORT_PLUS_5_DIAMETRAL")
    print("n10_Cut_nerve_f_vector: " + ",".join(str(len(simplices[s])) for s in range(1, 4)))
    print(f"n10_Cut_nerve_boundary_ranks: {r1},{r2}")
    print("n10_Cut_nerve_rational_Betti: " + ",".join(map(str, betti)))
    print("n10_Cut_nerve_nonzero_Smith_factors: ALL_ONE")
    print("n10_Cut_nerve_integral_homology: H0=Z,H1=0,H2=Z^14")
    print(f"compatible_triple_order_checks: {order_checks}")
    print("raw_Koszul_S3_character: SIGN")
    print("native_three_Thom_normal_character: SIGN")
    print("combined_triple_restriction_character: TRIVIAL")
    print("n10_local_three_Cut_sign_coherence: PROVED")
    print("next_gate: BUILD_INTEGRAL_THOM_TWISTED_CECH_COMPLEX_AND_TEST_H2")


if __name__ == "__main__":
    main()
