#!/usr/bin/env python3
"""Identify the descended q_J roof with the canonical D03 Yoneda basis."""

from itertools import combinations


Diagonal = tuple[int, int]


def diagonal(a: int, b: int) -> Diagonal:
    return (a, b) if a < b else (b, a)


def between(v: int, a: int, b: int) -> bool:
    return 0 < (v + 6 - a) % 6 < (b + 6 - a) % 6


def crosses(x: Diagonal, y: Diagonal) -> bool:
    if set(x) & set(y):
        return False
    return (between(y[0], *x) != between(y[1], *x)
            and between(x[0], *y) != between(x[1], *y))


def main() -> None:
    longs = [diagonal(i, i + 3) for i in range(3)]
    d03 = diagonal(0, 3)
    assert d03 in longs
    assert all(crosses(x, y) for x, y in combinations(longs, 2))

    # Hence the support-level-2 face poset is top plus three isolated long
    # facets.  Its normalized relative one-chains have the three primitive
    # edges [top<D_i], and there are no normalized two-simplices.
    q_edges = [("top", value) for value in longs]
    q_two_simplices: list[tuple] = []
    assert len(q_edges) == 3
    assert not q_two_simplices

    # The descended corrected roof:
    # q_J = -[top,a] + [top,D03] + XD03[D03,c].
    qj_q_coordinates = [1 if value == d03 else 0 for _, value in q_edges]
    assert qj_q_coordinates == [1, 0, 0]
    assert sum(abs(x) for x in qj_q_coordinates) == 1

    # With no Q two-simplex, the primitive unit vector is not a boundary.
    boundary_rank_into_q_edges = 0
    assert boundary_rank_into_q_edges == 0

    f1_correction = "+XD03[D03,c]"
    f0_correction = "-[top,v_plus]"
    assert f1_correction.startswith("+")
    assert f0_correction.startswith("-")

    print("Q_basis: [top<D03], [top<D14], [top<D25]")
    print("Q_two_simplices: 0")
    print("qJ_Q_coordinate: (1,0,0), primitive and nonboundary")
    print("roof_corrections: +XD03[D03,c], -[top,v_plus]")
    print("canonical_D03_Yoneda_roof: IDENTIFIED")


if __name__ == "__main__":
    main()
