from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/rh-remainder-cone-equivalence-skeleton-v1.json")


def hankel(weights: list[sp.Expr], bases: list[sp.Expr], size: int) -> sp.Matrix:
    moments = [sum(w * y**n for w, y in zip(weights, bases)) for n in range(2 * size - 1)]
    return sp.Matrix(size, size, lambda i, j: moments[i + j])


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # Real positive rates produce positive sampled bases and Gram Hankel matrices.
    weights = [sp.Rational(2), sp.Rational(3), sp.Rational(5)]
    bases = [sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(4, 5)]
    H = hankel(weights, bases, 3)
    assert H.is_positive_definite

    # A pure nonreal conjugate pair gives a negative rank-two determinant.
    u, v, w = sp.symbols("u v w", positive=True, real=True)
    complex_H = hankel([w, w], [u + sp.I * v, u - sp.I * v], 2)
    assert sp.simplify(complex_H.det()) == -4 * v**2 * w**2

    # Small-mesh phase rigidity for lambda=sigma+i omega.
    h, sigma, omega = sp.symbols("h sigma omega", positive=True, real=True)
    sampled = sp.exp(-h * (sigma + sp.I * omega))
    assert sp.simplify(sp.im(sampled)) == -sp.exp(-h * sigma) * sp.sin(h * omega)

    # Critical-line equivalence for the squared-centered rate.
    beta, gamma = sp.symbols("beta gamma", real=True)
    rho = beta + sp.I * gamma
    lam = sp.expand(-(rho - sp.Rational(1, 2)) ** 2)
    assert sp.simplify(sp.im(lam) + 2 * (beta - sp.Rational(1, 2)) * gamma) == 0

    result = {
        "schema":"marici.voevodsky.rh-remainder-cone-equivalence-skeleton-check.v1",
        "status":"finite_equivalence_mechanisms_verified",
        "real_positive_gram_fixture":True,
        "nonreal_pair_negative_fixture":True,
        "small_mesh_phase_formula":True,
        "centered_square_imaginary_part":True,
        "source_complete_equivalence":False,
        "remainder_cone":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
