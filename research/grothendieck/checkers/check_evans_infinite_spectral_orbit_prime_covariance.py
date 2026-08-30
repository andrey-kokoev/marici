from fractions import Fraction
from math import comb


def add(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + value
        if out[key] == 0:
            del out[key]
    return out


def transported(k):
    # Terms represent r * coefficient * L^power * (F_j - B_j).
    out = {}
    for j in range(k + 1):
        coefficient = Fraction(comb(k, j) * ((-1) ** (k - j)))
        power = k - j
        out[(power, "F", j)] = coefficient
        out[(power, "B", j)] = -coefficient
    return out


def spectral_derivative(expr):
    out = {}
    for (power, kind, index), coefficient in expr.items():
        # Derivative of r is -L r.
        out = add(out, {(power + 1, kind, index): -coefficient})
        # Derivative raises the endpoint or seam moment.
        out = add(out, {(power, kind, index + 1): coefficient})
    return out


def main():
    covariance = {
        f"spectral_prime_covariance_order_{k}":
        spectral_derivative(transported(k)) == transported(k + 1)
        for k in range(7)
    }

    # Moment covectors evaluated on narrow packets around distinct positive
    # points have a Vandermonde matrix. Its determinant is nonzero.
    points = [Fraction(1), Fraction(2), Fraction(4), Fraction(7)]
    vandermonde = Fraction(1)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            vandermonde *= points[j] - points[i]

    top_derivative = spectral_derivative(transported(3))
    checks = {
        **covariance,
        "first_four_moment_covectors_independent": vandermonde != 0,
        "finite_truncation_has_top_wall": any(
            kind == "F" and index == 4 for _, kind, index in top_derivative
        ),
        "finite_truncation_needs_next_seam_jet": any(
            kind == "B" and index == 4 for _, kind, index in top_derivative
        ),
    }

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
