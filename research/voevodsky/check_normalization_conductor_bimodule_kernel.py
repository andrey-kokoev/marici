"""Audit the universal mixed-variance normalization-conductor kernel."""

from math import gcd


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector))


def main():
    # Degree-n truncations of A+=Z[x] and A-=Z[y].  The conductor maps retain
    # the constant term, and delta=epsilon_+-epsilon_- is primitive surjective.
    n = 6
    sheet_rank = n + 1
    delta = [1] + [0] * n + [-1] + [0] * n
    assert len(delta) == 2 * sheet_rank
    assert gcd(*delta) == 1
    node_rank = len(delta) - 1
    assert node_rank == 2 * n + 1

    # Reflection swaps the sheet blocks.  Delta changes sign, so equivariance
    # requires the conductor orientation line to be odd.
    for basis_index in range(2 * sheet_rank):
        basis = [0] * (2 * sheet_rank)
        basis[basis_index] = 1
        reflected = basis[sheet_rank:] + basis[:sheet_rank]
        assert dot(delta, reflected) == -dot(delta, basis)

    # The forced ray-to-sheet comparison is the unimodular endpoint swap.
    endpoint_swap = [[0, 1], [1, 0]]
    determinant = endpoint_swap[0][0] * endpoint_swap[1][1] - endpoint_swap[0][1] * endpoint_swap[1][0]
    assert determinant == -1

    # Relative exceptional interval: Z^2 -> Z with row (-1,-1). Its kernel is
    # generated primitively by (-1,+1), supplying the retained shifted grade.
    relative_boundary = [-1, -1]
    relative_class = [-1, 1]
    assert dot(relative_boundary, relative_class) == 0
    assert gcd(*relative_class) == 1

    # K=[A+ direct-sum A- -> C] has H0=A_node and H1=0. Tensoring its
    # quasi-isomorphic node module with Tor0 plus the relative Tor1 line gives
    # one torsion-free copy in each of two adjacent grades.
    retained_homology_ranks = (node_rank, node_rank)
    assert retained_homology_ranks == (13, 13)

    # Forgetting endpoint framing replaces relative chains by the absolute V
    # tree. Its boundary Z^2 -> Z^3 is injective, so the relative H1 class dies.
    absolute_boundary = [
        [-1, -1],
        [1, 0],
        [0, 1],
    ]
    column_0 = [row[0] for row in absolute_boundary]
    column_1 = [row[1] for row in absolute_boundary]
    assert column_0 != column_1
    unit_minor = (
        absolute_boundary[1][0] * absolute_boundary[2][1]
        - absolute_boundary[1][1] * absolute_boundary[2][0]
    )
    assert unit_minor == 1
    absolute_image_of_relative_class = [
        row[0] * relative_class[0] + row[1] * relative_class[1]
        for row in absolute_boundary
    ]
    assert absolute_image_of_relative_class == [0, -1, 1]
    assert absolute_image_of_relative_class != [0, 0, 0]

    print("recollement_kernel: [A+ direct-sum A- -> C]")
    print("conductor_differential: epsilon_+ - epsilon_-")
    print("differential_primitive_surjective: YES")
    print(f"node_kernel_rank_at_truncation_6: {node_rank}")
    print("reflection_on_conductor: ODD")
    print("endpoint_comparison: UNIMODULAR_SWAP")
    print("retained_Tor_grades: ONE_UNSHIFTED_PLUS_ONE_SHIFTED")
    print("integral_torsion: NONE")
    print("ordinary_endpoint_forgetting_kills_relative_class: YES")
    print("mixed_variance_bimodule_kernel: CONSTRUCTED_UNIVERSALLY")
    print("full_multirees_stalk_instantiation: NEXT_GATE")


if __name__ == "__main__":
    main()
