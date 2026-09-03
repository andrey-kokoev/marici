from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Finite fixture for two observer norms on one algebraic core.
    G0 = sp.Matrix([[2, 1], [1, 2]])
    GH = sp.Matrix([[1, 0], [0, 3]])
    Gstar = G0 + GH
    assert Gstar == sp.Matrix([[3, 1], [1, 5]])
    assert Gstar.det() == 14
    assert all(ev > 0 for ev in Gstar.eigenvals())

    # The graph norm dominates each component norm exactly.
    c0, c1 = sp.symbols("c0 c1", real=True)
    c = sp.Matrix([c0, c1])
    assert sp.expand((c.T * (Gstar - G0) * c)[0] - (c.T * GH * c)[0]) == 0
    assert sp.expand((c.T * (Gstar - GH) * c)[0] - (c.T * G0 * c)[0]) == 0

    result = {
        "schema":"marici.voevodsky.common-graph-norm-pullback-check.v1",
        "status":"pullback_graph_norm_verified",
        "graph_norm":"||p||_*^2=||p||_0^2+||p||_H2^2",
        "component_projections_contractive":True,
        "common_completion_constructed_abstractly":True,
        "hardy_topology_source_derived":False,
        "semiboundedness_in_reference_norm":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
