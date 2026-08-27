from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def contaminated_fidelity(alpha, beta, epsilon):
    # Fidelity of (1-epsilon)|psi><psi| + epsilon|0><0| with |psi>.
    overlap_with_false_state_squared = alpha * alpha
    return (1 - epsilon) + epsilon * overlap_with_false_state_squared


def main() -> None:
    epsilon = Fraction(1, 100)
    # Avoid irrational arithmetic in the equal-superposition case by using its
    # known |<0|psi>|^2=1/2.
    fidelities = {
        "zero": contaminated_fidelity(Fraction(1), Fraction(0), epsilon),
        "one": contaminated_fidelity(Fraction(0), Fraction(1), epsilon),
        "equal_superposition": (1 - epsilon) + epsilon * Fraction(1, 2),
    }
    assert fidelities["zero"] == 1
    assert fidelities["one"] == Fraction(99, 100)
    assert fidelities["equal_superposition"] == Fraction(199, 200)
    average_fidelity = sum(fidelities.values()) / len(fidelities)
    worst_case_fidelity = min(fidelities.values())
    assert average_fidelity == Fraction(199, 200)
    assert worst_case_fidelity == Fraction(99, 100)

    dark_probability = Fraction(1, 100)
    independent_dual_false_probability = dark_probability * dark_probability
    assert independent_dual_false_probability == Fraction(1, 10000)
    assert independent_dual_false_probability > 0

    result = {
        "schema": "marici.aspect.false-herald-recovery-boundary.v1",
        "status": "pass",
        "accepted_false_event_fraction": str(epsilon),
        "probe_fidelities": {name: str(value) for name, value in fidelities.items()},
        "average_probe_fidelity": str(average_fidelity),
        "worst_case_probe_fidelity": str(worst_case_fidelity),
        "zero_probe_is_blind": fidelities["zero"] == 1,
        "exact_conditional_recovery": all(value == 1 for value in fidelities.values()),
        "single_false_herald_probability": str(dark_probability),
        "independent_dual_false_herald_probability": str(independent_dual_false_probability),
        "dual_herald_restores_exactness": independent_dual_false_probability == 0,
        "verdict": "A one-percent accepted false-herald fraction leaves average spanning-probe fidelity 199/200 but destroys exact conditional recovery and gives worst-case fidelity 99/100. Independent dual heralding suppresses the error quadratically without restoring exactness.",
        "claim_boundary": "fixed |0> false-event contamination and independent redundant heralds; no state-dependent dark counts, afterpulsing, common-mode pickup, or finite-sample confidence bounds",
    }
    output = Path(__file__).parents[1] / "results" / "false_herald_recovery_boundary.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
