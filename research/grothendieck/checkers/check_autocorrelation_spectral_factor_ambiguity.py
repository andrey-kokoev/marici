from fractions import Fraction as F


def correlations(coefficients):
    return tuple(
        sum(coefficients[j] * coefficients[j + k] for j in range(len(coefficients) - k))
        for k in range(len(coefficients))
    )


def current(correlations_, w):
    return sum(correlations_[k] * (w**k - w ** (-k)) for k in range(1, len(correlations_)))


def main() -> None:
    checks = {}
    packets = [
        [F(1), F(2)],
        [F(1), F(3), F(2)],
        [F(2), F(-1), F(4), F(3)],
        [F(3), F(0), F(2), F(5), F(1)],
        [F(1), F(2), F(3), F(4), F(5), F(6)],
    ]
    for index, packet in enumerate(packets):
        reverse = list(reversed(packet))
        checks[f"autocorrelation_reversal_invariant_{index}"] = correlations(packet) == correlations(reverse)
        checks[f"packet_distinct_from_reverse_{index}"] = packet != reverse

    p = [F(1), F(2)]
    reverse = list(reversed(p))
    corr = correlations(p)
    root_inside = F(-1, 2)
    root_outside = F(-2)
    checks["same_c0"] = corr[0] == 5
    checks["same_c1"] = corr[1] == 2
    checks["inside_factor_zero"] = p[0] + p[1] * root_inside == 0
    checks["outside_factor_zero"] = reverse[0] + reverse[1] * root_outside == 0
    checks["zeros_are_reciprocal"] = root_inside * root_outside == 1
    checks["inside_current_positive"] = current(corr, root_inside) == 3
    checks["outside_current_negative"] = current(corr, root_outside) == -3
    checks["same_current_function_used"] = correlations(p) == correlations(reverse)

    # Boundary modulus equality at rational unit-circle samples.
    unit_samples = [(F(1), F(0)), (F(-1), F(0)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]
    for index, (x, y) in enumerate(unit_samples):
        # |a+bw|^2 = a^2+b^2+2ab Re(w).
        modulus_p = p[0] ** 2 + p[1] ** 2 + 2 * p[0] * p[1] * x
        modulus_reverse = reverse[0] ** 2 + reverse[1] ** 2 + 2 * reverse[0] * reverse[1] * x
        checks[f"boundary_modulus_equal_{index}"] = modulus_p == modulus_reverse

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed")


if __name__ == "__main__":
    main()

