"""Exact minimal finite-cut value--flux reflection gate."""
import json
import sympy as sp


def main():
    # Boundary packet b=(v_left,q_left,v_right,q_right), with q the
    # coordinate derivative trace. Reflection x -> -x acts by (v,q)->(v,-q).
    graph = sp.Matrix([[1, 0, -1, 0], [0, 1, 0, 1]])
    value = graph[:1, :]
    flux = graph[1:, :]
    flux_witness = sp.Matrix([0, 1, 0, 0])

    # The one-jet Green form omega((v,q),(V,Q))=v Q-q V.
    J = sp.Matrix([[0, 1], [-1, 0]])
    R = sp.diag(1, -1)
    anti_symplectic = sp.simplify(R.T * J * R + J)

    checks = {
        "reflection_reverses_green_form": anti_symplectic == sp.zeros(2),
        "value_flux_graph_has_rank_two": graph.rank() == 2,
        "value_channel_has_rank_one": value.rank() == 1,
        "flux_is_independent_of_value": sp.Matrix.vstack(value, flux).rank() == 2,
        "scalar_zero_witness_survives": value * flux_witness == sp.zeros(1, 1),
        "same_witness_violates_flux": flux * flux_witness != sp.zeros(1, 1),
    }
    result = {
        "schema": "marici.grothendieck.continuum-value-flux-reflection-gate.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "reflection_matrix": [[str(x) for x in R.row(i)] for i in range(2)],
        "graph_constraint": [[str(x) for x in graph.row(i)] for i in range(2)],
        "graph_rank": graph.rank(),
        "value_rank": value.rank(),
        "flux_witness": [str(x) for x in flux_witness],
        "scope": "Boundary one-jets on a finite reflected interval; no theta or Xi action law.",
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
