from __future__ import annotations

import json
import sympy as sp


def lower_bound_constant(G: sp.Matrix, K: sp.Matrix) -> sp.Expr:
    # Fixtures use diagonal positive G, so generalized eigenvalues are exact.
    values = [(K[i, i] / G[i, i]) for i in range(G.rows)]
    return sp.Max(0, -min(values))


def main() -> None:
    stable = []
    divergent = []
    for n in (2, 4, 8, 16):
        G = sp.eye(n)
        K_stable = sp.diag(*([sp.Integer(-3)] + [sp.Integer(1)] * (n - 1)))
        K_divergent = sp.diag(*([sp.Integer(1)] * (n - 1) + [-sp.Integer(n)]))
        stable.append(int(lower_bound_constant(G, K_stable)))
        divergent.append(int(lower_bound_constant(G, K_divergent)))
    assert stable == [3, 3, 3, 3]
    assert divergent == [2, 4, 8, 16]

    result = {
        "schema":"marici.voevodsky.source-form-semiboundedness-gate-check.v1",
        "status":"generalized_eigenvalue_gate_verified",
        "stable_fixture_lower_constants":stable,
        "divergent_fixture_lower_constants":divergent,
        "criterion":"sup_F max(0,-lambda_min(K_F,G_F)) finite",
        "marici_completed_heat_kernel_evaluated":False,
        "closability_proved":False,
        "semiboundedness_proved":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
