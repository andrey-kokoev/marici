from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    positions = (sp.Rational(-1, 2), sp.Rational(1))
    weights = (sp.Rational(2, 5), sp.Rational(3, 5))
    moments = tuple(
        sp.simplify(sum(weight * position**degree for weight, position in zip(weights, positions)))
        for degree in range(6)
    )
    assert moments == (
        1,
        sp.Rational(2, 5),
        sp.Rational(7, 10),
        sp.Rational(11, 20),
        sp.Rational(5, 8),
        sp.Rational(47, 80),
    )

    hankel_1 = sp.Matrix([[moments[i + j] for j in range(2)] for i in range(2)])
    hankel_2 = sp.Matrix([[moments[i + j] for j in range(3)] for i in range(3)])
    assert hankel_1.det() == sp.Rational(27, 50) > 0
    assert hankel_1.rank() == hankel_2.rank() == 2
    assert hankel_2.det() == 0

    vandermonde = sp.Matrix(
        [[position**degree for position in positions] for degree in range(3)]
    )
    gram = vandermonde * sp.diag(*weights) * vandermonde.T
    assert gram == hankel_2

    kernel = hankel_2.nullspace()
    assert len(kernel) == 1
    annihilator = kernel[0] / kernel[0][2]
    assert annihilator == sp.Matrix([sp.Rational(-1, 2), sp.Rational(-1, 2), 1])
    x = sp.symbols("x")
    annihilating_polynomial = sp.expand(sum(annihilator[k] * x**k for k in range(3)))
    recovered_positions = tuple(sp.solve(annihilating_polynomial, x))
    assert recovered_positions == positions

    recovered_weights = tuple(
        sp.solve(
            [
                sp.Symbol("w0") + sp.Symbol("w1") - moments[0],
                positions[0] * sp.Symbol("w0") + positions[1] * sp.Symbol("w1") - moments[1],
            ],
            [sp.Symbol("w0"), sp.Symbol("w1")],
        )[symbol]
        for symbol in (sp.Symbol("w0"), sp.Symbol("w1"))
    )
    assert recovered_weights == weights

    predicted_fifth = sp.simplify(
        sum(weight * position**5 for weight, position in zip(recovered_weights, recovered_positions))
    )
    assert predicted_fifth == moments[5]

    # A small exact fourth-moment change destroys flatness and the two-atom certificate.
    hostile_moments = list(moments[:5])
    hostile_moments[4] += sp.Rational(1, 100)
    hostile_hankel_2 = sp.Matrix(
        [[hostile_moments[i + j] for j in range(3)] for i in range(3)]
    )
    assert hostile_hankel_2.det() != 0
    assert hostile_hankel_2.rank() == 3

    result = {
        "schema": "marici.aspect.scatter-flat-moment-certificate.v1",
        "status": "pass",
        "moments_0_through_5": [str(value) for value in moments],
        "hankel_ranks": [hankel_1.rank(), hankel_2.rank()],
        "hankel_1_determinant": str(hankel_1.det()),
        "hankel_2_determinant": str(hankel_2.det()),
        "annihilating_polynomial": str(annihilating_polynomial),
        "recovered_positions": [str(value) for value in recovered_positions],
        "recovered_weights": [str(value) for value in recovered_weights],
        "predicted_fifth_moment": str(predicted_fifth),
        "hostile_perturbed_hankel_rank": hostile_hankel_2.rank(),
        "verdict": "Positive Hankel factorization plus rank stabilization from two to two gives an exact two-atom certificate for the frozen truncated moment sequence and reconstructs off-grid positions and weights. The next moment becomes a falsifiable prediction. A fourth-moment perturbation destroys flatness. The certificate remains conditional on the source measure belonging to the admitted positive moment class.",
        "claim_boundary": "exact univariate positive two-atomic measure with moments through degree four for reconstruction and degree five for out-of-sample verification; no noisy moments, signed measures, multidimensional angles, or proof that a physical source is finitely atomic",
    }
    output = Path(__file__).parents[1] / "results" / "scatter_flat_moment_certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
