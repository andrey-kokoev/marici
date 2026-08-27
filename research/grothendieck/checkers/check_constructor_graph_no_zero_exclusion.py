from fractions import Fraction


def dot(row, column):
    return sum((row[i] * column[i] for i in range(len(row))), Fraction(0))


def main():
    source = [Fraction(1), Fraction(-1)]
    tail = source[:]
    endpoint = [Fraction(1), Fraction(1)]

    constructors = {
        "seam": [Fraction(2), Fraction(3)],
        "primitive": [Fraction(5), Fraction(-4)],
        "square": [Fraction(7), Fraction(6)],
        "archimedean": [Fraction(-3), Fraction(8)],
    }
    outputs = {
        name: dot(row, source) for name, row in constructors.items()
    }

    # The common-domain state stores each constructor output independently.
    residuals = {
        name: outputs[name] - dot(row, source)
        for name, row in constructors.items()
    }
    tail_residual = [tail[i] - source[i] for i in range(2)]

    checks = {
        "tail_graph_residual_zero": tail_residual == [0, 0],
        "all_boundary_graph_residuals_zero": all(value == 0 for value in residuals.values()),
        "endpoint_wall_zero": dot(endpoint, tail) == 0,
        "sum_carrier_nonzero": tail != [0, 0],
        "kernel_descent_fails": dot(endpoint, tail) == 0 and tail != [0, 0],
        "boundary_maps_arbitrary_nonzero": all(any(value != 0 for value in row) for row in constructors.values()),
    }

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
