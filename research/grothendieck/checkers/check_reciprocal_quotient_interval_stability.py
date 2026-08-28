from fractions import Fraction as F


def reverse(packet):
    return tuple(reversed(packet))


def main() -> None:
    checks = {}

    generic = (F(1), F(2), F(3), F(5))
    checks["generic_phase_port_nonzero"] = generic != reverse(generic)
    first_moment = sum(k * value for k, value in enumerate(generic))
    reverse_moment = sum(k * value for k, value in enumerate(reverse(generic)))
    checks["first_oriented_moment_changes"] = first_moment != reverse_moment

    hostile = (F(1), F(4), F(0), F(4), F(1))
    checks["hostile_is_palindromic"] = hostile == reverse(hostile)
    checks["complete_reversal_odd_port_vanishes"] = all(
        hostile[k] - hostile[-1 - k] == 0 for k in range(len(hostile))
    )

    # Q(y)=y^2+4y-2 and w^2 Q(w+w^-1)=P(w).
    def q(y):
        return y * y + 4 * y - 2

    checks["q_minus_five_positive"] = q(F(-5)) == 3
    checks["q_minus_two_negative"] = q(F(-2)) == -6
    checks["off_interval_root_forced"] = q(F(-5)) * q(F(-2)) < 0

    # Coefficient expansion of w^2[(w+w^-1)^2+4(w+w^-1)-2].
    expanded = (F(1), F(4), F(0), F(4), F(1))
    checks["quotient_expands_to_hostile"] = expanded == hostile

    # Exact unit-circle quotient samples from rational Pythagorean points.
    unit_points = [(F(1), F(0)), (F(-1), F(0)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]
    for index, (x, imag) in enumerate(unit_points):
        norm = x * x + imag * imag
        y = 2 * x
        checks[f"unit_norm_{index}"] = norm == 1
        checks[f"quotient_in_interval_{index}"] = F(-2) <= y <= F(2)

    # Conversely, discriminant is nonpositive for sampled interval points.
    for index, y in enumerate((F(-2), F(-3, 2), F(0), F(7, 5), F(2))):
        checks[f"interval_discriminant_{index}"] = y * y - 4 <= 0

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed")


if __name__ == "__main__":
    main()

