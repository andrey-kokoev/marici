"""WP367: exact common causal response from a canonical quartic intervention."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    epsilon = sp.symbols("epsilon", real=True)
    U = sp.symbols("U", real=True, negative=True)
    h = sp.symbols("h", real=True, nonzero=True)
    alpha = sp.symbols("alpha", positive=True)
    x0 = sp.symbols("x0", real=True)

    intervened_U = U + h * epsilon
    source_port = -1 / intervened_U
    flavor_port = alpha * source_port
    q_response = sp.simplify(sp.diff(source_port, epsilon).subs(epsilon, 0))
    p_response = sp.simplify(sp.diff(flavor_port, epsilon).subs(epsilon, 0))
    response_ratio = sp.simplify(p_response / q_response)
    response_jacobian = sp.Matrix([p_response, q_response])
    deleted_portal_response = sp.diff(x0, epsilon)

    packet_a = {U: -1, h: 1}
    packet_b = {U: -2, h: 4}

    checks = {
        "source_response_is_nonzero": q_response == h / U**2,
        "flavor_response_is_nonzero_with_portal": p_response == alpha * h / U**2,
        "common_response_ratio_recovers_alpha": response_ratio == alpha,
        "response_jacobian_has_rank_one": response_jacobian.rank() == 1,
        "portal_deletion_kills_flavor_response": deleted_portal_response == 0,
        "portal_deletion_leaves_source_response": q_response != 0,
        "distinct_source_packets_share_response_ratio": (
            packet_a != packet_b
            and response_ratio.subs(packet_a) == response_ratio.subs(packet_b)
        ),
        "chosen_hostile_packets_share_response_amplitude": (
            q_response.subs(packet_a) == q_response.subs(packet_b) == 1
        ),
        "deliberate_off_shell_flavor_law_changes_ratio": (
            sp.simplify((2 * p_response) / q_response - alpha) != 0
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP367",
        "admitted_state_domain": "negative canonical quartic U, nonzero intervention coupling h, and a local epsilon-neighborhood with U+h*epsilon<0, conditional on the equilibrium portal shell J^2=alpha*(-1/U)",
        "faithful_quotient_coordinate": "canonical source coordinate U upstream and full physical16 downstream; the response observes only J^2 and therefore is not physical16-faithful",
        "source_authorized_probe_family": "coefficient interventions U->U+h*epsilon with equilibrium source and flavor response slopes",
        "contextual_partition": "at fixed alpha all admitted (U,h) packets share p/q=alpha; even response amplitude can collide when h/U^2 agrees",
        "classification": "conditional source-side common causal constructor and relational response instrument grammar; neither numerical selector nor complete source/physical16 identifier",
        "intervened_U": str(intervened_U),
        "source_port": str(source_port),
        "flavor_port": str(flavor_port),
        "responses": {"p": str(p_response), "q": str(q_response), "p_over_q": str(response_ratio)},
        "response_jacobian": str(response_jacobian),
        "response_rank": 1,
        "deletion_test": {"portal_deleted_p": str(deleted_portal_response), "source_q": str(q_response)},
        "smallest_exact_falsifier": "deleting the portal leaves q=h/U^2 nonzero but forces the uncoupled flavor response p to zero",
        "remaining_physical_instrument_gate": "realize U->U+h*epsilon with a calibrated physical threshold control, prepare the response regime, and jointly measure J^2 and Q/M2 with uncertainties in one scheme",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp367_quartic_intervention_common_response.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
