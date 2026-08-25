import json
from pathlib import Path
import sympy as sp


def main():
    tau_x = sp.Matrix([[2, 3]])
    tau_y = sp.Matrix([[2, 3, 5]])
    v_xy = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    assert tau_y * v_xy == tau_x

    u_xy, u_yz = sp.Integer(7), sp.Integer(13)
    lam_x = sp.Integer(11)
    lam_y = u_xy * lam_x
    lam_z = u_yz * lam_y
    u_xz = u_yz * u_xy
    assert lam_y * tau_y * v_xy - u_xy * lam_x * tau_x == sp.zeros(1, 2)
    assert lam_z == u_xz * lam_x

    # A fixed scalar frame fails when the line transition is nontrivial.
    fixed_frame_residual = lam_x * tau_x - u_xy * lam_x * tau_x
    assert fixed_frame_residual != sp.zeros(1, 2)

    # Unnatural label mixing changes the common source row.
    v_bad = sp.Matrix([[1, 0], [0, 1], [1, 0]])
    naturality_residual = tau_y * v_bad - tau_x
    assert naturality_residual != sp.zeros(1, 2)

    result = {
        "owner": "marici.Kitaev",
        "classification": "incidence_torsor_requiring_one_source_reference",
        "assumptions": ["tau_Y V_XY = tau_X", "tau_X nonzero",
                        "U_XY invertible"],
        "coherent_fixture": {
            "tau_X": [2, 3], "tau_Y": [2, 3, 5],
            "U_XY": 7, "lambda_X": 11, "lambda_Y": int(lam_y),
            "two_cutoff_residual": [0, 0],
            "three_cutoff_path_residual": str(lam_z - u_xz * lam_x),
        },
        "hostiles": {
            "fixed_scalar_frame_residual": [str(x) for x in fixed_frame_residual],
            "unnatural_bonding_residual": [str(x) for x in naturality_residual],
            "zero_initial_incidence_stays_zero": True,
            "detector_can_annihilate_nonzero_line_state": True,
        },
        "finite_arithmetic_aggregation_adds_kernel": False,
        "remaining_source_reference": "undefined",
        "completion_stable_tau_lower_bound": "unproved",
        "detector_transversality": "unproved",
    }
    out = Path(__file__).parents[1] / "results" / "theta-common-trace-incidence-torsor.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
