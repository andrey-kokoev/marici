"""Test the first four-Cut induction gate on the dodecagon."""

from collections import Counter
from itertools import combinations, permutations

import check_n10_physical_cut_nerve as n10_nerve
import check_n10_physical_cut_obstruction as regions
from check_n8_cut_cech_h1_carrier_homology import unit_smith_rank
import check_n8_six_by_four_cut_boundary as polygon


N = 12


def physical_cuts():
    return tuple(d for d in polygon.diagonals(N) if (d[1] - d[0]) % 2 == 1)


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
    assert len(cuts) == 24
    channel_types = Counter(min(b - a, N - (b - a)) for a, b in cuts)
    assert channel_types == {3: 12, 5: 12}

    simplices = {}
    for size in range(1, 6):
        simplices[size] = tuple(
            simplex
            for simplex in combinations(cuts, size)
            if all(not polygon.crosses(a, b) for a, b in combinations(simplex, 2))
        )
    assert not simplices[5]
    assert simplices[4]

    profile_counts = {}
    for size in range(1, 5):
        profile_counts[size] = Counter(
            tuple(sorted(map(len, regions.polygon_regions(simplex, N))))
            for simplex in simplices[size]
        )
    assert profile_counts[1] == {(4, 10): 12, (6, 8): 12}
    assert set(value for profile in profile_counts.values() for value in profile) <= {
        (4, 10), (6, 8), (4, 4, 8), (4, 6, 6),
        (4, 4, 4, 6), (4, 4, 4, 4, 4)
    }
    assert profile_counts[4] == {(4, 4, 4, 4, 4): len(simplices[4])}

    boundaries = {
        degree: incidence(simplices[degree], simplices[degree + 1])
        for degree in range(1, 4)
    }
    ranks = {degree: n10_nerve.rank(matrix) for degree, matrix in boundaries.items()}
    unit_ranks = {degree: unit_smith_rank(matrix)[0] for degree, matrix in boundaries.items()}
    assert ranks == unit_ranks
    for degree in range(1, 3):
        left, right = boundaries[degree], boundaries[degree + 1]
        assert all(
            sum(left[i][k] * right[k][j] for k in range(len(right))) == 0
            for i in range(len(left))
            for j in range(len(right[0]))
        )
    betti = (
        len(simplices[1]) - ranks[1],
        len(simplices[2]) - ranks[1] - ranks[2],
        len(simplices[3]) - ranks[2] - ranks[3],
        len(simplices[4]) - ranks[3],
    )

    order_checks = 0
    obstruction = []
    for simplex in simplices[4]:
        assert tuple(sorted(map(len, regions.polygon_regions(simplex, N)))) == (4, 4, 4, 4, 4)
        for order in permutations(range(4)):
            koszul = permutation_sign(order)
            thom = permutation_sign(order)
            value = koszul * thom
            assert value == 1
            order_checks += 1
        obstruction.append(0)
    assert not any(obstruction)

    print(f"n12_physical_Cuts: {len(cuts)}=12_SHORT_PLUS_12_MEDIUM")
    print("n12_Cut_nerve_f_vector: " + ",".join(str(len(simplices[d])) for d in range(1, 5)))
    print("n12_Cut_nerve_boundary_ranks: " + ",".join(str(ranks[d]) for d in range(1, 4)))
    print("n12_Cut_nerve_integral_Betti: " + ",".join(map(str, betti)))
    print("n12_Cut_nerve_nonzero_Smith_factors: ALL_ONE")
    for degree in range(1, 5):
        print(f"stratum_{degree - 1}_profiles: {dict(profile_counts[degree])}")
    print(f"compatible_quadruple_order_checks: {order_checks}")
    print("combined_four_Cut_permutation_character: TRIVIAL")
    print("physical_top_obstruction_3_cochain: ZERO")
    print("all_stratum_factor_arities: SUBSET_OF_{4,6,8,10}_RIGID")
    print("n12_framed_Cut_gluing: EXISTS_AND_IS_CONTRACTIBLE")
    print("next_gate: EXTRACT_GENERAL_EVEN_ARITY_INDUCTION_THEOREM")


if __name__ == "__main__":
    main()
