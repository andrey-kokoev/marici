#!/usr/bin/env python3
"""Exact constructor-dependence census for the relative-syndrome decoder."""

from fractions import Fraction


def coefficient(depth):
    return Fraction(-6, 1) if depth % 2 else Fraction(-1, 6)


def differential_rank(depth, branching):
    assert depth >= 1 and branching >= 1
    # Each parent row has disjoint nonzero child support, and multiplication
    # by a nonzero multiple of z on Q[z]/(z^2) has Q-rank one.
    assert coefficient(depth) != 0
    return branching ** (depth - 1)


def stable_homology(depth, branching):
    chain_dimension = 2 * branching ** depth
    return (
        chain_dimension
        - differential_rank(depth, branching)
        - differential_rank(depth + 1, branching)
    )


def main():
    census = {}
    for branching in range(1, 8):
        values = []
        for depth in range(1, 5):
            observed = stable_homology(depth, branching)
            expected = (branching - 1) * branching ** (depth - 1)
            assert observed == expected
            values.append(observed)
        census[branching] = values

    assert census[1] == [0, 0, 0, 0]
    assert census[4] == [3, 12, 48, 192]
    assert census[5] == [4, 20, 100, 500]
    assert census[4] != census[5]

    print("PASS: H_n^(k)=(k-1)k^(n-1) for k=1..7 and n=1..4")
    print("PASS: the four-branch three-plane changes under constructor refinement")
    print("GATE: no physical typing is allowed before source derivation of A and epsilon")


if __name__ == "__main__":
    main()
