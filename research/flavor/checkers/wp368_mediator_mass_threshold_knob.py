"""WP368: exact tree-level mediator constructor for the quartic threshold knob."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    epsilon, t, S = sp.symbols("epsilon t S", real=True)
    L = sp.symbols("L", positive=True)
    mu, k = sp.symbols("mu k", real=True, nonzero=True)
    U0 = sp.symbols("U0", real=True)
    alpha = sp.symbols("alpha", positive=True)

    controlled_mass2 = L + k * epsilon
    mediator_potential = controlled_mass2 * S**2 / 2 + mu * S * t**2 / 2
    mediator_solution = -mu * t**2 / (2 * controlled_mass2)
    stationarity_residual = sp.simplify(
        sp.diff(mediator_potential, S).subs(S, mediator_solution)
    )
    matched_shift = sp.factor(mediator_potential.subs(S, mediator_solution))
    effective_U = U0 - mu**2 / (2 * controlled_mass2)
    effective_U0 = effective_U.subs(epsilon, 0)
    intervention_strength = sp.simplify(sp.diff(effective_U, epsilon).subs(epsilon, 0))

    source_port = -1 / effective_U
    flavor_port = alpha * source_port
    q_response = sp.simplify(sp.diff(source_port, epsilon).subs(epsilon, 0))
    p_response = sp.simplify(sp.diff(flavor_port, epsilon).subs(epsilon, 0))
    response_ratio = sp.simplify(p_response / q_response)

    checks = {
        "mediator_stationarity_residual_zero": stationarity_residual == 0,
        "tree_matching_shift_is_negative_quartic": sp.simplify(
            matched_shift + mu**2 * t**4 / (8 * controlled_mass2)
        ) == 0,
        "effective_quartic_has_declared_form": effective_U == U0 - mu**2 / (2 * controlled_mass2),
        "mass_control_generates_quartic_intervention": intervention_strength == mu**2 * k / (2 * L**2),
        "source_response_matches_chain_rule": sp.simplify(
            q_response - intervention_strength / effective_U0**2
        ) == 0,
        "flavor_response_is_alpha_times_source": p_response == alpha * q_response,
        "common_response_ratio_recovers_alpha": response_ratio == alpha,
        "mediator_deletion_kills_intervention": intervention_strength.subs(mu, 0) == 0,
        "control_deletion_kills_intervention": intervention_strength.subs(k, 0) == 0,
        "heavy_mass_decouples_quartic_shift": sp.limit(effective_U, L, sp.oo) == U0,
        "heavy_mass_decouples_response": sp.limit(intervention_strength, L, sp.oo) == 0,
        "deliberate_wrong_sign_matching_is_detected": matched_shift != mu**2 * t**4 / (8 * controlled_mass2),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP368",
        "admitted_state_domain": "tree-level canonical scalar EFT with positive controlled mediator mass-squared L+k*epsilon near epsilon=0, nonzero superrenormalizable coupling mu, nonzero mass-control slope k, and the conditional invariant flavor portal",
        "faithful_quotient_coordinate": "canonical effective quartic Ueff upstream and full physical16 downstream; the instrument still factors through J^2",
        "source_authorized_probe_family": "mediator mass interventions, exact tree matching, deletion limits, decoupling limits, and equilibrium two-port responses",
        "contextual_partition": "packets with equal induced alpha and calibrated response ratio remain equivalent to this rank-one probe; mediator parameters are not fully identified",
        "classification": "conditional tree-level source constructor for the common threshold perturbation; candidate instrument grammar, not numerical selector or completed laboratory experiment",
        "mediator_potential": str(mediator_potential),
        "mediator_solution": str(mediator_solution),
        "matched_shift": str(matched_shift),
        "effective_U": str(effective_U),
        "intervention_strength": str(intervention_strength),
        "responses": {"p": str(p_response), "q": str(q_response), "p_over_q": str(response_ratio)},
        "smallest_exact_falsifier": "mu=0 deletes the threshold quartic shift and both common-port responses",
        "remaining_physical_instrument_gate": "derive an experimentally controllable background for the mediator pole mass and include finite width, mixing, loop matching, wave-function normalization, stability, and detector resolution",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp368_mediator_mass_threshold_knob.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
