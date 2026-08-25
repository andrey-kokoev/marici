import json
from pathlib import Path
import sympy as sp


def observability(eigenvalues, row):
    n = len(eigenvalues)
    return sp.Matrix([[row[j] * eigenvalues[j] ** k for j in range(n)]
                      for k in range(n)])


def main():
    eigenvalues = [sp.Integer(0), sp.Integer(1), sp.Integer(3)]
    row = [sp.Integer(2), sp.Integer(5), sp.Integer(7)]
    O = observability(eigenvalues, row)
    determinant = sp.factor(O.det())
    assert determinant != 0 and O.rank() == 3

    repeated = observability([sp.Integer(0), sp.Integer(1), sp.Integer(1)],
                             [sp.Integer(1), sp.Integer(1), sp.Integer(1)])
    repeated_witness = sp.Matrix([0, 1, -1])
    assert repeated * repeated_witness == sp.zeros(3, 1)

    delta = sp.symbols("delta", positive=True)
    clustered = observability([sp.Integer(0), delta, 2 * delta],
                              [sp.Integer(1), sp.Integer(1), sp.Integer(1)])
    clustered_det = sp.factor(clustered.det())
    assert clustered_det == 2 * delta**3
    assert sp.limit(clustered_det, delta, 0, dir="+") == 0

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "finite_observability_theorem_and_clustered_spectrum_obstruction",
        "observable_fixture": {
            "eigenvalues": [0, 1, 3], "output_row": [2, 5, 7],
            "observability_matrix": [[str(v) for v in r] for r in O.tolist()],
            "determinant": str(determinant), "rank": O.rank(),
        },
        "repeated_mode_hostile": {
            "rank": repeated.rank(),
            "hidden_state": [int(v) for v in repeated_witness],
            "hidden_output_orbit": [int(v) for v in repeated * repeated_witness],
        },
        "clustered_modes": {
            "eigenvalues": ["0", "delta", "2*delta"],
            "determinant": str(clustered_det),
            "zero_spacing_limit": "0",
            "finite_rank_full_for_delta_positive": True,
            "uniform_observability": False,
        },
        "actual_theta_coefficient_generator": "undefined",
        "physical_time_jet_instrument": "not_established",
    }
    out = Path(__file__).parents[1] / "results" / "theta-dynamical-observability.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
