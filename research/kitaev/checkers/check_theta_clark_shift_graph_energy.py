import json
from pathlib import Path
import sympy as sp
from itertools import combinations


def principal_minors_nonnegative(matrix):
    indices = range(matrix.rows)
    minors = []
    for size in range(1, matrix.rows + 1):
        for subset in combinations(indices, size):
            minor = sp.factor(matrix.extract(subset, subset).det())
            minors.append(minor)
            assert minor.is_nonnegative is True
    return minors


def main():
    # Exact finite graph model: mass plus a first difference derivative.
    D = sp.Matrix([[-1, 1, 0], [0, -1, 1]])
    I = sp.eye(3)
    endpoint = sp.diag(1, 0, 0)
    Q_graph = I + D.T * D

    a = sp.Rational(1, 2)
    Q_clark = a**2 * I + D.T * D + a * endpoint
    lower_residual = sp.simplify(Q_clark - a**2 * Q_graph)
    upper_residual = sp.simplify(sp.Rational(3, 2) * Q_graph - Q_clark)
    lower_minors = principal_minors_nonnegative(lower_residual)
    upper_minors = principal_minors_nonnegative(upper_residual)

    # L2-only control cannot dominate graph frequency n uniformly.
    n = sp.symbols("n", positive=True, integer=True)
    graph_frequency_ratio = 1 + n**2
    assert sp.limit(graph_frequency_ratio, n, sp.oo) == sp.oo

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "source_derived_clark_shift_graph_form_equivalence",
        "a": "1/2",
        "graph_matrix": [[str(v) for v in row] for row in Q_graph.tolist()],
        "clark_matrix": [[str(v) for v in row] for row in Q_clark.tolist()],
        "lower_constant": "1/4",
        "upper_constant": "3/2",
        "lower_residual_rank": lower_residual.rank(),
        "upper_residual_rank": upper_residual.rank(),
        "lower_principal_minors": [str(v) for v in lower_minors],
        "upper_principal_minors": [str(v) for v in upper_minors],
        "l2_only_graph_ratio": str(graph_frequency_ratio),
        "l2_only_uniform_graph_control": False,
        "finite_horizon_uniform_observability": False,
        "global_poisson_green_comparison": "unproved",
        "detector_transversality": "unproved",
    }
    out = Path(__file__).parents[1] / "results" / "theta-clark-shift-graph-energy.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
