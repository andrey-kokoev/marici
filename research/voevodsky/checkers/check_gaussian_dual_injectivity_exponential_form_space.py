from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/gaussian-dual-injectivity-exponential-form-space-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    x, y, beta, t = sp.symbols("x y beta t", real=True, positive=True)

    # Convolution is a bilateral Laplace transform after Gaussian damping.
    exponent_identity = sp.simplify(
        -(x - y) ** 2 / (4 * t)
        - (-x**2 / (4 * t) - y**2 / (4 * t) + x * y / (2 * t))
    )
    assert exponent_identity == 0

    # Cauchy-Schwarz companion factor is integrable for every beta,t>0.
    half_integral = sp.integrate(
        sp.exp(beta * y - y**2 / (2 * t)), (y, 0, sp.oo)
    )
    expected_half = (
        sp.sqrt(2 * sp.pi * t)
        * sp.exp(beta**2 * t / 2)
        * (1 + sp.erf(beta * sp.sqrt(t / 2)))
        / 2
    )
    assert sp.simplify(half_integral - expected_half) == 0
    assert expected_half.is_positive

    # Gaussian damping dominates every fixed exponential Laplace direction.
    z = sp.symbols("z", real=True)
    completed_square = sp.simplify(
        -y**2 / (4 * t) + z * y
        - (-(y - 2 * t * z) ** 2 / (4 * t) + t * z**2)
    )
    assert completed_square == 0

    # Finite atomic hostile: zero Gaussian convolution forces both coefficients zero.
    a, b = sp.symbols("a b", real=True)
    samples = sp.Matrix([
        [1, sp.exp(-1 / (4 * t))],
        [sp.exp(-1 / (4 * t)), 1],
    ])
    determinant = sp.factor(samples.det())
    expected_determinant = (1 - sp.exp(-1 / (4 * t))) * (1 + sp.exp(-1 / (4 * t)))
    assert sp.simplify(determinant - expected_determinant) == 0
    assert determinant != 0
    assert samples.gauss_jordan_solve(sp.zeros(2, 1))[0] == sp.zeros(2, 1)

    status = contract["status"]
    assert status["actual_form_dual_identification"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.gaussian-dual-injectivity-exponential-form-space-check.v1",
        "status":"exponential_dual_injectivity_mechanism_verified",
        "convolution_laplace_identity":True,
        "exponential_gaussian_integrability":True,
        "entire_transform_gaussian_domination":True,
        "finite_atomic_injectivity_fixture":True,
        "actual_form_dual_identification":False,
        "graph_orthogonality_intertwining":False,
        "positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
