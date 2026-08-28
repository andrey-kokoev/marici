from fractions import Fraction


def current(a: Fraction, b: Fraction, w: Fraction) -> Fraction:
    return a * b * (w - 1 / w)


def main() -> None:
    checks = {}
    pairs = [
        (Fraction(1), Fraction(2)),
        (Fraction(2), Fraction(1)),
        (Fraction(2), Fraction(3)),
        (Fraction(3), Fraction(5)),
        (Fraction(5), Fraction(8)),
        (Fraction(8), Fraction(5)),
    ]
    for index, (a, b) in enumerate(pairs):
        w_plus = -a / b
        w_minus = 1 / w_plus
        j_plus = current(a, b, w_plus)
        j_minus = current(a, b, w_minus)
        checks[f"reciprocal_orbit_{index}"] = w_plus * w_minus == 1
        checks[f"sign_transport_{index}"] = j_minus == -j_plus
        checks[f"scalar_pushforward_zero_{index}"] = j_plus + j_minus == 0
        checks[f"fiber_residues_nonzero_{index}"] = j_plus != 0 and j_minus != 0
        checks[f"both_points_off_unit_{index}"] = abs(w_plus) != 1 and abs(w_minus) != 1

    for index, fixed in enumerate((Fraction(1), Fraction(-1))):
        checks[f"fixed_point_current_zero_{index}"] = current(Fraction(3), Fraction(7), fixed) == 0
        checks[f"fixed_point_is_reciprocal_{index}"] = fixed == 1 / fixed

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed")


if __name__ == "__main__":
    main()

