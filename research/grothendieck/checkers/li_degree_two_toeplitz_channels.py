"""Exact channel decomposition of the degree-two Li Toeplitz form."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    l1, l2, l3 = sp.symbols("lambda_1 lambda_2 lambda_3", real=True)
    c0 = l1
    c1 = (l2 - 2 * l1) / 2
    c2 = (l3 - 2 * l2 + l1) / 2
    toeplitz = sp.Matrix([[c0, c1, c2], [c1, c0, c1], [c2, c1, c0]])

    sqrt2 = sp.sqrt(2)
    # Columns: normalized antisymmetric, endpoint-symmetric, center.
    basis = sp.Matrix(
        [
            [1 / sqrt2, 1 / sqrt2, 0],
            [0, 0, 1],
            [-1 / sqrt2, 1 / sqrt2, 0],
        ]
    )
    channels = sp.simplify(basis.T * toeplitz * basis)
    expected = sp.Matrix(
        [
            [c0 - c2, 0, 0],
            [0, c0 + c2, sqrt2 * c1],
            [0, sqrt2 * c1, c0],
        ]
    )
    assert (channels - expected).applyfunc(sp.simplify) == sp.zeros(3)

    antisymmetric = sp.factor(c0 - c2)
    coupled_determinant = sp.factor(c0 * (c0 + c2) - 2 * c1**2)
    full_determinant = sp.factor(toeplitz.det())
    assert sp.simplify(full_determinant - antisymmetric * coupled_determinant) == 0

    expected_antisymmetric = (l1 + 2 * l2 - l3) / 2
    expected_coupled = (l1 * l3 + 2 * l1 * l2 - l1**2 - l2**2) / 2
    assert sp.simplify(antisymmetric - expected_antisymmetric) == 0
    assert sp.simplify(coupled_determinant - expected_coupled) == 0

    # Reconnaissance values previously computed independently at 80 digits.
    values = {
        l1: sp.Float("0.0230957089661210338143102", 80),
        l2: sp.Float("0.0923457352280466703857285", 80),
        l3: sp.Float("0.207638920554324803791492", 80),
    }
    print("channel_residual_zero=True")
    print(f"antisymmetric_channel={antisymmetric}")
    print(f"coupled_determinant={coupled_determinant}")
    print(f"full_determinant_factorization={full_determinant}")
    print(f"observed_antisymmetric={sp.N(antisymmetric.subs(values), 24)}")
    print(f"observed_coupled_determinant={sp.N(coupled_determinant.subs(values), 24)}")


if __name__ == "__main__":
    main()
