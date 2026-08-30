"""WP264: exact tree-level matching audit for one stable Gaussian mediator."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    x, mediator = sp.symbols("x mediator", real=True)
    mass2, coupling, vev = sp.symbols("mass2 coupling vev", positive=True)
    direct_quartic = sp.symbols("direct_quartic", real=True)

    ultraviolet = mass2 * (mediator - vev) ** 2 / 2 - coupling * mediator * x
    mediator_solution = sp.solve(sp.diff(ultraviolet, mediator), mediator)[0]
    effective = sp.factor(ultraviolet.subs(mediator, mediator_solution))
    linear_coefficient = sp.expand(effective).coeff(x, 1)
    quadratic_coefficient = sp.expand(effective).coeff(x, 2)

    repaired_uv = ultraviolet + direct_quartic * x**2
    repaired_effective = sp.factor(repaired_uv.subs(mediator, mediator_solution))
    repaired_quadratic = sp.expand(repaired_effective).coeff(x, 2)

    # Exact stable witness.
    witness = {mass2: sp.Rational(4), coupling: sp.Rational(1), vev: sp.Rational(1)}
    witness_effective = sp.expand(effective.subs(witness))
    witness_curvature = sp.diff(witness_effective, x, 2)
    minimum_direct_quartic = sp.solve(sp.Eq(repaired_quadratic, 0), direct_quartic)[0]

    checks = {
        "stable_mediator_hessian_positive": sp.diff(ultraviolet, mediator, 2) == mass2,
        "mediator_solution_exact": mediator_solution == vev + coupling * x / mass2,
        "linear_selector_term_generated": linear_coefficient == -coupling * vev,
        "generated_quadratic_term_has_wrong_sign": quadratic_coefficient == -coupling**2 / (2 * mass2),
        "stable_nonzero_coupling_cannot_generate_positive_b": quadratic_coefficient.is_negative,
        "exact_witness_is_concave_in_x": witness_curvature == -sp.Rational(1, 4),
        "direct_repair_introduces_independent_coefficient": repaired_quadratic == direct_quartic - coupling**2 / (2 * mass2),
        "positive_effective_b_requires_strict_counterterm_bound": minimum_direct_quartic == coupling**2 / (2 * mass2),
        "deliberate_one_mediator_stabilization_claim_fails": witness_curvature < 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP264",
        "theorem_domain": "one real stable Gaussian mediator with positive mass squared and a linear coupling to the nonnegative commutator invariant x",
        "uv_potential": "M^2(S-v)^2/2 - g*S*x",
        "mediator_solution": str(mediator_solution),
        "tree_effective_potential": str(effective),
        "effective_coefficients": {
            "linear_x": str(linear_coefficient),
            "quadratic_x_squared": str(quadratic_coefficient),
        },
        "direct_repair": {
            "added_operator": "b0*x^2",
            "effective_quadratic_coefficient": str(repaired_quadratic),
            "strict_stability_requirement": "b0 > coupling^2/(2*mass2)",
        },
        "exact_witness": {
            "mass2": "4",
            "coupling": "1",
            "vev": "1",
            "effective_potential": str(witness_effective),
            "x_curvature": str(witness_curvature),
        },
        "classification": "single stable Gaussian-mediator matching generates the desired linear selector term but a destabilizing negative quadratic term; a positive stabilizer requires an independent source coefficient",
        "smallest_exact_falsifier": "M^2=4, g=1, and v=1 give V_eff=-x-x^2/8 with curvature -1/4",
        "remaining_authority_gate": "derive a positive direct x^2 term, nonlinear mediator sector, or radiative correction with its sign and normalization independently fixed before flavor readout",
        "scope_limit": "tree-level theorem for one stable Gaussian mediator linearly coupled to x; it does not exclude nonlinear, multi-mediator, fermion-loop, supersymmetric, or nonperturbative matching",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp264_gaussian_mediator_matching.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
