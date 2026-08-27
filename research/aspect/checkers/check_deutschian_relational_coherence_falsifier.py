from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "deutschian_relational_coherence_falsifier.json"


def parity(gamma, kappa_a, kappa_b, sewing, cosine):
    visibility = gamma * kappa_a * kappa_b * sewing
    return ((1 + visibility * cosine) / 2,
            (1 - visibility * cosine) / 2)


def main():
    gamma = F(3, 5)
    phases = (F(1), F(0), F(-1), F(0))
    interventions = {
        "coherent_sewing": (F(1), F(1), F(1), gamma),
        "one_wing_dephased": (F(0), F(1), F(1), F(0)),
        "local_record_measured_and_forgotten": (F(0), F(1), F(1), F(0)),
        "record_coherently_retained_and_uncomputed": (F(1), F(1), F(1), gamma),
        "classical_record_comparison": (F(1), F(1), F(0), F(0)),
        "vacuum_port_sewing_tau_9_25": (F(1), F(1), F(9, 25), F(27, 125)),
    }
    curves = {}
    for name, (ka, kb, sewing, expected_visibility) in interventions.items():
        curve = [parity(gamma, ka, kb, sewing, c)[0] for c in phases]
        visibility = curve[0] - curve[2]
        assert visibility == expected_visibility
        curves[name] = {
            "even_probabilities": [str(x) for x in curve],
            "visibility": str(visibility),
        }

    conditioned_plus = [(1 + gamma * c) / 2 for c in phases]
    conditioned_minus = [(1 - gamma * c) / 2 for c in phases]
    totalized = [(a + b) / 2 for a, b in zip(conditioned_plus, conditioned_minus)]
    assert all(x == F(1, 2) for x in totalized)

    falsifiers = {
        "local_phase_fringe_above_tolerance": "falsifies relational-only localization",
        "zero_joint_fringe_with_verified_nonzero_gamma_and_coherent_sewing": "falsifies odd-port promotion",
        "unconditional_fringe_after_entanglement_breaking_measurement": "falsifies coherent-constructor necessity",
        "unconditional_fringe_from_classical_record_join": "falsifies sewing-versus-conditioning distinction",
        "visibility_not_multiplicative_after_independence_is_certified": "falsifies the finite composition law",
    }
    out = {
        "schema": "marici.aspect.deutschian-relational-coherence-falsifier.v1",
        "status": "pass",
        "prediction": "joint visibility equals gamma*kappa_A*kappa_B*sewing while both local marginals remain flat",
        "gamma": str(gamma), "curves": curves,
        "conditioned_fibers": {
            "plus": [str(x) for x in conditioned_plus],
            "minus": [str(x) for x in conditioned_minus],
            "unconditional_totalization": [str(x) for x in totalized],
        },
        "falsifiers": falsifiers,
        "standard_quantum_status": "the finite probability law agrees with ordinary quantum mechanics; the Deutschian content is the constructor-level counterfactual explanation",
        "independence_gate": "kappa_A*kappa_B is predicted only for interventions whose joint phase channel is independently certified to factorize",
        "sewing_authority_gate": "partial sewing must be implemented by a full vacuum-port unitary dilation; its visible round-trip factor is not an abstract fitted scalar",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
