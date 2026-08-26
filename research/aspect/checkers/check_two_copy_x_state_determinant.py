from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


Gaussian = tuple[F, F]


def add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def main() -> None:
    half = F(1, 2)

    # Sparse two-copy observable on basis |i,j>, i,j in {00,01,10,11}.
    # Diagonal population sector contributes bc; the coherence exchange
    # sector contributes -|z|^2.
    observable: dict[tuple[tuple[int, int], tuple[int, int]], F] = {
        ((1, 2), (1, 2)): half,
        ((2, 1), (2, 1)): half,
        ((3, 0), (0, 3)): -half,
        ((0, 3), (3, 0)): -half,
    }

    a = d = F(9, 20)
    b, c = F(1, 100), F(9, 100)
    z: Gaussian = (F(3, 100), F(4, 100))
    w: Gaussian = (F(1, 100), F(-1, 200))
    zero: Gaussian = (F(0), F(0))
    rho: dict[tuple[int, int], Gaussian] = {
        (0, 0): (a, F(0)),
        (1, 1): (b, F(0)),
        (2, 2): (c, F(0)),
        (3, 3): (d, F(0)),
        (0, 3): z,
        (3, 0): (z[0], -z[1]),
        (1, 2): w,
        (2, 1): (w[0], -w[1]),
    }

    expectation = zero
    for (row_pair, column_pair), value in observable.items():
        i, j = column_pair
        k, ell = row_pair
        rho_product = multiply(rho.get((i, k), zero), rho.get((j, ell), zero))
        expectation = add(expectation, (value * rho_product[0], value * rho_product[1]))

    determinant = b * c - z[0] ** 2 - z[1] ** 2
    assert expectation == (determinant, F(0))
    assert determinant == F(-1, 625)

    # Spectrum: two population basis states have +1/2. In the coherence
    # exchange block, symmetric and antisymmetric combinations have -1/2 and
    # +1/2. The other twelve dimensions have eigenvalue zero.
    matrix = [[F(0) for _ in range(16)] for _ in range(16)]
    for (row_pair, column_pair), value in observable.items():
        matrix[4 * row_pair[0] + row_pair[1]][4 * column_pair[0] + column_pair[1]] = value
    square = [
        [sum((matrix[row][k] * matrix[k][column] for k in range(16)), F(0))
         for column in range(16)]
        for row in range(16)
    ]
    support = {4 * 1 + 2, 4 * 2 + 1, 4 * 3 + 0, 4 * 0 + 3}
    for row in range(16):
        for column in range(16):
            expected = F(1, 4) if row == column and row in support else F(0)
            assert square[row][column] == expected
    trace = sum((matrix[index][index] for index in range(16)), F(0))
    assert trace == 1
    nonzero_rank = len(support)
    positive_multiplicity = (nonzero_rank + 2 * trace) / 2
    negative_multiplicity = nonzero_rank - positive_multiplicity
    assert positive_multiplicity == 3
    assert negative_multiplicity == 1
    spectrum = {"-1/2": 1, "0": 12, "+1/2": 3}
    assert sum(spectrum.values()) == 16

    result = {
        "schema": "marici.aspect.two-copy-x-state-determinant.v1",
        "status": "pass",
        "observable_expectation": "b*c-|z|^2",
        "npt_decision": "negative expectation",
        "hostile_expectation": str(determinant),
        "observable_spectrum": spectrum,
        "outcome_interval": ["-1/2", "+1/2"],
        "nuisance_w_cancels": True,
        "copies_per_trial": 2,
        "settings": 1,
        "candidate_optical_instrument": "synchronized two-pair source plus collective spectral measurement using copy interference and number-resolved coincidences",
        "verdict": "One two-copy observable linearizes the nonlinear determinant residual into a bounded single-setting expectation.",
        "claim_boundary": "exact observable identity; no proof that passive linear optics alone realizes the complete spectral measurement and no count-rate advantage claim",
    }
    output = Path(__file__).parents[1] / "results" / "two_copy_x_state_determinant.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
