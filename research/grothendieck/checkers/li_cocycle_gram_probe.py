"""High-precision hostile probe of the Hilbert-cocycle Gram condition for Li coefficients."""

from __future__ import annotations

import mpmath as mp


def xi(s: mp.mpf) -> mp.mpf:
    # Entire completed zeta, with the removable value at s=1 supplied by limit.
    if s == 1:
        return mp.mpf("0.5")
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def li_coefficient(n: int) -> mp.mpf:
    f = lambda s: mp.power(s, n - 1) * mp.log(xi(s))
    return mp.diff(f, 1, n) / mp.factorial(n - 1)


def main() -> None:
    mp.mp.dps = 80
    order = 12
    lam = [mp.mpf("0")] + [li_coefficient(n) for n in range(1, order + 1)]

    for rank in range(1, order + 1):
        gram = mp.matrix(
            rank,
            rank,
        )
        for i in range(rank):
            for j in range(rank):
                m, n = i + 1, j + 1
                gram[i, j] = (lam[m] + lam[n] - lam[abs(m - n)]) / 2
        eigvals = mp.eigsy(gram, eigvals_only=True)
        minimum = min(eigvals)
        print(f"rank={rank} min_eigenvalue={mp.nstr(minimum, 24)}")

    print("li_coefficients=" + ",".join(mp.nstr(value, 24) for value in lam[1:]))


if __name__ == "__main__":
    main()
