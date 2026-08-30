from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def matvec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def norm_squared(vector):
    return sum(value * value for value in vector)


def main() -> None:
    eta = Fraction(9, 25)
    sqrt_eta = Fraction(3, 5)
    assert sqrt_eta * sqrt_eta == eta

    # The accessible outputs of |0> and |1> under collection loss are
    # rho_0=|0><0| and rho_1=(1-eta)|0><0|+eta|1><1|.
    # Their trace distance is eta, versus one at the input.
    input_trace_distance = Fraction(1)
    accessible_trace_distance = eta
    assert accessible_trace_distance < input_trace_distance
    deterministic_exact_recovery_possible = accessible_trace_distance == input_trace_distance
    assert not deterministic_exact_recovery_possible

    minimum_bloch_margin = eta
    formal_inverse_gain = 1 / minimum_bloch_margin
    assert formal_inverse_gain == Fraction(25, 9)

    no_loss_filter = ((Fraction(1), Fraction(0)), (Fraction(0), sqrt_eta))
    recovery_filter = ((sqrt_eta, Fraction(0)), (Fraction(0), Fraction(1)))
    probes = {
        "zero": (Fraction(1), Fraction(0)),
        "one": (Fraction(0), Fraction(1)),
        "superposition": (Fraction(3, 5), Fraction(4, 5)),
    }
    success_probabilities = {}
    for name, probe in probes.items():
        no_loss = matvec(no_loss_filter, probe)
        recovered_unnormalized = matvec(recovery_filter, no_loss)
        expected = tuple(sqrt_eta * value for value in probe)
        assert recovered_unnormalized == expected
        success_probabilities[name] = norm_squared(recovered_unnormalized)
        assert success_probabilities[name] == eta

    assert len(set(success_probabilities.values())) == 1

    result = {
        "schema": "marici.aspect.imperfect-environment-access.v1",
        "status": "pass",
        "collection_efficiency": str(eta),
        "input_orthogonal_trace_distance": str(input_trace_distance),
        "accessible_output_trace_distance": str(accessible_trace_distance),
        "deterministic_exact_recovery_possible": deterministic_exact_recovery_possible,
        "minimum_bloch_reconstruction_margin": str(minimum_bloch_margin),
        "formal_inverse_gain": str(formal_inverse_gain),
        "heralded_recovery_exact_for_all_probes": True,
        "heralded_total_success_probability": str(eta),
        "success_probability_input_independent": len(set(success_probabilities.values())) == 1,
        "verdict": "Any unmonitored missing environment fraction forbids deterministic exact recovery because accessible trace distance contracts. With a monitored no-loss branch, a compensating filter recovers every input exactly with input-independent total success probability eta.",
        "claim_boundary": "ideal single-qubit collection loss with perfect loss heralding and exact filtering; no dark counts, mode mismatch, multiphoton terms, or detector dead time",
    }
    output = Path(__file__).parents[1] / "results" / "imperfect_environment_access.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
