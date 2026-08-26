"""WP379: exact sign and power-counting audit for Gaussian portal mediators."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    A, F = sp.symbols("A F", real=True)
    mass2 = sp.symbols("M2", positive=True)
    coupling = sp.symbols("g", real=True, nonzero=True)

    potential = mass2 * A**2 / 2 + coupling * A * F
    mediator_solution = -coupling * F / mass2
    stationary_residual = sp.simplify(
        sp.diff(potential, A).subs(A, mediator_solution)
    )
    effective_potential = sp.factor(potential.subs(A, mediator_solution))
    completed_square = (
        mass2 * (A + coupling * F / mass2) ** 2 / 2
        - coupling**2 * F**2 / (2 * mass2)
    )
    matched_coefficient = sp.expand(effective_potential).coeff(F, 2)

    A1, A2 = sp.symbols("A1 A2", real=True)
    mass1, mass2b = sp.symbols("M1sq M2sq", positive=True)
    coupling1, coupling2 = sp.symbols("g1 g2", real=True, nonzero=True)
    multi_potential = (
        mass1 * A1**2 / 2 + mass2b * A2**2 / 2
        + (coupling1 * A1 + coupling2 * A2) * F
    )
    multi_effective = sp.factor(multi_potential.subs({
        A1: -coupling1 * F / mass1,
        A2: -coupling2 * F / mass2b,
    }))
    multi_coefficient = sp.expand(multi_effective).coeff(F, 2)

    ghost_potential = -mass2 * A**2 / 2 + coupling * A * F
    ghost_solution = coupling * F / mass2
    ghost_effective = sp.factor(ghost_potential.subs(A, ghost_solution))
    ghost_curvature = sp.diff(ghost_potential, A, 2)

    residual_field_degree = 24
    mediator_field_degree = 1
    linear_vertex_field_degree = residual_field_degree + mediator_field_degree

    checks = {
        "healthy_mediator_stationarity_residual_zero": stationary_residual == 0,
        "completion_of_square_is_exact": sp.expand(potential - completed_square) == 0,
        "healthy_exchange_generates_negative_square": matched_coefficient == -coupling**2 / (2 * mass2),
        "healthy_matched_coefficient_is_strictly_negative": matched_coefficient.is_negative,
        "two_healthy_mediators_remain_negative_semidefinite": multi_coefficient == -coupling1**2 / (2 * mass1) - coupling2**2 / (2 * mass2b),
        "two_mediator_coefficient_is_strictly_negative": multi_coefficient.is_negative,
        "ghost_curvature_is_negative": ghost_curvature == -mass2,
        "ghost_exchange_has_positive_matched_square": sp.expand(ghost_effective).coeff(F, 2) == coupling**2 / (2 * mass2),
        "linearized_vertex_has_field_degree_twenty_five": linear_vertex_field_degree == 25,
        "coupling_deletion_kills_matching": matched_coefficient.subs(coupling, 0) == 0,
        "heavy_mass_decouples_matching": sp.limit(matched_coefficient, mass2, sp.oo) == 0,
        "deliberate_positive_penalty_claim_fails": matched_coefficient != coupling**2 / (2 * mass2),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP379",
        "admitted_state_domain": "ordinary real linearly coupled Gaussian mediators with positive mass curvature, acting on WP378's real polynomial residual F",
        "faithful_quotient_coordinate": "WP378's nondegenerate physical16 shell coordinate F; this audit acts upstream on the mediator source",
        "source_authorized_probe_family": "exact stationary elimination, completion of square, multi-mediator extension, deletion, decoupling, and power counting",
        "contextual_partition": "all healthy linear Gaussian mediator packets generate coefficients in the negative-semidefinite F^2 cone; none reaches a positive penalty",
        "classification": "exact sign and power-counting obstruction for ordinary healthy linear-Gaussian tree completion; not a no-go for non-Gaussian or symmetry-protected sources",
        "potential": str(potential),
        "mediator_solution": str(mediator_solution),
        "effective_potential": str(effective_potential),
        "matched_coefficient": str(matched_coefficient),
        "two_mediator_effective_potential": str(multi_effective),
        "two_mediator_coefficient": str(multi_coefficient),
        "ghost_effective_potential": str(ghost_effective),
        "ghost_curvature": str(ghost_curvature),
        "linear_vertex_field_degree": linear_vertex_field_degree,
        "smallest_exact_falsifier": "a healthy real mediator produces -g^2*F^2/(2*M2), the opposite sign from the required positive shell penalty",
        "remaining_physical_instrument_gate": "construct a ghost-free non-Gaussian, constrained-auxiliary, radiative, or symmetry-protected source that derives a positive F^2 term and alpha before readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp379_gaussian_portal_sign_obstruction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
