from fractions import Fraction
from math import comb


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def block_diag(a, b):
    na, nb = len(a), len(b)
    out = [[Fraction(0) for _ in range(na + nb)] for _ in range(na + nb)]
    for i in range(na):
        for j in range(na):
            out[i][j] = a[i][j]
    for i in range(nb):
        for j in range(nb):
            out[na + i][na + j] = b[i][j]
    return out


def cross_form(n):
    out = [[Fraction(0) for _ in range(2 * n)] for _ in range(2 * n)]
    for i in range(n):
        out[i][n + i] = Fraction(1)
        out[n + i][i] = Fraction(1)
    return out


def pascal(n, shift, scalar):
    return [
        [scalar * comb(i, j) * shift ** (i - j) if j <= i else Fraction(0)
         for j in range(n)]
        for i in range(n)
    ]


def main():
    checks = {}
    for n in range(1, 7):
        length = Fraction(3, 5)
        scalar = Fraction(2, 7)
        a = pascal(n, -length, scalar)
        a_inverse = pascal(n, length, 1 / scalar)
        checks[f"inverse_order_{n}"] = multiply(a, a_inverse) == identity(n)

        hyperbolic = block_diag(a, transpose(a_inverse))
        q = cross_form(n)
        preserved = multiply(multiply(transpose(hyperbolic), q), hyperbolic)
        checks[f"cross_form_preserved_order_{n}"] = preserved == q

        same_sheet = block_diag(a, a)
        wrong = multiply(multiply(transpose(same_sheet), q), same_sheet)
        checks[f"same_sheet_rejected_order_{n}"] = wrong != q

    # The first basis vector in the primal polarization is nonzero and null.
    n = 3
    q = cross_form(n)
    x = [[Fraction(1)], [Fraction(0)], [Fraction(0)],
         [Fraction(0)], [Fraction(0)], [Fraction(0)]]
    null_value = multiply(multiply(transpose(x), q), x)[0][0]
    checks["pure_sector_nonzero_vector_is_null"] = null_value == 0

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
