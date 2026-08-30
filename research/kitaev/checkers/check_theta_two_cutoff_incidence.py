import json
from pathlib import Path
import sympy as sp


def residual(a_x, b_x, a_y, b_y):
    return sp.expand(a_y * b_x - b_y * a_x)


def main():
    u = sp.Symbol("u", nonzero=True)

    # Coherent projective slope.
    coherent = residual(sp.Integer(2), sp.Integer(6), sp.Integer(5), sp.Integer(15))
    assert coherent == 0

    # Smallest mismatch and the residual left after fitting the tail cell.
    mismatch = residual(sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(2))
    fitted_v = u
    tail_residual = sp.expand(sp.Integer(1) * fitted_v - u * sp.Integer(1))
    seam_residual = sp.expand(sp.Integer(2) * fitted_v - u * sp.Integer(1))
    assert mismatch == -1 and tail_residual == 0 and seam_residual == u

    # Higher-rank graph inclusion but not equality: V embeds Q into Q^2.
    V = sp.Matrix([[1], [0]])
    joint_x = sp.eye(1)
    joint_y = sp.eye(2)
    induced = joint_y * V
    assert induced.rank() == 1 and joint_y.rank() == 2

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "finite_algebraic_theorem_and_source_typing_boundary",
        "coherent_fixture": {"rows_X": [2, 6], "rows_Y": [5, 15],
                             "projective_residual": str(coherent)},
        "slope_mismatch": {"rows_X": [1, 1], "rows_Y": [1, 2],
                           "projective_residual": str(mismatch),
                           "tail_fitted_residual": str(tail_residual),
                           "seam_remaining_residual": str(seam_residual)},
        "operator_kernel_hostile": {"a_X": 0, "b_X": 1,
                                    "kernel_inclusion": False},
        "graph_inclusion_not_equality": {"induced_rank": induced.rank(),
                                         "target_graph_rank": joint_y.rank(),
                                         "surjective": False},
        "incidence_value_type": "projective_anomaly_line",
        "actual_theta_maps": {
            "V_XY": "undefined",
            "tail_to_line_incidence": "undefined",
            "seam_to_line_incidence": "undefined",
            "projective_residual": "undefined",
        },
    }
    out = Path(__file__).parents[1] / "results" / "theta-two-cutoff-incidence.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
