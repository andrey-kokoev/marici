from fractions import Fraction


def main() -> None:
    checks = []
    c = Fraction(1, 3)
    hostile_zero = Fraction(-1, 2)

    # R(w) = 1 + 2w and F(w) = R(w)/(1-cw).
    primitive_value = 1 + 2 * hostile_zero
    denominator = 1 - c * hostile_zero
    checks.append(("primitive seed vanishes", primitive_value == 0))
    checks.append(("recursive denominator is regular", denominator == Fraction(7, 6)))
    checks.append(("completed transform retains zero", primitive_value / denominator == 0))

    # Exact coefficient identity through a hostile finite window.
    coefficients = [Fraction(1)]
    for n in range(1, 65):
        coefficients.append(c**n + 2 * c ** (n - 1))
    checks.append(("all first 65 source coefficients positive", all(x > 0 for x in coefficients)))

    # Verify F = R + cwF coefficientwise.  R has coefficients (1, 2, 0, ...).
    recursion_ok = True
    for n, value in enumerate(coefficients):
        primitive = Fraction(1) if n == 0 else Fraction(2) if n == 1 else Fraction(0)
        shifted = Fraction(0) if n == 0 else c * coefficients[n - 1]
        recursion_ok &= value == primitive + shifted
    checks.append(("positive coefficients satisfy exact recursion", recursion_ok))

    # Multiple positive recursions preserve the same primitive divisor.
    factors = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5), Fraction(1, 7)]
    multiden = Fraction(1)
    for factor in factors:
        multiden *= 1 - factor * hostile_zero
    checks.append(("all-scale denominator stays regular at hostile zero", multiden > 0))
    checks.append(("all-scale positive completion retains hostile zero", primitive_value / multiden == 0))

    # Reciprocal doubling is still an invertible localization of the seed.
    reciprocal_partner = Fraction(-2)
    reciprocal_seed_at_first = (1 + 2 * hostile_zero) * (1 + 2 / hostile_zero)
    reciprocal_seed_at_second = (1 + 2 * reciprocal_partner) * (1 + 2 / reciprocal_partner)
    bilateral_den_first = (1 - c * hostile_zero) * (1 - c / hostile_zero)
    bilateral_den_second = (1 - c * reciprocal_partner) * (1 - c / reciprocal_partner)
    checks.append(("hostile pair is reciprocal", hostile_zero * reciprocal_partner == 1))
    checks.append(("both hostile roots lie in bilateral convergence annulus", c < abs(hostile_zero) < 1 / c and c < abs(reciprocal_partner) < 1 / c))
    checks.append(("bilateral denominators are regular", bilateral_den_first != 0 and bilateral_den_second != 0))
    checks.append(("reciprocal positive completion retains both zeros", reciprocal_seed_at_first / bilateral_den_first == 0 and reciprocal_seed_at_second / bilateral_den_second == 0))

    failed = [name for name, ok in checks if not ok]
    if failed:
        raise AssertionError("failed: " + ", ".join(failed))
    print(f"{len(checks)}/{len(checks)} exact gates passed")


if __name__ == "__main__":
    main()
