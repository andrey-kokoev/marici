from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def scale(vector, factor):
    return tuple(factor * value for value in vector)


def norm_squared(vector):
    return sum(value * value for value in vector)


def main() -> None:
    horizontal = (Fraction(0), Fraction(0), Fraction(1))
    vertical = (Fraction(0), Fraction(0), Fraction(-1))
    diagonal = (Fraction(1), Fraction(0), Fraction(0))
    circular = (Fraction(0), Fraction(1), Fraction(0))
    probes = (horizontal, vertical, diagonal, circular)

    depolarization = Fraction(1, 2)
    contraction = 1 - depolarization
    outputs = tuple(scale(probe, contraction) for probe in probes)
    assert contraction == Fraction(1, 2)
    assert all(norm_squared(output) == Fraction(1, 4) for output in outputs)
    recovered_horizontal = scale(outputs[0], 1 / contraction)
    assert recovered_horizontal == horizontal

    # The algebraic inverse is not positive on the whole physical output ball.
    valid_observed_state = (Fraction(0), Fraction(0), Fraction(3, 4))
    assert norm_squared(valid_observed_state) <= 1
    formal_inverse_state = scale(valid_observed_state, 1 / contraction)
    assert norm_squared(formal_inverse_state) == Fraction(9, 4) > 1

    near_complete_depolarization = Fraction(99, 100)
    near_contraction = 1 - near_complete_depolarization
    inverse_gain = 1 / near_contraction
    assert inverse_gain == 100

    complete_outputs = tuple(scale(probe, Fraction(0)) for probe in probes)
    assert len(set(complete_outputs)) == 1

    result = {
        "schema": "marici.aspect.depolarizing-pilot-inverse.v1",
        "status": "pass",
        "depolarization": str(depolarization),
        "bloch_contraction": str(contraction),
        "tomographic_probe_output_norm_squared": "1/4",
        "exact_image_inverse_recovers_horizontal": True,
        "valid_observed_state": [str(value) for value in valid_observed_state],
        "formal_inverse_state": [str(value) for value in formal_inverse_state],
        "formal_inverse_state_norm_squared": str(norm_squared(formal_inverse_state)),
        "formal_inverse_positive_on_full_state_space": False,
        "near_complete_depolarization": str(near_complete_depolarization),
        "near_complete_inverse_gain": str(inverse_gain),
        "complete_depolarization_output_count": len(set(complete_outputs)),
        "verdict": "Spanning tomography identifies a depolarizing pilot channel. For nonzero contraction its linear inverse recovers exact image records, but the inverse is not a physical positive map on arbitrary observed states and amplifies deviations by 1/(1-p). At p=99/100 the gain is 100; at complete depolarization all probes coincide and inversion is impossible. Calibration identifies the channel, not a universally physical undo operation.",
        "claim_boundary": "exact unital isotropic qubit depolarization represented on Bloch vectors with perfect process tomography; no anisotropy, nonunital loss, finite-sample tomography, environment access, or regularized state estimation",
    }
    output = Path(__file__).parents[1] / "results" / "depolarizing_pilot_inverse.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
