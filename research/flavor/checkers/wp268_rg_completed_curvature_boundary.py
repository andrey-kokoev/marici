"""WP268: exact RG completion of the one-loop selector curvature."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    amplitude, slope = sp.symbols("amplitude slope", positive=True)
    log_scale, log_mass_reference = sp.symbols("log_scale log_mass_reference", real=True)
    boundary = sp.symbols("boundary", real=True)

    # c=3/2 packet from WP267. log_scale=log(mu/mu0) and
    # log_mass_reference=log(M^2/mu0^2).
    loop_curvature = 2 * amplitude * slope**2 * (log_mass_reference - 2 * log_scale)
    running_counterterm = boundary + 2 * amplitude * slope**2 * log_scale
    total_curvature = sp.simplify(loop_curvature + 2 * running_counterterm)
    rg_derivative = sp.diff(total_curvature, log_scale)

    # Exact boundary-hostile packets at M=mu0 and with linear coefficient a=1.
    a = sp.Rational(1)
    packet_one_curvature = total_curvature.subs({amplitude: 1, slope: 1, log_mass_reference: 0, boundary: 1})
    packet_two_curvature = total_curvature.subs({amplitude: 1, slope: 1, log_mass_reference: 0, boundary: 2})
    selected_one = sp.simplify(a / packet_one_curvature)
    selected_two = sp.simplify(a / packet_two_curvature)

    checks = {
        "counterterm_beta_cancels_loop_scale_dependence": rg_derivative == 0,
        "total_curvature_is_rg_invariant": total_curvature == 2 * amplitude * slope**2 * log_mass_reference + 2 * boundary,
        "boundary_constant_survives_completion": sp.diff(total_curvature, boundary) == 2,
        "first_boundary_packet_positive": packet_one_curvature == 2,
        "second_boundary_packet_positive": packet_two_curvature == 4,
        "hostile_boundaries_select_distinct_points": selected_one == sp.Rational(1, 2) and selected_two == sp.Rational(1, 4),
        "same_rg_transport_does_not_fix_boundary": selected_one != selected_two,
        "deliberate_rg_uniqueness_claim_fails": selected_one - selected_two == sp.Rational(1, 4),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP268",
        "theorem_domain": "WP267 one-loop curvature plus a running local x^2 counterterm in the c=3/2 subtraction packet",
        "scale_coordinates": {
            "ell": "log(mu/mu0)",
            "L0": "log(M^2/mu0^2)",
        },
        "loop_curvature": str(loop_curvature),
        "running_counterterm_coefficient": str(running_counterterm),
        "counterterm_beta": str(sp.diff(running_counterterm, log_scale)),
        "rg_invariant_total_curvature": str(total_curvature),
        "hostile_boundary_packets": [
            {"boundary_c2_mu0": "1", "total_curvature": str(packet_one_curvature), "selected_x": str(selected_one)},
            {"boundary_c2_mu0": "2", "total_curvature": str(packet_two_curvature), "selected_x": str(selected_two)},
        ],
        "classification": "RG completion restores matching-scale invariance but leaves one boundary integration constant that controls the numerical interior selector",
        "first_nonfaithful_arrow": "RG beta function and scheme transport -> renormalized boundary value c2(mu0)",
        "smallest_exact_falsifier": "with identical loop content and RG law, c2(mu0)=1 and 2 select x=1/2 and 1/4",
        "remaining_authority_gate": "derive the renormalized boundary coefficient from a UV fixed point, symmetry-breaking threshold, finite matching condition, or other source law independently of flavor readout",
        "scope_limit": "does not exclude a UV completion that fixes the boundary value; it proves that RG consistency and the one-loop beta function alone do not",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp268_rg_completed_curvature_boundary.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
