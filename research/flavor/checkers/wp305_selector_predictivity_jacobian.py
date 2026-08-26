"""WP305: exact source-parameter response ranks for candidate selectors."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def jacobian_rank(outputs, parameters):
    return sp.Matrix(outputs).jacobian(parameters).rank()


def main():
    b1, b2 = sp.symbols("b1 b2", real=True)
    full_point = sp.Matrix([b1 / 2, b2 / 3])
    full_rank = jacobian_rank(full_point, (b1, b2))

    beta, curvature, mixing = sp.symbols("beta curvature mixing", positive=True)
    symmetric_point = sp.Matrix([beta / (curvature + mixing)] * 2)
    symmetric_physical_rank = jacobian_rank(symmetric_point, (beta,))
    projective_ratio = sp.simplify(symmetric_point[0] / symmetric_point[1])
    projective_rank = jacobian_rank([projective_ratio], (beta,))

    radius = sp.symbols("radius", positive=True)
    normalized_lift = sp.Matrix([radius / sp.sqrt(2)] * 2)
    normalization_rank = jacobian_rank(normalized_lift, (radius,))

    boundary_coupling, beta_coefficient, reference_scale = sp.symbols(
        "boundary_coupling beta_coefficient reference_scale", positive=True
    )
    transmutation_scale = reference_scale * sp.exp(-1 / (beta_coefficient * boundary_coupling))
    transmutation_response = sp.simplify(sp.diff(transmutation_scale, boundary_coupling))
    transmutation_rank = jacobian_rank([transmutation_scale], (boundary_coupling,))

    checks = {
        "unconstrained_quadratic_source_has_rank_two_ambiguity": full_rank == 2,
        "swap_symmetric_source_has_rank_one_physical_ambiguity": symmetric_physical_rank == 1,
        "projective_ratio_kills_amplitude_response": projective_rank == 0 and projective_ratio == 1,
        "normalization_lift_restores_rank_one_response": normalization_rank == 1,
        "dimensional_transmutation_retains_boundary_response": transmutation_rank == 1 and transmutation_response != 0,
        "transmutation_response_formula_is_exact": transmutation_response == transmutation_scale / (beta_coefficient * boundary_coupling**2),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP305",
        "criterion": "after quotienting genuine source redundancies, rank(d x_star/d theta)=0 is necessary for a parameter-independent point prediction on the admitted source family",
        "rank_audits": {
            "wp301_unconstrained_linear_source": {"free_parameters": ["b1", "b2"], "physical_response_rank": full_rank},
            "wp302_swap_symmetric_source": {"free_parameters": ["beta"], "physical_response_rank": symmetric_physical_rank},
            "wp303_projective_ratio": {"free_parameters": ["beta"], "projective_response_rank": projective_rank},
            "wp303_normalization_lift": {"free_parameters": ["radius"], "physical_response_rank": normalization_rank},
            "wp304_dimensional_transmutation": {
                "free_parameters": ["g0"],
                "scale_response_rank": transmutation_rank,
                "response": str(transmutation_response),
            },
        },
        "classification": "source-modulus response rank measures local predictive ambiguity; quotienting can remove redundant directions, but every physical normalization modulus must also have zero response or independent selection",
        "smallest_exact_falsifier": "swap symmetry reduces the physical ambiguity rank from two to one, but only the projective quotient makes it zero; lifting by a free radius returns rank one",
        "scope_limit": "zero response rank is necessary, not sufficient: disconnected branches, global monodromy, coefficient provenance, dynamics, descent, and instruments remain separate gates",
        "remaining_physical_instrument_gate": "enumerate the actual source moduli, quotient only admitted redundancies, compute the full source-to-physical16 response rank with uncertainty, and derive operations selecting every surviving responsive modulus",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp305_selector_predictivity_jacobian.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
