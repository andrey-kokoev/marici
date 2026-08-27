import json
import sympy as sp


def main():
    fourier_even = sp.Matrix(
        [[sp.sqrt(3) / 3, sp.sqrt(6) / 3], [sp.sqrt(6) / 3, -sp.sqrt(3) / 3]]
    )
    graph_constraint = sp.Matrix.hstack(-fourier_even, sp.eye(2))
    scalar_readout = graph_constraint[:1, :]
    witness = sp.Matrix([0, 0, 0, 1])
    defect = sp.simplify(graph_constraint * witness)
    checks = {
        "fourier_graph_has_codimension_two": graph_constraint.rank() == 2,
        "scalar_zero_has_codimension_one": scalar_readout.rank() == 1,
        "one_boundary_channel_is_missing": graph_constraint.rank() - scalar_readout.rank() == 1,
        "witness_has_zero_scalar_readout": scalar_readout * witness == sp.zeros(1, 1),
        "witness_is_not_in_fourier_graph": defect != sp.zeros(2, 1),
    }
    result = {
        "schema": "marici.grothendieck.scalar-zero-fourier-graph-rank-gap.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "graph_rank": graph_constraint.rank(),
        "scalar_rank": scalar_readout.rank(),
        "witness_graph_defect": [str(x) for x in defect],
        "interpretation": (
            "In the smallest reflection-even Fourier boundary space, a linearly compressed scalar zero enforces "
            "one of two graph equations. One independent linear channel is still required; a determinant is not covered."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
