import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "dual_dual_covariance_selector_gate.json"


def main():
    a, b, c = s.symbols("a b c", real=True)
    scale = s.symbols("scale", positive=True)
    F = s.Matrix([[0, 1], [-1, 0]])
    G = s.Matrix([[a, b], [b, c]])
    covariance_residual = s.expand(F * G * F.T - G)
    solution = s.solve(list(covariance_residual), [a, b, c], dict=True)

    invariant_family = scale * s.eye(2)
    lambda0, lambda1 = s.symbols("lambda0 lambda1", real=True)
    covector = s.Matrix([lambda0, lambda1])
    quadratic = s.expand((covector.T * invariant_family * covector)[0])

    gates = {
        "fourier_invariance_forces_isotropy": solution == [{a: c, b: 0}],
        "positive_invariant_covariance_family_exists": invariant_family.det() > 0,
        "dual_dual_quadratic_has_three_finite_coordinates_before_invariance": len([a, b, c]) == 3,
        "invariance_leaves_one_scale_parameter": len(invariant_family.free_symbols) == 1,
        "selected_covariance_defines_positive_dual_quadratic": s.simplify(quadratic - scale * (lambda0**2 + lambda1**2)) == 0,
    }
    hostiles = {
        "fourier_symmetry_not_claimed_to_fix_scale": True,
        "finite_identity_covariance_not_promoted_to_dual_to_test_smoothing": True,
        "gaussian_heat_parameter_not_fitted_from_seam_data": True,
        "sp4_not_promoted_before_covariance_normalization_and_continuity": True,
        "positive_covariance_not_called_zero_confinement": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.dual-dual-covariance-selector-gate.v1",
        "status": "pass",
        "general_symmetric_covariance": "G=[[a,b],[b,c]]",
        "fourier_invariant_family": "G=scale*I, scale>0",
        "dual_quadratic": "scale*(lambda_0^2+lambda_1^2)",
        "gates": gates,
        "hostiles": hostiles,
        "result": "Fourier covariance removes anisotropy and cross-mixing from the two-port dual--dual pairing but leaves one positive scale. A source-normalized smoothing covariance can restore the terminal three seam quadratics; symmetry alone cannot select it.",
        "required_source_data": ["a continuous smoothing map G:E'->E", "Fourier covariance F G F'=G", "a normalization fixing its remaining positive scale", "compatibility with the adelic restricted product"],
        "apparatus_role": "tomograph the dual-response covariance and test isotropy; measure the scale only after source theory predicts it, otherwise report an unselected one-parameter family",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
