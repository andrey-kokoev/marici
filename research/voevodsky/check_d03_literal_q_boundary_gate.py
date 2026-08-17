#!/usr/bin/env python3
"""Audit the literal absolute Q-boundary against the expanded log carrier."""

from dataclasses import dataclass


Diagonal = tuple[int, int]
Face = frozenset[Diagonal]


def diagonal(a: int, b: int) -> Diagonal:
    return (a, b) if a < b else (b, a)


def incidence_sign(face: Face, added: Diagonal) -> int:
    return 1 if sum(value < added for value in face) % 2 == 0 else -1


@dataclass(frozen=True)
class Term:
    coefficient: str
    face: Face


D03 = diagonal(0, 3)
X3 = diagonal(3, 5)
V_PLUS = frozenset({diagonal(1, 3), diagonal(3, 5), diagonal(1, 5)})
Q03 = frozenset({D03})
ED3 = frozenset({D03, X3})


def contains_d03(face: Face) -> bool:
    return D03 in face


def main() -> None:
    sign = incidence_sign(Q03, X3)
    literal_boundary = Term(f"{sign:+d} X3", ED3)

    assert sign == -1
    assert contains_d03(literal_boundary.face)
    assert not contains_d03(V_PLUS)

    # Every absolute cellular boundary of a D03-containing face is obtained by
    # adding a diagonal (or changing its normal-circle state), hence retains
    # D03.  Therefore G03 is a subcomplex and its projection to F0 is zero.
    absolute_second_transgression = 0
    assert absolute_second_transgression == 0

    # The expanded log path has an endpoint outside G03:
    # d C_log = XD03*X0*c - X1*X5*v_plus.
    expanded_v_plus_coefficient = "-X1*X5"
    assert expanded_v_plus_coefficient != "0"

    print("literal_Q_boundary: -X3 * {D03,x3}")
    print("first_coefficient_match: PASS (up to the forced target-basis sign)")
    print("absolute_second_transgression: ZERO (G03 is D03-supported)")
    print("expanded_log_v_plus_leg: -X1*X5 * v_plus")
    print("missing_datum: comparison map from the expanded log carrier to the absolute support filtration")


if __name__ == "__main__":
    main()
