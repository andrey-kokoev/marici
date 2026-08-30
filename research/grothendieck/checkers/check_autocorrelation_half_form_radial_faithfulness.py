from fractions import Fraction as F


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def inv(z):
    norm = z[0] * z[0] + z[1] * z[1]
    return z[0] / norm, -z[1] / norm


def power(z, exponent):
    if exponent < 0:
        return power(inv(z), -exponent)
    out = (F(1), F(0))
    for _ in range(exponent):
        out = mul(out, z)
    return out


def evaluate(coefficients, z):
    out = (F(0), F(0))
    for exponent, coefficient in enumerate(coefficients):
        term = power(z, exponent)
        out = add(out, (coefficient * term[0], coefficient * term[1]))
    return out


def correlations(coefficients):
    return [
        sum(coefficients[j] * coefficients[j + k] for j in range(len(coefficients) - k))
        for k in range(len(coefficients))
    ]


def half_form(coefficients, z):
    corr = correlations(coefficients)
    out = (corr[0] / 2, F(0))
    for k in range(1, len(corr)):
        term = power(z, k)
        out = add(out, (corr[k] * term[0], corr[k] * term[1]))
    return out


def current(coefficients, z):
    corr = correlations(coefficients)
    out = (F(0), F(0))
    for k in range(1, len(corr)):
        forward, backward = power(z, k), power(z, -k)
        out = add(out, (corr[k] * (forward[0] - backward[0]), corr[k] * (forward[1] - backward[1])))
    return out


def main() -> None:
    checks = {}

    # Exact Fejer identity on rational unit-circle points and signed packets.
    packets = [[F(1), F(2)], [F(2), F(-3), F(5)], [F(1), F(0), F(1)], [F(3), F(1), F(-2), F(4)]]
    unit_points = [(F(1), F(0)), (F(-1), F(0)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]
    for pi, packet in enumerate(packets):
        for wi, w in enumerate(unit_points):
            p = evaluate(packet, w)
            a = half_form(packet, w)
            modulus_squared = p[0] * p[0] + p[1] * p[1]
            checks[f"fejer_{pi}_{wi}"] = 2 * a[0] == modulus_squared

    # Known roots in all three radial regimes.
    roots = [
        ([F(1), F(2)], (F(-1, 2), F(0)), "inside"),
        ([F(2), F(1)], (F(-2), F(0)), "outside"),
        ([F(2), F(2), F(1)], (F(-1), F(1)), "outside"),
        ([F(1), F(2), F(2)], (F(-1, 2), F(1, 2)), "inside"),
        ([F(1), F(1)], (F(-1), F(0)), "seam"),
        ([F(1), F(0), F(1)], (F(0), F(1)), "seam"),
    ]
    for index, (packet, root, region) in enumerate(roots):
        p = evaluate(packet, root)
        j = current(packet, root)
        checks[f"root_{index}"] = p == (0, 0)
        if region == "inside":
            checks[f"radial_sign_{index}"] = j[0] > 0
            checks[f"half_form_identity_{index}"] = j == tuple(2 * x for x in half_form(packet, root))
        elif region == "outside":
            checks[f"radial_sign_{index}"] = j[0] < 0
            checks[f"half_form_identity_{index}"] = j == tuple(-2 * x for x in half_form(packet, inv(root)))
        else:
            checks[f"radial_sign_{index}"] = j[0] == 0
            checks[f"current_tangential_{index}"] = j[0] == 0

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed")


if __name__ == "__main__":
    main()

