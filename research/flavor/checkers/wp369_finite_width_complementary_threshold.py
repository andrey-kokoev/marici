"""WP369: exact finite-width dispersive/absorptive threshold audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    epsilon = sp.symbols("epsilon", real=True)
    L, omega = sp.symbols("L Omega", positive=True)
    mu, k = sp.symbols("mu k", real=True, nonzero=True)

    controlled_L = L + k * epsilon
    complex_shift = -mu**2 / (2 * (controlled_L - sp.I * omega))
    dispersive = sp.simplify(sp.re(complex_shift))
    absorptive = sp.simplify(sp.im(complex_shift))
    response_R = sp.factor(sp.diff(dispersive, epsilon).subs(epsilon, 0))
    response_I = sp.factor(sp.diff(absorptive, epsilon).subs(epsilon, 0))

    threshold_map = sp.Matrix([
        dispersive.subs(epsilon, 0), absorptive.subs(epsilon, 0)
    ])
    threshold_jacobian = threshold_map.jacobian([L, omega])
    threshold_determinant = sp.factor(threshold_jacobian.det())
    response_vector = sp.Matrix([response_R, response_I])

    checks = {
        "dispersive_part_has_declared_form": sp.simplify(
            dispersive + mu**2 * controlled_L / (2 * (controlled_L**2 + omega**2))
        ) == 0,
        "absorptive_part_has_declared_form": sp.simplify(
            absorptive + mu**2 * omega / (2 * (controlled_L**2 + omega**2))
        ) == 0,
        "dispersive_response_has_declared_form": response_R == mu**2 * k * (L - omega) * (L + omega) / (2 * (L**2 + omega**2)**2),
        "absorptive_response_has_declared_form": response_I == mu**2 * k * L * omega / (L**2 + omega**2)**2,
        "dispersive_blind_point_at_equal_mass_width": response_R.subs(L, omega) == 0,
        "absorptive_channel_repairs_blind_point": sp.simplify(
            response_I.subs(L, omega) - mu**2 * k / (4 * omega**2)
        ) == 0,
        "joint_threshold_map_is_locally_faithful": threshold_determinant != 0,
        "narrow_width_recovers_real_matching": sp.simplify(
            dispersive.subs(omega, 0) + mu**2 / (2 * controlled_L)
        ) == 0,
        "narrow_width_kills_absorptive_channel": sp.limit(absorptive, omega, 0, dir="+") == 0,
        "heavy_mass_decouples_both_channels": all(
            sp.limit(component, L, sp.oo) == 0 for component in threshold_map
        ),
        "heavy_mass_decouples_both_responses": all(
            sp.limit(component, L, sp.oo) == 0 for component in response_vector
        ),
        "coupling_deletion_kills_both_channels": threshold_map.subs(mu, 0) == sp.zeros(2, 1),
        "deliberate_dispersive_only_probe_is_blind": (
            response_R.subs(L, omega) == 0 and response_I.subs(L, omega) != 0
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP369",
        "admitted_state_domain": "finite-width complex pole with positive mass-squared L, positive width scale Omega, nonzero mediator coupling mu, and nonzero local mass-control slope k",
        "faithful_quotient_coordinate": "the calibrated complex threshold pair (Delta U_R,Delta U_I) for mediator identification; full physical16 remains downstream and projected to J^2",
        "source_authorized_probe_family": "dispersive quartic shift and absorptive width/line-shape response derived from the same complex pole",
        "contextual_partition": "the dispersive projection alone has a response blind stratum L=Omega; the joint complex threshold map locally separates (L,Omega) when mu is known",
        "classification": "complementary source-derived threshold identifier and blind-point repair; not a new control direction or numerical flavor selector",
        "complex_shift": str(complex_shift),
        "dispersive": str(dispersive),
        "absorptive": str(absorptive),
        "responses": {"dispersive": str(response_R), "absorptive": str(response_I)},
        "threshold_jacobian_determinant": str(threshold_determinant),
        "smallest_exact_falsifier": "at L=Omega the dispersive mass-control response is zero while the absorptive response is mu^2*k/(4*Omega^2)",
        "remaining_physical_instrument_gate": "derive and calibrate the mediator width and line-shape channel, include mixing, backgrounds, loop matching, and detector resolution, and verify common control support",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp369_finite_width_complementary_threshold.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
