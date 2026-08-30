"""Exact symbolic factorization of anchored Li cocycle Grams into increment correlations."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    rank = 7
    lam = sp.symbols(f"l0:{rank + 1}")

    # Even displacement sequence with l0=0.
    gram = sp.Matrix(
        rank,
        rank,
        lambda i, j: (lam[i + 1] + lam[j + 1] - lam[abs(i - j)]) / 2,
    ).subs(lam[0], 0)

    # Increment correlation c_k = 1/2 Delta^2 lambda_k, with c_0=lambda_1.
    corr = [lam[1]] + [
        (lam[k + 1] - 2 * lam[k] + lam[k - 1]) / 2
        for k in range(1, rank)
    ]
    toeplitz = sp.Matrix(rank, rank, lambda i, j: corr[abs(i - j)]).subs(lam[0], 0)
    summation = sp.Matrix(rank, rank, lambda i, j: 1 if j <= i else 0)

    residual = (gram - summation * toeplitz * summation.T).applyfunc(sp.expand)
    assert residual == sp.zeros(rank)
    assert summation.det() == 1

    print(f"checked_rank={rank}")
    print("factorization_residual_zero=True")
    print("summation_determinant=1")
    print("gram_psd_iff_increment_toeplitz_psd=True")


if __name__ == "__main__":
    main()
