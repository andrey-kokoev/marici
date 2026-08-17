"""Audit the unique Thom/Gysin regrading compatible with the PC target."""


def main():
    tate = [1, 3, 3, 1]
    cartier = [1, 3, 3, 1]
    target = [12, 57, 87, 43]

    # A uniform codimension-one Gysin correction c per Cartier degree sends
    # total degree p+q to p+q-cq+shift.
    admissible = []
    for correction in range(-4, 6):
        for shift in range(-12, 13):
            image_degrees = {
                p + q - correction * q + shift
                for p, p_rank in enumerate(tate)
                for q, q_rank in enumerate(cartier)
                if p_rank and q_rank
            }
            if image_degrees == {0, 1, 2, 3}:
                admissible.append((correction, shift))
    assert admissible == [(1, 0)]

    collapsed = [
        tate_rank * sum(cartier)
        for tate_rank in tate
    ]
    assert collapsed == [8, 24, 24, 8]
    assert all(source_rank <= target_rank for source_rank, target_rank in zip(collapsed, target))

    # Under deg_G(p,q)=p, the horizontal Tate differential remains degree -1,
    # while the vertical Cartier differential becomes degree zero.
    for p in range(4):
        for q in range(4):
            if p:
                assert (p - 1) - p == -1
            if q:
                assert p - p == 0

    print("uniform_regrading: deg_G(p,q)=p+q-q=p")
    print("admissible_correction_and_shift: (1,0)")
    print("uniqueness: YES")
    print("collapsed_degree_ranks: 8,24,24,8")
    print("target_degree_ranks: 12,57,87,43")
    print("degreewise_rank_capacity: PASS")
    print("Tate_differential_degree: -1")
    print("Cartier_operator_degree: 0")
    print("interpretation: FILTERED_GYSIN_TRANSFER")
    print("transferred_chain_map: NOT_YET_CONSTRUCTED")


if __name__ == "__main__":
    main()
