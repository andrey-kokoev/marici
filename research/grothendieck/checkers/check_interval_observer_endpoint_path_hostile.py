"""Exact endpoint-equal but path-distinct observer hostile."""

from fractions import Fraction


def main():
    # Two doubled observer paths with a common initial state and distinct
    # terminal vectors in the kernel of sigma(x,y)=x+y.
    reciprocal = ((Fraction(0), Fraction(0)), (Fraction(1, 2), Fraction(-1, 2)), (Fraction(1), Fraction(-1)))
    adjoint = ((Fraction(0), Fraction(0)), (Fraction(3, 2), Fraction(-3, 2)), (Fraction(2), Fraction(-2)))

    sigma = lambda v: v[0] + v[1]

    checks = [
        ("common_initial_endpoint", reciprocal[0] == adjoint[0] == (0, 0)),
        ("reciprocal_terminal_scalar_null", sigma(reciprocal[-1]) == 0),
        ("adjoint_terminal_scalar_null", sigma(adjoint[-1]) == 0),
        ("terminal_vectors_distinct", reciprocal[-1] != adjoint[-1]),
        ("full_interval_paths_distinct", reciprocal != adjoint),
        ("endpoint_projection_does_not_determine_path", reciprocal[0] == adjoint[0] and sigma(reciprocal[-1]) == sigma(adjoint[-1]) and reciprocal != adjoint),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()
