from fractions import Fraction


def add(a, b):
    n = max(len(a), len(b))
    return [
        (a[i] if i < len(a) else Fraction(0))
        + (b[i] if i < len(b) else Fraction(0))
        for i in range(n)
    ]


def scale(a, scalar):
    return [scalar * value for value in a]


def derivative(a):
    return [Fraction(i) * a[i] for i in range(1, len(a))]


def multiply(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return out


def integrate_01(a):
    return sum((a[i] / Fraction(i + 1) for i in range(len(a))), Fraction(0))


def evaluate(a, value):
    total = Fraction(0)
    for coefficient in reversed(a):
        total = total * value + coefficient
    return total


def main():
    z = Fraction(1)
    # G(q) = q - q^2.
    g = [Fraction(0), Fraction(1), Fraction(-1)]
    # f = -G' - zG.
    f = scale(add(derivative(g), scale(g, z)), Fraction(-1))
    residual = add(add(derivative(g), scale(g, z)), f)

    energy = integrate_01(multiply(g, g))
    forcing = integrate_01(multiply(f, g))

    checks = {
        "tail_residual_zero": all(value == 0 for value in residual),
        "left_endpoint_zero": evaluate(g, Fraction(0)) == 0,
        "right_endpoint_zero": evaluate(g, Fraction(1)) == 0,
        "tail_state_nonzero": any(value != 0 for value in g),
        "off_seam_parameter_nonzero": z != 0,
        "energy_exact": energy == Fraction(1, 30),
        "forcing_exact": forcing == Fraction(-1, 30),
        "green_balance_exact": z * energy + forcing == 0,
    }

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
