from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    mu = sp.Rational(1, 2)
    coupling = sp.Rational(1, 4)
    tail_norm = sp.Rational(1, 2)
    schur_residual = sp.simplify(mu - coupling**2 / (1 - tail_norm))
    assert schur_residual == sp.Rational(3, 8)

    block_fixture = sp.Matrix([[mu, coupling], [coupling, 1 - tail_norm]])
    eigenvalues = list(block_fixture.eigenvals().keys())
    assert min(eigenvalues) >= 0

    failing_mu = sp.Rational(1, 10)
    failing_residual = sp.simplify(failing_mu - coupling**2 / (1 - tail_norm))
    assert failing_residual < 0

    L, b, M = sp.symbols("L b M", positive=True)
    d1 = sp.log(1 + sp.pi / (2 * L))
    d_tail = sp.log(1 + (M + 1) * sp.pi / (2 * L))
    generic_tail = b / d_tail
    generic_coupling = b / sp.sqrt(d1 * d_tail)

    result = {
        "schema": "marici.voevodsky.weighted-birman-schwinger-certificate.v1",
        "status": "finite_schur_certificate_interface_verified",
        "fixture_mu": str(mu),
        "fixture_coupling_bound": str(coupling),
        "fixture_tail_norm_bound": str(tail_norm),
        "fixture_schur_residual": str(schur_residual),
        "fixture_block_eigenvalues": [str(value) for value in eigenvalues],
        "deliberate_failure_mu": str(failing_mu),
        "deliberate_failure_residual": str(failing_residual),
        "generic_tail_bound": str(generic_tail),
        "generic_coupling_bound": str(generic_coupling),
        "source_matrix_assembled": False,
        "first_missing_object": "complete normalized explicit-formula identity with signs, prefactors, adjoints, and endpoint terms",
        "next_gate": "materialize source identity, then interval-enclose mu_M, c_M, and r_M",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
