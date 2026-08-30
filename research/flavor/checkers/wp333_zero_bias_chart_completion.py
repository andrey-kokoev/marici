"""WP333: exact nonlogarithmic chart completion at zero CP bias."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    beta, c0, gap, gain = sp.symbols("beta c0 gap gain", real=True, positive=True)
    epsilon = sp.symbols("epsilon", real=True)
    thermal_coordinate = beta * gap
    cp_amplitude = gain * c0
    log_odds = 2 * beta * epsilon * c0
    parameters = (beta, epsilon, c0)
    response = sp.Matrix([
        [sp.diff(readout, parameter) for parameter in parameters]
        for readout in (thermal_coordinate, cp_amplitude, log_odds)
    ])
    boundary_response = sp.simplify(response.subs(epsilon, 0))
    boundary_gram = sp.simplify(boundary_response.T * boundary_response)
    determinant = sp.factor(boundary_response.det())
    squared_singular_values = {gap**2, gain**2, 4 * beta**2 * c0**2}
    inverse_bias = sp.simplify(log_odds * gap * gain / (2 * thermal_coordinate * cp_amplitude))
    checks = {
        "boundary_response_has_full_rank": boundary_response.rank() == 3,
        "boundary_determinant_is_nonzero_on_domain": determinant == -2 * beta * c0 * gain * gap,
        "boundary_gram_is_diagonal": boundary_gram == sp.diag(gap**2, 4 * beta**2 * c0**2, gain**2),
        "boundary_squared_singular_values_are_exact": set(boundary_gram.diagonal()) == squared_singular_values,
        "signed_bias_is_reconstructed_across_zero": inverse_bias == epsilon,
        "zero_log_odds_implies_zero_bias_on_positive_support": sp.solve(sp.Eq(log_odds, 0), epsilon) == [0],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP333",
        "admitted_state_domain": "positive beta,c0,gap,gain and signed epsilon, including epsilon=0",
        "faithful_quotient_coordinate": "the source triple (beta,epsilon,c0) in the nonlogarithmic common-frame chart",
        "readout_coordinates": ["x=-log A=beta*gap", "C=gain*c0", "L=2*beta*epsilon*c0"],
        "zero_bias_response_jacobian": [[str(value) for value in row] for row in boundary_response.tolist()],
        "zero_bias_determinant": str(determinant),
        "zero_bias_gram_matrix": [[str(value) for value in row] for row in boundary_gram.tolist()],
        "squared_singular_values": ["gap^2", "gain^2", "4*beta^2*c0^2"],
        "signed_bias_inverse": "epsilon=L*gap*gain/(2*x*C)",
        "robustness_rule": "at zero bias, full rank survives additive Jacobian error smaller than min(gap,gain,2*beta*c0) in consistently calibrated units",
        "contextual_partition": "the nonlog chart separates negative, zero, and positive bias; only the positive log chart of WP332 excludes the zero stratum",
        "classification": "a faithful chart completion for source identification across CP symmetry restoration; it adds no selector and remains conditional on calibrated units",
        "smallest_exact_falsifier": "if gap, gain, beta, or c0 vanishes, one boundary singular value vanishes and the corresponding source direction is unreadable",
        "remaining_physical_instrument_gate": "calibrate a common detector metric before comparing dimensionful singular values, bound additive errors below the minimum margin, and resolve finite-sample log-odds near zero",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp333_zero_bias_chart_completion.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
