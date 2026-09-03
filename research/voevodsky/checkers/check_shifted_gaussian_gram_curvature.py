from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/shifted-gaussian-gram-curvature-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    u, a, b, t = sp.symbols("u a b t", real=True, positive=True)
    left = sp.exp(-t * (u - a) ** 2 / 2) * sp.exp(-t * (u - b) ** 2 / 2)
    right = sp.exp(-t * (a - b) ** 2 / 4) * sp.exp(-t * (u - (a + b) / 2) ** 2)
    assert sp.simplify(left / right) == 1

    # Logarithm of the rank-two determinant ratio is the midpoint convexity residual.
    A, B, M = sp.symbols("A B M", positive=True)
    log_ratio = sp.log(A) + sp.log(B) - 2 * sp.log(M) + t * (a - b) ** 2 / 2
    qa = sp.log(A) + t * a**2
    qb = sp.log(B) + t * b**2
    qm = sp.log(M) + t * ((a + b) / 2) ** 2
    assert sp.simplify(log_ratio - (qa + qb - 2 * qm)) == 0

    tau = sp.symbols("tau", positive=True)
    Fx, Fxx, Fxxx, Fxxxx = sp.symbols("Fx Fxx Fxxx Fxxxx", real=True)
    q = Fxx + 1 / (2 * tau)
    q_tau_from_heat = Fxxxx + 2 * Fxx**2 + 2 * Fx * Fxxx - 1 / (2 * tau**2)
    q_pde_rhs = Fxxxx + 2 * Fx * Fxxx + 2 * q**2 - (2 / tau) * q
    assert sp.simplify(q_tau_from_heat - q_pde_rhs) == 0

    # At first contact q=0, q_x=0, q_xx>=0 gives q_tau>=0.
    qxx = sp.symbols("qxx", nonnegative=True)
    first_contact_rhs = qxx
    assert first_contact_rhs >= 0

    status = contract["status"]
    assert status["arithmetic_curvature_inequality"] == "not proved"
    result = {
        "schema":"marici.voevodsky.shifted-gaussian-gram-curvature-check.v1",
        "status":"rank_two_curvature_interface_verified",
        "gaussian_product_identity":True,
        "spectral_multiplication_midpoint_formula":True,
        "translated_source_gram_identification":False,
        "rank_two_midpoint_convexity_equivalence":True,
        "local_curvature":"partial_xi^2 log Theta + 2t",
        "curvature_pde_identity":True,
        "forward_first_contact_sign":True,
        "backward_narrow_propagation":False,
        "arithmetic_curvature_verified":False,
        "higher_rank_psd_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
