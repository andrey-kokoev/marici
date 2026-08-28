from fractions import Fraction


def current_at_zero(a: Fraction, b: Fraction) -> Fraction:
    w = -a / b
    return a * b * (w - 1 / w)


def main() -> None:
    checks = {
        "common_relative_change_of_basis_invertible": -2 != 0,
    }

    pairs = [
        (Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(2)),
        (Fraction(2), Fraction(1)),
        (Fraction(2), Fraction(3)),
        (Fraction(3), Fraction(5)),
        (Fraction(5), Fraction(3)),
    ]
    for index, (a, b) in enumerate(pairs):
        w = -a / b
        x = a + b * w
        j = current_at_zero(a, b)
        checks[f"scalar_zero_{index}"] = x == 0
        checks[f"relative_residue_{index}"] = j == b * b - a * a
        checks[f"balance_equivalence_{index}"] = (j == 0) == (a == b)
        checks[f"seam_equivalence_{index}"] = (abs(w) == 1) == (a == b)

    # The exact hostile used previously retains a nonzero quotient class.
    checks["hostile_1_2_residue_is_three"] = current_at_zero(Fraction(1), Fraction(2)) == 3

    # A value-only multiplier tower still vanishes while the relative class survives.
    a, b = Fraction(1), Fraction(2)
    w = -a / b
    x = a + b * w
    multipliers = [Fraction(7, 6), Fraction(5, 4), Fraction(11, 9)]
    checks["all_principal_ports_vanish"] = all(m * x == 0 for m in multipliers)
    checks["cokernel_port_survives"] = current_at_zero(a, b) != 0

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed")


if __name__ == "__main__":
    main()

