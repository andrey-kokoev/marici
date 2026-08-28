#!/usr/bin/env python3
"""Exact finite model for the six A3--Veronese interchange squares."""

from fractions import Fraction


GENERATORS = (0, 1, 2)  # multiplication by u^2, uv, v^2


def generator_matrix(grade, shift):
    rows = 2 * (grade + 1) + 1
    cols = 2 * grade + 1
    out = [[Fraction(0) for _ in range(cols)] for _ in range(rows)]
    for col in range(cols):
        out[col + shift][col] = Fraction(1)
    return out


def identity(n, scale=1):
    return [[Fraction(scale if i == j else 0) for j in range(n)] for i in range(n)]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def commutes_across_grade(lower_map, upper_map, grade, shift):
    control = generator_matrix(grade, shift)
    return matmul(upper_map, control) == matmul(control, lower_map)


def main():
    gates = []

    # Two adjacent stage arrows, each scalar and constant across grades.
    arrows = (Fraction(2), Fraction(3))
    for arrow_index, scale in enumerate(arrows):
        lower = identity(3, scale)  # grade 1
        upper = identity(5, scale)  # grade 2
        for shift in GENERATORS:
            gates.append((
                f"arrow {arrow_index} commutes with generator shift {shift}",
                commutes_across_grade(lower, upper, 1, shift),
            ))

    # The long composite is forced once the adjacent scales commute.
    long_lower = identity(3, arrows[0] * arrows[1])
    long_upper = identity(5, arrows[0] * arrows[1])
    gates.append(("long composite commutes without a new generator", all(
        commutes_across_grade(long_lower, long_upper, 1, shift)
        for shift in GENERATORS
    )))

    # xz=y^2: all three degree-two paths shift an exponent by two.
    x_then_z = matmul(generator_matrix(1, 2), generator_matrix(0, 0))
    y_then_y = matmul(generator_matrix(1, 1), generator_matrix(0, 1))
    gates.append(("Veronese quadratic relation is exact", x_then_z == y_then_y))

    # Hostile: preserve dimensions but alter one middle weight.
    hostile_lower = identity(3, 2)
    hostile_upper = identity(5, 2)
    hostile_upper[2][2] = Fraction(5)
    failures = [not commutes_across_grade(hostile_lower, hostile_upper, 1, shift)
                for shift in GENERATORS]
    gates.append(("typed middle-weight defect is detected before composition", any(failures)))

    for name, passed in gates:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"SUMMARY: {sum(ok for _, ok in gates)}/{len(gates)} gates passed")
    if not all(ok for _, ok in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
