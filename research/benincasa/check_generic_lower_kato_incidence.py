"""Type the generic lower deletion cube by its frozen affine pole incidence."""

from fractions import Fraction
from itertools import combinations


NAMES = ("q_g1", "q_g2", "q_g3", "q_g23")
# Coordinates are (c,a,b), with equations normal dot x + constant = 0.
PLANES = (
    ((1, 0, 1), "X1"),
    ((1, 1, 0), "X2"),
    ((0, 1, 1), "X3"),
    ((1, 0, 1), "X2+X3"),
)
PROPER = (7, 5, 5, 1, 5, 1, 1, 1, 5, 0, 1, 0, 1, 0, 1, 0)


def rank(rows):
    if not rows:
        return 0
    work = [[Fraction(value) for value in row] for row in rows]
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


def generically_nonempty(indices):
    normals = [PLANES[i][0] for i in indices]
    normal_rank = rank(normals)
    # The only dependent normals are q_g1 and q_g23. Their generic constants
    # differ by X1-X2-X3, so any subset containing both is empty.
    if 0 in indices and 3 in indices:
        return False, normal_rank
    return normal_rank == len(indices), normal_rank


def main():
    nonempty_masks = []
    empty_masks = []
    for size in range(1, 5):
        for indices in combinations(range(4), size):
            mask = sum(1 << i for i in indices)
            nonempty, normal_rank = generically_nonempty(indices)
            if nonempty:
                assert normal_rank == size
                nonempty_masks.append(mask)
            else:
                empty_masks.append(mask)

    nonempty_masks.sort()
    empty_masks.sort()
    assert [mask for mask in range(1, 16) if PROPER[mask] > 0] == nonempty_masks
    assert empty_masks == [0b1001, 0b1011, 0b1101, 0b1111]
    assert tuple(PROPER[mask] for mask in nonempty_masks if mask.bit_count() == 1) == (5, 5, 5, 5)
    assert tuple(PROPER[mask] for mask in nonempty_masks if mask.bit_count() == 2) == (1, 1, 1, 1, 1)
    assert tuple(PROPER[mask] for mask in nonempty_masks if mask.bit_count() == 3) == (1, 1)

    # Boolean localization signs anticommute on every nonempty square. This is
    # the support-level differential of the iterated residue/Gysin cube.
    square_checks = 0
    for mask in range(16):
        for i, j in combinations([k for k in range(4) if not mask & (1 << k)], 2):
            top = mask | (1 << i) | (1 << j)
            if top not in nonempty_masks:
                continue
            sign_i = (-1) ** sum(mask & (1 << k) != 0 for k in range(i))
            sign_j_after_i = (-1) ** sum((mask | (1 << i)) & (1 << k) != 0 for k in range(j))
            sign_j = (-1) ** sum(mask & (1 << k) != 0 for k in range(j))
            sign_i_after_j = (-1) ** sum((mask | (1 << j)) & (1 << k) != 0 for k in range(i))
            assert sign_i * sign_j_after_i == -(sign_j * sign_i_after_j)
            square_checks += 1

    print("pole_normal_vectors: (101),(110),(011),(101)")
    print("unique_parallel_pair: q_g1,q_g23")
    print("generic_parallel_coincidence_divisor: X1-X2-X3")
    print("finite_pair_strata: 5")
    print("transverse_triple_strata: q_g1q_g2q_g3,q_g2q_g3q_g23")
    print("empty_support_masks: 1001,1011,1101,1111")
    print(f"Boolean_Gysin_sign_squares: {square_checks}")
    print("nonzero_proper_grade_supports_equal_nonempty_incidence_strata: YES")
    print("Kato_support_typing_of_deletion_cube: PASS")
    print("rank_five_coefficient_objects_and_Gysin_maps: NOT_YET_CONSTRUCTED")


if __name__ == "__main__":
    main()
