from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def matvec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


def norm_squared(vector):
    return sum(value * value for value in vector)


def main() -> None:
    zero = Fraction(0)
    one = Fraction(1)

    # Basis order: |00>, |01>, |10>, |11>. This is the complete-damping
    # dilation, extended unitarily outside the occupied environment input.
    complete_dilation = (
        (one, zero, zero, zero),
        (zero, zero, one, zero),
        (zero, -one, zero, zero),
        (zero, zero, zero, one),
    )
    inverse_dilation = transpose(complete_dilation)

    probes = {
        "zero": (one, zero),
        "one": (zero, one),
        "plus": (Fraction(3, 5), Fraction(4, 5)),
    }
    reduced_system_populations = {}
    recovered = {}
    environment_states = {}
    for name, (alpha, beta) in probes.items():
        joint_input = (alpha, zero, beta, zero)
        joint_output = matvec(complete_dilation, joint_input)
        assert joint_output == (alpha, beta, zero, zero)
        assert norm_squared(joint_output) == norm_squared(joint_input) == one

        # Both environment amplitudes accompany system state |0>.
        reduced_system_populations[name] = (norm_squared(joint_output[:2]), norm_squared(joint_output[2:]))
        assert reduced_system_populations[name] == (one, zero)
        environment_states[name] = joint_output[:2]

        restored = matvec(inverse_dilation, joint_output)
        assert restored == joint_input
        recovered[name] = restored == joint_input

    assert len(set(reduced_system_populations.values())) == 1
    assert len(set(environment_states.values())) == len(probes)

    # A rational beamsplitter rotation: survival amplitude 3/5 and transfer
    # amplitude 4/5. Reduced damping is 16/25; its least Bloch contraction is
    # 1-gamma = 9/25, while the joint rotation remains norm preserving.
    survival_amplitude = Fraction(3, 5)
    transfer_amplitude = Fraction(4, 5)
    damping_probability = transfer_amplitude * transfer_amplitude
    reduced_minimum_margin = survival_amplitude * survival_amplitude
    reduced_inverse_gain = one / reduced_minimum_margin
    assert damping_probability == Fraction(16, 25)
    assert reduced_minimum_margin == Fraction(9, 25)
    assert reduced_inverse_gain == Fraction(25, 9)

    result = {
        "schema": "marici.aspect.environment-assisted-channel-recovery.v1",
        "status": "pass",
        "complete_damping_reduced_output_count": len(set(reduced_system_populations.values())),
        "complete_damping_environment_record_count": len(set(environment_states.values())),
        "joint_inverse_recovers_all_probes": all(recovered.values()),
        "partial_transfer_survival_amplitude": str(survival_amplitude),
        "partial_transfer_amplitude": str(transfer_amplitude),
        "partial_damping_probability": str(damping_probability),
        "reduced_minimum_reconstruction_margin": str(reduced_minimum_margin),
        "reduced_inverse_gain": str(reduced_inverse_gain),
        "joint_unitary_minimum_margin": "1",
        "verdict": "At complete amplitude damping all reduced system records coincide, while a retained coherent environment port contains distinct input states and the inverse dilation restores every probe exactly. Environment-assisted recovery is a larger typed instrument, not an inverse licensed by reduced tomography.",
        "claim_boundary": "ideal two-qubit amplitude-damping dilation with perfect coherent environment access and exact pure-state probes; no finite visibility, uncontrolled bath dimension, detector loss, or thermalization",
    }
    output = Path(__file__).parents[1] / "results" / "environment_assisted_channel_recovery.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
