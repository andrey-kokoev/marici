from fractions import Fraction


def multiply(a, x):
    return [
        sum((a[i][j] * x[j] for j in range(len(x))), Fraction(0))
        for i in range(len(a))
    ]


def determinant3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def main():
    h = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    x = [Fraction(1), Fraction(-1)]
    ell = [Fraction(1), Fraction(1)]
    hx = multiply(h, x)
    u = [x[i] + hx[i] for i in range(2)]
    endpoint = sum((ell[i] * u[i] for i in range(2)), Fraction(0))

    bordered = [
        [Fraction(1), Fraction(0), u[0]],
        [Fraction(0), Fraction(1), u[1]],
        [ell[0], ell[1], Fraction(0)],
    ]
    kernel = [-u[0], -u[1], Fraction(1)]
    graph_energy = 2 * sum((x[i] * hx[i] for i in range(2)), Fraction(0))

    checks = {
        "sum_carrier_nonzero": u != [0, 0],
        "scalar_endpoint_zero": endpoint == 0,
        "graph_energy_positive": graph_energy > 0,
        "bordered_determinant_zero": determinant3(bordered) == 0,
        "canonical_kernel_exact": multiply(bordered, kernel) == [0, 0, 0],
        "kernel_carrier_component_nonzero": kernel[:2] != [0, 0],
        "evaluation_wall_coordinate_nonzero": kernel[2] == 1,
    }

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
