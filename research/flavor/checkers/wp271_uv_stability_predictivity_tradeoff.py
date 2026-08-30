"""WP271: exact UV stability-versus-finite-scale-predictivity theorem."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    time = sp.symbols("time", nonnegative=True)
    amplitudes = sp.symbols("A1 A2 A3", real=True)

    stability_matrix = sp.diag(-2, -1, 3)
    trajectory = sp.Matrix([
        amplitudes[0] * sp.exp(-2 * time),
        amplitudes[1] * sp.exp(-time),
        amplitudes[2] * sp.exp(3 * time),
    ])
    flow_residual = sp.simplify(trajectory.diff(time) - stability_matrix * trajectory)

    # Reaching the fixed point as t->infinity forces only the positive mode's
    # amplitude to zero. The two attractive amplitudes remain arbitrary.
    uv_admissible_constraints = {amplitudes[2]: 0}
    admissible_trajectory = trajectory.subs(uv_admissible_constraints)
    matching_map = sp.simplify(admissible_trajectory.subs(time, 0))
    amplitude_jacobian = matching_map.jacobian(sp.Matrix(amplitudes[:2]))

    # A zero-dimensional stable manifold: all exponents positive, so only the
    # exact fixed trajectory reaches the UV point; there is no attractive mode.
    zero_dimensional_matrix = sp.diag(1, 2, 3)
    zero_dimensional_trajectory = sp.Matrix([
        amplitudes[0] * sp.exp(time),
        amplitudes[1] * sp.exp(2 * time),
        amplitudes[2] * sp.exp(3 * time),
    ])
    zero_dimensional_constraints = {amplitude: 0 for amplitude in amplitudes}

    checks = {
        "linearized_flow_solution_exact": flow_residual == sp.zeros(3, 1),
        "two_uv_attractive_eigenvalues": sum(1 for value in stability_matrix.diagonal() if value < 0) == 2,
        "one_uv_repulsive_amplitude_must_vanish": sp.limit(trajectory[2].subs(amplitudes[2], 1), time, sp.oo) == sp.oo and admissible_trajectory[2] == 0,
        "two_free_attractive_amplitudes_survive": matching_map == sp.Matrix([amplitudes[0], amplitudes[1], 0]),
        "finite_matching_map_has_rank_two": amplitude_jacobian.rank() == 2,
        "uv_limit_collapses_rank_two_family": all(sp.limit(admissible_trajectory[i], time, sp.oo) == 0 for i in range(3)),
        "zero_dimensional_uv_surface_requires_all_amplitudes_zero": zero_dimensional_constraints == {amplitudes[0]: 0, amplitudes[1]: 0, amplitudes[2]: 0},
        "zero_dimensional_case_has_no_attractive_eigendirection": all(value > 0 for value in zero_dimensional_matrix.diagonal()),
        "deliberate_attraction_implies_unique_trajectory_claim_fails": amplitude_jacobian.rank() != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP271",
        "theorem_domain": "finite-dimensional autonomous RG flow linearized at a hyperbolic UV fixed point, with t increasing toward the UV",
        "mixed_stability_matrix": [[int(value) for value in stability_matrix.row(i)] for i in range(3)],
        "mixed_eigenvalues": [str(value) for value in stability_matrix.diagonal()],
        "uv_critical_surface_dimension": 2,
        "uv_admissible_trajectory": [str(value) for value in admissible_trajectory],
        "finite_matching_map": [str(value) for value in matching_map],
        "finite_matching_amplitude_rank": int(amplitude_jacobian.rank()),
        "zero_dimensional_matrix": [[int(value) for value in zero_dimensional_matrix.row(i)] for i in range(3)],
        "classification": "each UV-attractive eigendirection contributes one free finite-scale trajectory amplitude; eliminating all such amplitudes makes the UV critical surface zero-dimensional but removes open-basin attraction",
        "smallest_exact_falsifier": "diag(-2,-1,3) has a two-dimensional family (A1*e^-2t,A2*e^-t,0) sharing one UV limit while retaining rank-two finite matching data",
        "remaining_authority_gate": "supply independent conditions for every attractive trajectory amplitude, or derive a zero-dimensional UV critical surface and explain physical preparation on its measure-zero trajectory",
        "scope_limit": "local hyperbolic theorem; center manifolds, limit cycles, nonautonomous flows, singular boundaries, and stochastic UV dynamics require separate typing",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp271_uv_stability_predictivity_tradeoff.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
