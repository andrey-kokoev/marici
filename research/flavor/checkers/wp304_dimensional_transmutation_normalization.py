"""WP304: exact RG-invariant scale and boundary-authority audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    beta_coefficient, boundary_coupling, reference_scale, scale = sp.symbols(
        "beta_coefficient boundary_coupling reference_scale scale", positive=True
    )
    running_coupling = 1 / (1 / boundary_coupling + beta_coefficient * sp.log(scale / reference_scale))
    transmutation_scale = sp.simplify(scale * sp.exp(-1 / (beta_coefficient * running_coupling)))
    boundary_form = reference_scale * sp.exp(-1 / (beta_coefficient * boundary_coupling))
    logarithmic_derivative = sp.simplify(scale * sp.diff(transmutation_scale, scale))

    packet_one = boundary_form.subs({beta_coefficient: 1, reference_scale: 1, boundary_coupling: 1})
    packet_two = boundary_form.subs({beta_coefficient: 1, reference_scale: 1, boundary_coupling: sp.Rational(1, 2)})
    recovered_coupling = sp.solve(sp.Eq(sp.symbols("radius", positive=True), boundary_form), boundary_coupling)[0]

    checks = {
        "running_solution_obeys_boundary_condition": sp.simplify(running_coupling.subs(scale, reference_scale) - boundary_coupling) == 0,
        "transmutation_scale_equals_boundary_form": sp.simplify(transmutation_scale - boundary_form) == 0,
        "transmutation_scale_is_rg_invariant": logarithmic_derivative == 0,
        "same_beta_law_different_boundary_couplings_give_different_scales": packet_one != packet_two,
        "first_exact_scale_is_exp_minus_one": packet_one == sp.exp(-1),
        "second_exact_scale_is_exp_minus_two": packet_two == sp.exp(-2),
        "target_radius_inverts_to_boundary_coupling": sp.simplify(recovered_coupling + 1 / (beta_coefficient * sp.log(sp.symbols("radius", positive=True) / reference_scale))) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP304",
        "theorem_domain": "one asymptotically free coupling with beta(g)=-b*g^2, b>0, positive boundary coupling g0 at reference scale mu0",
        "running_coupling": "1/g(mu)=1/g0+b*log(mu/mu0)",
        "rg_invariant_scale": "Lambda=mu*exp(-1/(b*g(mu)))=mu0*exp(-1/(b*g0))",
        "rival_boundary_packets": [
            {"b": "1", "mu0": "1", "g0": "1", "Lambda": str(packet_one)},
            {"b": "1", "mu0": "1", "g0": "1/2", "Lambda": str(packet_two)},
        ],
        "authority_inversion": "g0=-1/(b*log(Lambda/mu0))",
        "descent": "Lambda is invariant along the declared RG trajectory once the reference normalization and boundary coupling are fixed",
        "classification": "dimensional transmutation supplies an RG-invariant normalization relation but does not numerically select the scale without boundary-coupling authority",
        "smallest_exact_falsifier": "the same beta function and reference scale give Lambda=exp(-1) at g0=1 and Lambda=exp(-2) at g0=1/2",
        "remaining_physical_instrument_gate": "derive or measure the boundary coupling and reference normalization independently of the target flavor radius, then match Lambda covariantly into physical16 with thresholds and uncertainties",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp304_dimensional_transmutation_normalization.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
