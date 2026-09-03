from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/categorical-rh-proof-bracket-form-core-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    x, n = sp.symbols("x n", real=True, positive=True)

    # Smooth concentration fixture: f_n(0)=1 while ||f_n||_2 tends to zero.
    f = sp.exp(-n * x**2)
    norm_squared = sp.integrate(f**2, (x, -sp.oo, sp.oo))
    assert sp.simplify(norm_squared - sp.sqrt(sp.pi / (2 * n))) == 0
    assert sp.limit(norm_squared, n, sp.oo) == 0
    assert f.subs(x, 0) == 1

    # A stronger graph norm containing endpoint evaluation detects the fixture.
    graph_norm_squared = norm_squared + f.subs(x, 0) ** 2
    assert sp.limit(graph_norm_squared, n, sp.oo) == 1

    # Finite-dimensional analogue: positivity on a non-core subspace misses a negative direction.
    q = sp.diag(1, -1)
    packet_inclusion = sp.Matrix([1, 0])
    restricted_q = (packet_inclusion.T * q * packet_inclusion)[0]
    assert restricted_q == 1
    hidden_direction = sp.Matrix([0, 1])
    assert (hidden_direction.T * q * hidden_direction)[0] == -1

    # If the probe inclusion spans the whole finite domain, restriction reflects positivity.
    full_inclusion = sp.eye(2)
    assert full_inclusion.rank() == 2
    assert (full_inclusion.T * q * full_inclusion).eigenvals() == {1: 1, -1: 1}

    status = contract["status"]
    assert status["gaussian_form_core"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.categorical-rh-proof-bracket-form-core-check.v1",
        "status":"form_core_gate_verified",
        "endpoint_evaluation_not_L2_continuous":True,
        "graph_norm_detects_endpoint":True,
        "positive_noncore_restriction_misses_negative_direction":True,
        "full_finite_probe_reflects_sign":True,
        "gaussian_form_core_supplied":False,
        "source_Weil_comparison_reverified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
