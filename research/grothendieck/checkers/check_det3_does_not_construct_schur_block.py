from fractions import Fraction


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def schur(matrix):
    a, b = matrix[0]
    _, c = matrix[1]
    return c - b * b / a


def main():
    l0 = ((Fraction(2), Fraction(0)), (Fraction(0), Fraction(3, 2)))
    l1 = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(2)))

    checks = {
        "same_fixed_bulk": l0[0][0] == l1[0][0] == 2,
        "both_symmetric": l0[0][1] == l0[1][0] and l1[0][1] == l1[1][0],
        "same_determinant": det2(l0) == det2(l1) == 3,
        "different_incidence": l0[0][1] != l1[0][1],
        "different_return_block": l0[1][1] != l1[1][1],
        "same_reduced_schur_section": schur(l0) == schur(l1) == Fraction(3, 2),
    }

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
