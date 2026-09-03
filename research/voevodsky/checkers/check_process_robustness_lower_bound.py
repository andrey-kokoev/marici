from __future__ import annotations

import json
from fractions import Fraction


def mix(x: tuple[Fraction, Fraction], noise: tuple[Fraction, Fraction], s: Fraction) -> tuple[Fraction, Fraction]:
    return tuple((coordinate + s * noise_coordinate) / (1 + s) for coordinate, noise_coordinate in zip(x, noise))  # type: ignore[return-value]


def in_free_square(point: tuple[Fraction, Fraction]) -> bool:
    return all(0 <= coordinate <= 1 for coordinate in point)


def main() -> None:
    a = Fraction(1, 8)
    witness_noise_bound = Fraction(1)
    lower_bound = a / witness_noise_bound
    assert lower_bound == Fraction(1, 8)

    tight_process = (Fraction(-1, 8), Fraction(0))
    tight_noise = (Fraction(1), Fraction(0))
    assert not in_free_square(tight_process)
    assert in_free_square(mix(tight_process, tight_noise, lower_bound))
    assert not in_free_square(mix(tight_process, tight_noise, lower_bound - Fraction(1, 100)))

    strict_process = (Fraction(-1, 8), Fraction(-1))
    strict_noise = (Fraction(1), Fraction(1))
    assert not in_free_square(mix(strict_process, strict_noise, lower_bound))
    assert in_free_square(mix(strict_process, strict_noise, Fraction(1)))

    # Exhaust exact candidate noises from free-square vertices: no s<a can work.
    vertices = [(Fraction(i), Fraction(j)) for i in (0, 1) for j in (0, 1)]
    smaller_s = lower_bound - Fraction(1, 100)
    assert all(not in_free_square(mix(tight_process, noise, smaller_s)) for noise in vertices)

    result = {
        "schema": "marici.voevodsky.process-robustness-lower-bound.v1",
        "status": "affine_witness_process_lower_bound_verified",
        "witness_value": "-1/8",
        "witness_noise_upper_bound": "1",
        "conditional_process_robustness_lower_bound": "1/8",
        "tight_process_fixture": True,
        "strict_process_fixture_exact_robustness": "1",
        "scalar_bound_can_be_strict": True,
        "physical_associator_process_typed": False,
        "exact_physical_process_robustness_computed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
